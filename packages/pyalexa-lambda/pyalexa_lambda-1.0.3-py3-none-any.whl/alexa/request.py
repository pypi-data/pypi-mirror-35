# coding: utf-8

from .session import Session


class Request:
    def __init__(self, request):
        self.__session = Session(request)
        self.__request = request
        if "request" in request and "intent" in request["request"] and "slots" in request["request"]["intent"]:
            self.__slots = request["request"]["intent"]["slots"]
        else:
            self.__slots = {}

    @property
    def session(self) -> Session:
        return self.__session

    def has_slot(self, name) -> bool:
        if name not in self.__slots:
            return False
        return "value" in self.__slots[name]

    def get_slot(self, name, id=False, raise_non_exist=True):
        if not self.has_slot(name):
            if raise_non_exist:
                raise KeyError("slot {} not found".format(name))
            return None
        if id:
            return self.__slots[name]["resolutions"]["resolutionsPerAuthority"][0]["values"][0]["value"]["id"]
        return self.__slots[name]["value"]

    @property
    def type(self) -> str:
        return self.__request["request"]["type"]

    @property
    def intent(self) -> str:
        return self.__request["request"]["intent"]["name"]
