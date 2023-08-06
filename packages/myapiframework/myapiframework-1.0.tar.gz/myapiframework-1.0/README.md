# Myapi framework

Eazy python framework for beginers

> pip install myapiframework


```python
# main.py
from myapiframework import MyAPI
from myapiframework import Response
from myapiframework import parse_json, parse_form

app = MyAPI()


@app.get('/')
def home(request):
    data = {'message': 'hello'}
    return Response(status=200, data=data)

# get post with id 
@app.get('/post/{id}/')
def get_post(request, id):
    post = {
        'id': id,
        'name': 'myapi',
        'description': 'new framework myapi'
    }
    return Response(status=200, data=post)


# create post
@app.post('/post/')
def create_post(request):
    if request.content_type == 'application/json':
        data = parse_json(request.data)
        return Response(status=201, data=data)
    data = parse_form(request.data, request)
    return Response(status=201, data=data)
```

> gunicorn main:app

### methods:
- get
- post
- put
- patch
