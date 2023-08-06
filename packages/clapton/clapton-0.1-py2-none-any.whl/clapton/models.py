from clapton import models
from clapton import base

import boto

def get_model(name):
    return getattr(models, name)


def keras(local=False):
    from keras.models import load_model

    if not local:
        conn = boto.connect_s3(host=base.get_aws_s3_host())
        bucket = conn.get_bucket(base.get_bucket())
        key_obj = boto.s3.Key(bucket)
        key_obj.key = base.get_model_file_name()
        contents = key_obj.get_contents_to_filename(base.get_model_local_path())
    return load_model(base.get_model_local_path())