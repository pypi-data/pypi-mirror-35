from .session import Session


class Request:
    def __init__(self, req):
        self.__session = Session(req)
        self.__request = req
        self.__result = req["queryResult"]

    def has_slot(self, name) -> bool:
        if "parameters" in self.__result:
            return name in self.__result["parameters"]
        return False

    def get_slot(self, name, *, raise_non_exist=True, **_):
        if not self.has_slot(name):
            if raise_non_exist:
                raise KeyError("slot {} not found".format(name))
            return None
        return self.__result["parameters"][name]

    @property
    def type(self):
        return "IntentRequest"

    @property
    def session(self):
        return self.__session

    @property
    def intent(self):
        return self.__result["intent"]["displayName"]
