from settings import *
import os
####################
#   AWS SETTINGS   #
####################
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
AWS_PRELOAD_METADATA = True
AWS_CLOUDFRONT_DOMAIN = 'd1jriduhx7su5v.cloudfront.net'
AWS_S3_SECURE_URLS = False
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
AWS_STORAGE_BUCKET_NAME = 'restorethefourth'
CLOUDFRONT_URL = "http://" + AWS_CLOUDFRONT_DOMAIN + "/"
S3_URL = "http://"+ AWS_STORAGE_BUCKET_NAME +".s3.amazonaws.com/"
COMPRESS_ENABLED = False
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = 'storage.CachedS3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
]
STATIC_URL = CLOUDFRONT_URL
MEDIA_URL = STATIC_URL + "media/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
