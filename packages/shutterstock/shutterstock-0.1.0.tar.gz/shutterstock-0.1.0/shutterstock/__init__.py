import inspect

from shutterstock import resources


class ConfiguredAPI:
    pass


def configure_api(api):
    res = ConfiguredAPI()

    for name, val in resources.__dict__.items():
        if inspect.isclass(val) and issubclass(val, resources.Resource):
            setattr(res, name, type(name, (val,), {'API': api}))

    return res


def configure(token):
    from shutterstock.api import ShutterstockAPI
    return configure_api(ShutterstockAPI(token))
