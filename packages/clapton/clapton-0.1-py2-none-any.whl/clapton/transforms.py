from clapton import transforms
from clapton import base

import boto


def get_transform(name):
    return getattr(transforms, name)


def scikit(local=False):
    from sklearn.externals import joblib

    if not local:
        conn = boto.connect_s3(host=base.get_aws_s3_host())
        bucket = conn.get_bucket(base.get_bucket())
        key_obj = boto.s3.Key(bucket)
        key_obj.key = base.get_prep_file_name()
        contents = key_obj.get_contents_to_filename(base.get_prep_local_path())
    return joblib.load(base.get_prep_local_path())
