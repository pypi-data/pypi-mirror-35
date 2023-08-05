from functools import partial
from sanic.response import json


def check_result(rv):
    if isinstance(rv, tuple):
        rv = rv[0]
        other = rv[1]
        if isinstance(other, dict):
            rv_kw = other
        elif isinstance(other, int):
            rv_kw = {"status": other}
        else:
            raise Exception("unaccepted second return value: {}".format(other))
    else:
        rv_kw = {}

    if isinstance(rv, dict):
        if 'success' not in rv:
            rv['success'] = True if rv_kw.get('status', 200) == 200 else False

        return json(rv, **rv_kw)
    else:
        return rv


def check_response(fn):
    async def new_fn(*args, **kwargs):
        try:
            rv = await fn(*args, **kwargs)
        except Exception as e:
            rv = ({"success": False, "reason": str(e), "type": str(type(e))}, 500)

        return check_result(rv)

    return new_fn


def add_route(app, url, fn):
    app.route(url)(fn)


def json_route(app, url, fn):
    add_route(app, url, check_response(fn))


def get_json_route(app):
    return partial(json_route, app)
