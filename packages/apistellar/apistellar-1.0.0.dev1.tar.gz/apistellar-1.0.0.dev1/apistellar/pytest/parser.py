"""
{
 "mocks": [
   {"obj": "paas_backend.Mongo",
    "methods": [
          {"name": "find_one",
           "async": true,
           "ret_val": "1111"}
        ],
    "props": [
          {"name": "TABLE",
           "val": "user_test"
        ],
    }
 ]
}
"""
import json
import asyncio

from toolkit import load_class as _load


class Method(object):

    def __init__(self, obj, name, ret_val, async=False, ret_factory=None):
        self.obj = obj
        self.name = name
        self.ret_val = ret_val
        self.async = async
        self.ret_factory = ret_factory and _load(ret_factory)

    def __call__(self, *args, **kwargs):
        if self.ret_factory:
            factory = self.ret_factory(*args, **kwargs)
            return factory.result()
        else:
            if self.async:
                loop = asyncio.get_event_loop()
                future = loop.create_future()
                future.set_done(self.ret_val)
                return future
            else:
                return self.ret_val

    def __iter__(self):
        yield self.obj, self.name, self


class Prop(object):

    def __init__(self, obj, name, ret_val):
        self.obj = obj
        self.name = name
        self.ret_val = ret_val

    def __iter__(self):
        yield self.obj, self.name, self.ret_val


class Object(object):

    def __init__(self, mock):
        self.obj_name = mock["obj"]
        self.obj = _load(self.obj_name)
        self.elements = set()
        for method in mock["methods"]:
            self.elements.add(Method(self.obj, **method))
        for prop in mock["props"]:
            self.elements.add(Prop(self.obj, **prop))

    def find(self, obj_name, name):
        if self.obj_name == obj_name:
            for element in self.elements:
                if element.name == name:
                    return element


class Parser(object):

    def __init__(self, config_path):
        self.meta = json.load(open(config_path))
        self.objects = [Object(mock) for mock in self.meta["mocks"]]

    def find_mock(self, *mock_names):
        mocks = set()

        for mock_name in mock_names:
            obj_name, prop = mock_name.rpartition(".")

            for obj in self.objects:
                mock = obj.find(obj_name, prop)
                if mock:
                    mocks.add(mock)
                    break
            else:
                print(f"Mock of {mock_name} not found. ")
        return mocks

