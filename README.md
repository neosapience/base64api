# base64 API
> To test typecast SDK 3rd party authorization

## api example
```bash
curl -XPOST http://localhoost:5000/api/decode \
  -d '{"src": "aGVsbG8gd29ybGQ="}'

{
    "status": "success",
    "data": {
        "result": "hello world"
    }
}
```
