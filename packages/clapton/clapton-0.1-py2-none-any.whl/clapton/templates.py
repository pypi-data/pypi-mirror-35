from clapton import templates

def get_template(name):
    return getattr(templates, name)


def text():
    return """swagger: '2.0'
info:
  title: Text prediction API
  version: "0.1"
  description: predict
consumes:
  - application/json
produces:
  - application/json

paths:
  /predict/{data}:
    post:
      summary: Predict text data for given model
      description: text prediction
      operationId: run.prediction
      responses:
        200:
          description: Prediction response
          schema:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      parameters:
        - name: data
          in: path
          description: Text input for predictions.
          required: true
          type: array
          items:
            type: string"""


def sequence():
    pass


def image():
    pass