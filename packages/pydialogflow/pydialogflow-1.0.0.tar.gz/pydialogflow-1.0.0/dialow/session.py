class Session:
    def __init__(self, req):
        self.__id = req["session"]
        self.__real_id = self.__id.split("/")[-1]
        req = req["queryResult"]
        self.__attributes = {}
        if "outputContexts" in req:
                sa = [c for c in req["outputContexts"] if c["name"] == self.__id + "/contexts/session_attributes"]
                print(sa)
                if len(sa) != 0:
                    self.__attributes = sa[0]["parameters"]

    @property
    def id(self):
        return self.__id

    @property
    def real_id(self):
        return self.__real_id

    @property
    def attributes(self):
        return self.__attributes
