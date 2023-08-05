class MissingQueryException(Exception):
    pass


def valida_request_query(req, *args, **kwargs):
    q_args = []
    q_kwargs = {}
    for k in args:
        if k not in req.args:
            raise MissingQueryException("missing {}".format(k))
        else:
            # only need the first
            q_args.append(req.args[k][0])

    for k, default in kwargs.items():
        # only need the first
        req.args.get(k, [default])[0]

    return q_args, q_kwargs
