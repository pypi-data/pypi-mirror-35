import importlib, json

class NoSQLBackend:

    def __get_serializer_class(self, serializer_path):
        bits = serializer_path.split('.')
        class_name = bits.pop()
        module_string = (".").join(bits)
        mod = importlib.import_module(module_string)
        return getattr(mod, class_name)

    def get_serialized(self, instance, created = False):
        serializer = self.__get_serializer_class(instance.serializer_path)
        dta = serializer(instance).data
        id = str(instance.id)
        return (id, dta)

class RedisBackend(NoSQLBackend):
    '''
    usage:
    ```
    collection = RedisBackend(connection).collection('todos')
    collection.set(TodoSerializer, todo)
    '''

    def __init__(self, connection):
        self.redis = connection

    def __get_key(self, instance):
        return "{}.{}".format(self.collection, instance.pk)

    def collection(self, name):
        self.collection = name
        return self # this is so we can chain

    def set(self, serializer, instance):
        key = self.__get_key(instance)
        value = serializer(instance).data
        as_string = json.dumps(value)
        self.redis.set(key, as_string)
        return value

    def get(self, instance):
        key = self.__get_key(instance)
        value = self.redis.get(key)
        if value is None: return None
        return json.loads(value)

    def delete(self, instance):
        key = self.__get_key(instance)
        self.redis.delete(key)
