from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.insert({'name': "'John'", 'City': 'Tulsa'})
db.insert({'name': "'Luke'", 'City': 'Tulsa'})
