PyDialogflow for HTTPS server
==================

&copy; 2018 SiLeader.

## features
+ PyAlexa (pyalexa-lambda) like syntax
+ simple system

## usage

### use Flask
```python3
from flask import Flask, request, jsonify
import dialow


app = Flask(__name__)


# Alexa like syntax
@app.route("/dialogflow/endpoint", methods=["POST"])
def dialogflow_endpoint():
    req = dialow.Request(request.json)

    if request.type == "IntentRequest":
        res = dialow.Response()
        res.output_speech(text="Dialogflow Test")
        return jsonify(res.response)

```

## License
Apache License 2.0

See LICENSE

## for Alexa
[GitHub](https://github.com/SiLeader/pyalexa)

