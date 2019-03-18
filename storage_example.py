from tinydb import TinyDB, Query
db = TinyDB('db.json')

from tinydb.middlewares import CachingMiddleware

from s3_storage import S3Storage

s3Middleware = CachingMiddleware(S3Storage)

subscriptions_tinydb = TinyDB('db.json', storage=s3Middleware)


db = TinyDB('db.json')
db.insert({'name': "'John'", 'City': 'Tulsa'})
db.insert({'name': "'Luke'", 'City': 'Tulsa'})
