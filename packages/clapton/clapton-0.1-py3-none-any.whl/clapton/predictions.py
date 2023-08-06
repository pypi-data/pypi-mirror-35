from clapton import predictions
from clapton import base

import boto

def get_predictor(name):
    return getattr(predictions, name)


def keras(model, data, payload):
    predictions = model.predict(data)
    list_preds = [str(x[0]) for x in predictions]  # TODO: make proper numeric type
    
    output = dict(zip(payload, list_preds))
    return output