Usage:

'''
from tinydb import TinyDB, Query
from tinydb.middlewares import CachingMiddleware

from .s3_storage import S3Storage

s3Middleware = CachingMiddleware(S3Storage)

subscriptions_tinydb = TinyDB(SUBSCRIPTIONS_DATABASE, storage=s3Middleware())

'''
