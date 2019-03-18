from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from tinydb.middlewares import CachingMiddleware

from s3_storage import S3Storage

s3Middleware = CachingMiddleware(S3Storage)

s3_db = TinyDB('db.json', storage=s3Middleware(MemoryStorage))
s3_db.insert({'name': "'Jeremy'", 'City': 'Tulsa'})
s3_db.insert({'name': "'Yahya'", 'City': 'Tulsa'})
