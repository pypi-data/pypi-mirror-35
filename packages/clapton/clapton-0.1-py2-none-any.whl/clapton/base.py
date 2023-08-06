import json
import os
from subprocess import call

from clapton.transforms import get_transform
from clapton.models import get_model
from clapton.predictions import get_predictor

cwd = os.getcwd()
clapton_path = os.path.join(cwd, "clapton_settings.json")

with open(clapton_path, 'r') as cf:
    _CLAPTON_JSON = json.loads(cf.read())

def show_configs():
    print(_CLAPTON_JSON)
    print('\n==========\n\n')
    print(_ZAPPA_JSON)

zappa_path = os.path.join(cwd, "zappa_settings.json")
# TODO: set slimhandler

with open(zappa_path, 'r') as zf:
    _ZAPPA_JSON = json.loads(zf.read())

BUCKET_NAME = _ZAPPA_JSON['dev']['s3_bucket'] # TODO: "dev" hardcoded
PREP_FILE_NAME = _CLAPTON_JSON['preprocessing_path']
PREP_LOCAL_PATH = PREP_FILE_NAME
MODEL_FILE_NAME = _CLAPTON_JSON['model_path']
MODEL_LOCAL_PATH = MODEL_FILE_NAME
REGION = _ZAPPA_JSON['dev']['aws_region']
AWS_S3_HOST = 's3.{}.amazonaws.com'.format(REGION)
MODEL_TYPE = _CLAPTON_JSON['model_type']
PREP_TYPE = _CLAPTON_JSON['preprocessing_type']

def copy_model_to_s3():
    # TODO: can I also upload swagger.json like this?
    call(['aws', 's3', 'cp', MODEL_LOCAL_PATH, 's3://{}'.format(BUCKET_NAME)])
    if _CLAPTON_JSON['preprocessing']:
        call(['aws', 's3', 'cp', PREP_LOCAL_PATH, 's3://{}'.format(BUCKET_NAME)])


def get_bucket():
    return BUCKET_NAME


def get_prep_file_name():
    return PREP_FILE_NAME


def get_prep_local_path():
    return PREP_LOCAL_PATH


def get_model_file_name():
    return MODEL_FILE_NAME


def get_model_local_path():
    return MODEL_LOCAL_PATH


def get_aws_s3_host():
    return AWS_S3_HOST


def get_model_type():
    return MODEL_TYPE


def get_prep_type():
    return PREP_TYPE


def get_input_type():
    return _CLAPTON_JSON['input_type']


def predict(payload, local=False):
    # Transform
    transform_loader = get_transform(get_prep_type())
    data = transform_loader(local=local).transform(payload)

    # Model
    model_loader = get_model(get_model_type())
    model = model_loader(local=local)

    # Output
    predictor = get_predictor(get_model_type())
    output = predictor(model, data, payload)

    return json.dumps(output)