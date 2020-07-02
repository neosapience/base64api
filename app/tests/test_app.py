from app import app
import json
import jsend


def test_decode():
    cli = app.test_client()
    src = 'aGVsbG8gd29ybGQ='
    r = cli.post(
        '/api/decode',
        headers={'X-Base64-Access-Key': 'helloworld'},
        content_type='application/json',
        data=json.dumps({'src': src})
    )
    assert 200 == r.status_code
    ret = r.get_json()
    assert jsend.is_success(ret)
    assert ret['data']['result'] == 'hello world'


def test_decode_403():
    cli = app.test_client()
    r = cli.post('/api/decode', headers={'X-Base64-Access-Key': 'error'}, content_type='application/json')
    assert 403 == r.status_code

    r = cli.post('/api/decode', headers={'X-Key': 'error'}, content_type='application/json')
    assert 403 == r.status_code


def test_health():
    cli = app.test_client()
    r = cli.get('/')
    assert 200 == r.status_code
