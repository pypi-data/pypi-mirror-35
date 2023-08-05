# coding: utf-8

import typing


class Session:
    def __init__(self, context):
        if "session" in context:
            context = context["session"]
        self.__new = context["new"]
        self.__id = context["sessionId"]
        if "attributes" in context:
            self.__attributes = context["attributes"]
        else:
            self.__attributes = {}
        self.__application_id = context["application"]["applicationId"]
        self.__user_id = context["user"]["userId"]

        if "accessToken" in context["user"]:
            self.__access_token = context["user"]["accessToken"]
        else:
            self.__access_token = None

        if "permissions" in context["user"]:
            self.__permissions = context["user"]["permissions"]
        else:
            self.__permissions = {}

    @property
    def new(self) -> bool:
        return self.__new

    @property
    def id(self) -> str:
        return self.__id

    @property
    def attributes(self) -> typing.Dict[str, typing.Any]:
        return self.__attributes

    @property
    def application_id(self) -> str:
        return self.__application_id

    @property
    def user_id(self) -> str:
        return self.__user_id

    @property
    def access_token(self) -> typing.Optional[str]:
        return self.__access_token

    @property
    def permissions(self) -> typing.Dict[str, str]:
        return self.__permissions

