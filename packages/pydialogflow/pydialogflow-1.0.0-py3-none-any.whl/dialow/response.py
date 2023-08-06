class Response:
    def __init__(self, request, attributes=None):
        if attributes is None:
            attributes = {}
        self.__parameters = attributes
        self.__text = ""
        self.__card = None
        self.__request = request

    def add(self, key, value):
        self.__parameters[key] = value

    def output_speech(self, text, **_):
        self.__text = text

    def card(self, title=None, text=None, **_):
        self.__card = {
            "title": title,
            "subtitle": text
        }

    @property
    def response(self):
        res = {
            "fulfillmentText": self.__text,
            "outputContexts": [
                {
                    "name": "{session}/contexts/{name}".format(
                        name="session_attributes",
                        session=self.__request.session.id
                    ),
                    "lifespanCount": 5,
                    "parameters": self.__parameters
                }
            ]
        }

        if self.__card is not None:
            res["fulfillmentMessages"] = [
                self.__card
            ]

        return res
