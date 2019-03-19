from tinydb import TinyDB, Query

from s3_storage import S3Storage


s3_db = TinyDB('db.json', storage=S3Storage)

import ipdb; ipdb.set_trace()

s3_db.insert({'name': "'Jeremy'", 'City': 'Jenks'})
s3_db.insert({'name': "'Yahya'", 'City': 'Broken Arrow'})

import ipdb; ipdb.set_trace()
s3_db.search(Query()['name'] == 'Luke')
