#!/usr/bin/env python

import reconocedor as recon
from flask import Flask
from flask import request
from flask import jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route("/reconocedor/<name>",methods=['POST'])
def reconocer_service(name):
    result = recon.reconocer(request.data)
    return jsonify(result)

if __name__ == '__main__':
#DEBUG    app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=8085)

