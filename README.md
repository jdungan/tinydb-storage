Install

`pip install -r requirements.txt`

Usage


```
from tinydb import TinyDB, Query

from s3_storage import S3Storage

s3_db = TinyDB('db2.json', storage=S3Storage)
```
