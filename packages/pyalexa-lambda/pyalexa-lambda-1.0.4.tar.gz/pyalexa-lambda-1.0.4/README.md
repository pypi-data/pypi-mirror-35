PyAlexa for AWS lambda and HTTPS server
==================

&copy; 2018 SiLeader.

## usage

### use AWS Lambda
```python3
import alexa


def lambda_handler(data, _):
    request = alexa.Request(data)
    
    if request.type == "IntentRequest":
        response = alexa.Response()
        response.output_speech(text="Alexa Test")
        return response.response

```

### use Flask
```python3
from flask import Flask, request, jsonify
import alexa


app = Flask(__name__)


@app.route("/alexa/endpoint", methods=["POST"])
def alexa_endpoint():
    req = alexa.Request(request.json)

    if request.type == "IntentRequest":
        res = alexa.Response()
        res.output_speech(text="Alexa Test")
        return jsonify(res.response)

```

## License
Apache License 2.0

See LICENSE

## for Dialogflow
[GitHub](https://github.com/SiLeader/pydialogflow)

