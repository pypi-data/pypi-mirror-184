import os
import boto3
from botocore.exceptions import ClientError

class TkS3():
    def __init__(self, region=None):
        """
        :param region: The region for AWS S3
        """
        self.service_name = 's3'
        if region is None:
            region = os.getenv("S3_REGION")
        if region is None:
            region = os.getenv("REGION")
        if region is None:
            raise ValueError("REGION is missing in both ENV Variable and constructor params.")
        self.region = region
        self.access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.http_timeout = 60

    def get_client(self):
        if self.access_key is None or self.secret_key is None:
            self.client = boto3.client(service_name=self.service_name, region_name=self.region)
        else:
            self.client = boto3.client(service_name=self.service_name, region_name=self.region,
                                       aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        return self

    def get_resource(self):
        if self.access_key is None or self.secret_key is None:
            self.resource = boto3.resource(service_name=self.service_name, region_name=self.region)
        else:
            self.resource = boto3.resource(service_name=self.service_name, region_name=self.region,
                                           aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        return self

    def generate_presigned_get_url(self, s3_bucket, s3_key):
        self.get_client()
        url = self.client.generate_presigned_url('get_object', Params={'Bucket': s3_bucket, 'Key': s3_key}, ExpiresIn=3600)
        url = url.replace(f"s3.{self.region}.amazonaws.com/{s3_bucket}", f"{s3_bucket}.s3-{self.region}.amazonaws.com")
        return url

    def generate_presigned_post_url(self, s3_bucket, s3_key):
        self.get_client()
        url = self.client.generate_presigned_post(s3_bucket, s3_key, ExpiresIn=3600)
        return url

    def get_file_content(self, s3_bucket, s3_key):
        self.get_resource()
        obj = self.resource.Object(s3_bucket, s3_key)
        body = obj.get()['Body'].read().decode(encoding="utf-8", errors="ignore")
        return body

    def get_file_object(self, s3_bucket, s3_key):
        self.get_resource()
        return self.resource.Object(s3_bucket, s3_key).get()

    def upload_local_file_to_s3(self, s3_bucket, s3_key, local_path):
        try:
            self.get_client()
            self.client.upload_file(local_path, s3_bucket, s3_key)
            return True
        except Exception as e:
            print("Exception at upload_local_file_to_s3", str(e))
            return False





