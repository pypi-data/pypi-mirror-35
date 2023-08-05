import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey
from datetime import datetime
import hashlib
from sqlalchemy import create_engine, Float, ARRAY

from sharelock_utils.history_meta import Versioned, versioned_session

Base = declarative_base()


def get_db_conn(null_pool=False):
    host = os.environ.get('db_host')
    name = os.environ.get('db_name')
    user = os.environ.get('db_user')
    password = os.environ.get('db_password')
    full_path = 'postgresql://{user}:{password}@{host}/{db}'.format(user=user, password=password, host=host, db=name)
    if null_pool:
        engine = create_engine(full_path, poolclass=NullPool)
    else:
        engine = create_engine(full_path)
    return engine


def get_engine_and_base(null_pool=False):
    engine = get_db_conn(null_pool)
    existing_base = automap_base()
    existing_base.prepare(engine, reflect=True)
    return engine, existing_base


def get_session(engine=None):
    if not engine:
        engine = get_db_conn()

    Session = sessionmaker(bind=engine)
    versioned_session(Session)
    return Session()


def create_tables(engine):
    Base.metadata.create_all(engine)


class Feed(Base):
    __tablename__ = 'feeds'
    id = Column(Integer, primary_key=True)
    source = Column(String(20))
    name = Column(String(50))
    url = Column(String(50))
    last_update = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    top_news = Column(Boolean, default=False)

    def __repr__(self):
        return "source={} - name={}".format(self.source, self.name)


class Post(Base):
    MAX_URL_LEN = 2000
    __tablename__ = 'posts'
    id = Column(String(40), primary_key=True)
    feed = Column(Integer, ForeignKey(Feed.id))
    url = Column(String(MAX_URL_LEN))
    article_url = Column(String(MAX_URL_LEN))
    article_url_strip = Column(String(MAX_URL_LEN), index=True)
    insertion_date = Column(DateTime, default=datetime.utcnow)
    publish_date = Column(DateTime, nullable=True)
    message = Column(String)

    def __repr__(self):
        return "url={} message={}".format(self.url, self.message)


class PostLastMetricPrediction(Base):
    __tablename__ = 'post_last_metric_prediction'
    post_id = Column(String(40), ForeignKey('posts.id'), primary_key=True)
    updated_at = Column(DateTime)


class MetricMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def post_id(cls):
        return Column(String(40), ForeignKey('posts.id'), primary_key=True)

    insertion_date = Column(DateTime, default=datetime.utcnow)


class TwitterMixin(object):
    likes = Column(Integer)
    retweets = Column(Integer)

    def __repr__(self):
        return "post={} likes={} rt={}".format(self.post_id, self.likes, self.retweets)


class Twitter_Post_Metric(Versioned, Base, MetricMixin, TwitterMixin):
    pass


class Twitter_Post_Metric_Prediction(Base, MetricMixin, TwitterMixin):
    pass


class Twitter_Search_Metric(Versioned, Base, MetricMixin, TwitterMixin):
    pass


class RedditMixin(object):
    upvotes = Column(Integer)
    comments = Column(Integer)

    def __repr__(self):
        return "post={} upvotes={} comments={}".format(self.post_id, self.upvotes, self.comments)


class Reddit_Post_Metric(Versioned, Base, MetricMixin, RedditMixin):
    pass


class Reddit_Post_Metric_Prediction(Base, MetricMixin, RedditMixin):
    pass


class HN_Post_Metric(Versioned, Base, MetricMixin, RedditMixin):
    pass


class HN_Post_Metric_Prediction(Base, MetricMixin, RedditMixin):
    pass


class FacebookMixin(object):
    reactions = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)

    def __repr__(self):
        return "post={} reactions={} comments={} shares={}".format(self.post_id, self.upvotes, self.comments, self.shares)


class Facebook_Post_Metric(Versioned, Base, MetricMixin, FacebookMixin):
    pass


class Facebook_Post_Metric_Prediction(Base, MetricMixin, FacebookMixin):
    pass


class Post_Platform_Relevance(Base):
    __tablename__ = 'post_platform_relevance'
    post_id = Column(String(40), ForeignKey('posts.id'), primary_key=True)
    hn_relevance = Column(Float)


def get_hash_wrapper(context):
    fields = context.get_current_parameters()
    return get_hash(fields['title'], fields['body'])


def get_hash(title, body):
    text = ' '.join([title, body])
    return hashlib.md5(text.encode()).hexdigest()


class URLcontent(Base):
    __tablename__ = 'url_content'
    parsed_url = Column(String, primary_key=True)
    title = Column(String)
    headlines = Column(String, nullable=True)
    body = Column(String, nullable=True)
    publish_date = Column(DateTime, nullable=True)
    content_hash = Column(String(32), index=True, default=get_hash_wrapper)

    def __repr__(self):
        return "parsed_url={} - title={}".format(self.parsed_url, self.title[:15])


class ContentTopic(Base):
    __tablename__ = 'content_class'
    id = Column(Integer, primary_key=True)
    parsed_url = Column(String, ForeignKey(URLcontent.parsed_url), index=True)
    rank = Column(Integer)
    topic = Column(String(32), index=True)
    probability = Column(Float)


class URLmeta(Base):
    __tablename__ = 'url_meta'
    url = Column(String, index=True, primary_key=True)
    parsed_url = Column(String, ForeignKey(URLcontent.parsed_url), index=True)
    insertion_date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "parsed_url={} - url={}".format(self.parsed_url, self.url)


class Clusters(Base):
    __tablename__ = 'clusters'
    id = Column(Integer, primary_key=True)
    insertion_date = Column(DateTime, default=datetime.utcnow)
    categories = Column(ARRAY(String(32)))  # TODO validate this
    topics = Column(ARRAY(String(32)))
    # posts = relationship("Post2Cluster")


class Post2Cluster(Base):
    __tablename__ = 'post2cluster'

    id = Column(Integer, primary_key=True)
    cluster_id = Column(Integer, ForeignKey('clusters.id'), index=True)
    post_id = Column(String(40), ForeignKey('posts.id'), index=True)
    insertion_date = Column(DateTime, default=datetime.utcnow)

