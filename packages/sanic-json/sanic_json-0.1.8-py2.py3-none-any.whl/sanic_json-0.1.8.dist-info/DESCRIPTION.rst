# sanic json

A thin wrapper on sanic web framework to help writting JSON API

```
pip3 install sanic-json
```

## Exmaple

file `api/random.py`

```python
def obj_to_dict(obj):
    if not obj or isinstance(obj, (str, int, float)):
        return obj
    elif isinstance(obj, list):
        return [obj_to_dict(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: obj_to_dict(v) for k, v in obj.items()}
    else:
        return {k: obj_to_dict(v) for k, v in obj.__dict__.items()}


# the wrapper will get the args and kwargs value from the `request`
async def random_pohoto(req, count=10):
    res = api.photo.random(count=count)
    return {"data": obj_to_dict(res)}
```

file `app.py`

```python
from sanic import Sanic
from sanic_json import get_json_route
from api.random import random_pohoto

app = Sanic()
json_route = get_json_route(app)

json_route("/api/random", random_pohoto)


if __name__ == "__main__":
    import os

    debug = True if os.getenv("DEBUG") else False
    # hot reload in next release: https://github.com/channelcat/sanic/issues/168
    app.run(host="0.0.0.0", port=8000, debug=debug)
```


