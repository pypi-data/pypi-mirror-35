
class Resource:
    API = None
    LIST = None
    GET = None
    CREATE = None
    UPDATE = None
    DELETE = None

    @classmethod
    def all(cls, **params):
        return cls.API.get(cls.LIST, **params)

    @classmethod
    def get(cls, **params):
        return cls.API.get(cls.GET, **params)


class Image(Resource):
    LIST = '/images'
    GET = '/images/{id}'


class ImageCollection(Resource):
    LIST = '/images/collections'
    GET = '/images/collections/{id}'


class ImageLicense(Resource):
    LIST = '/images/licenses'
