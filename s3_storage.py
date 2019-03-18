from io import BytesIO
import json

from tinydb import Storage
import boto3
import botocore

from settings import APPLICATION_BUCKET

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# make sure the bucket exists
try:
    s3.meta.client.head_bucket(Bucket=APPLICATION_BUCKET)
except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404' or error_code == '403':
            s3.create_bucket(Bucket=APPLICATION_BUCKET)
        else:
            raise e


class S3Storage(Storage):

    def __init__(self, filename):
        self.filename = filename
        # make sure the key exists
        try:
            s3_object = s3_client.get_object(Bucket=APPLICATION_BUCKET, Key=self.filename)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                s3.Bucket(APPLICATION_BUCKET).put_object(Key=self.filename, Body="{_default': {}}")
            else:
                raise

    def read(self):
        s3_object = s3_client.get_object(Bucket=APPLICATION_BUCKET, Key=self.filename)

        try:
            bytestream = BytesIO(s3_object['Body'].read())
            decode_stream = bytestream.read().decode('utf-8')
            data = json.loads(decode_stream)
            return data
        except:
            return None

    def write(self, data):
        file_data = bytes(json.dumps(data),'utf-8')
        s3.Bucket(APPLICATION_BUCKET).put_object(Key=self.filename, Body=file_data)

    def close(self):
        pass
