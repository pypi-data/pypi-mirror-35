from functools import partial
from sanic.response import json


def response_check(fn):
    async def new_fn(*args, **kwargs):
        try:
            rv = await fn(*args, **kwargs)
        except Exception as e:
            rv = ({"success": False, "reason": str(e), "type": str(type(e))}, 500)

        if isinstance(rv, tuple):
            other = rv[1]
            if isinstance(other, dict):
                rv_kw = other
            elif isinstance(other, int):
                rv_kw = {"status": other}
            else:
                raise Exception("unaccepted second return value: {}".format(other))
            rv = rv[0]
        else:
            rv_kw = {}

        if isinstance(rv, dict):
            return json(rv, **rv_kw)
        else:
            return rv

    return new_fn


def json_route(app, url, fn):
    app.route(url)(response_check(fn))


def get_json_route(app):
    return partial(json_route, app)
