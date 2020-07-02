from flask import Flask, request, jsonify, abort
from distutils.util import strtobool
import os
import jsend
import base64
app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return 'ok'



@app.route('/api/decode', methods=['POST'])
def decode():
    if strtobool(os.environ.get('ENABLE_AUTH_HEADER', 'false')):
        key = os.environ['AUTH_TOKEN_KEY']
        value = os.environ['AUTH_TOKEN']
        if value != request.headers.get(key):
            abort(403)

    data = request.get_json(True)
    if 'src' not in data:
        return jsonify(jsend.error('params/src'))

    try:
        src = str(data['src'])
        b = bytearray()
        b.extend(src.encode())
        ret = base64.decodebytes(b).decode('ascii')
        return jsonify(jsend.success({'result': ret}))
    except:
        return jsonify(jsend.error('app/decoding'))

