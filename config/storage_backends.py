from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = None


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = False
    file_overwrite = False
