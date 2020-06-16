from flask import Flask, request, jsonify, abort
import jsend
import base64
app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return 'ok'



@app.route('/api/decode', methods=['POST'])
def decode():    
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

