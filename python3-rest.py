#!/usr/bin/env python

import reconocedor as recon
from flask import Flask
from flask import request
from flask import jsonify
from train import trainRecognizer
from PIL import Image
import io
from flask_cors import CORS, cross_origin



app = Flask(__name__)
CORS(app)

@app.route("/reconocedor/<name>",methods=['POST'])
def reconocer_service(name):
    result = recon.reconocer(request.data)
    return jsonify(result)

@app.route("/entrenamiento",methods=['POST'])
def entrenamiento_service():
    trainRecognizer('train', showFaces=False, forceTrain=True)
    result = "Entrenamiento: OK"
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8085)

