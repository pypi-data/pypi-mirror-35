# coding: utf-8

import enum
import typing


class SpeechResponseType(enum.Enum):
    PlainText = "PlainText"
    Ssml = "SSML"


class CardResponseType(enum.Enum):
    Simple = "Simple"
    Standard = "Standard"
    LinkAccount = "LinkAccount"


class Response:
    def __init__(self, attributes=None):
        self.__version = "1.0"
        if attributes is None:
            attributes = {}
        self.__session_attributes = attributes
        self.__response = {}
        self.__end_session = False

    def add(self, key, value):
        self.__session_attributes[key] = value

    @staticmethod
    def _output_speech_factory(text=None, ssml=None) -> typing.Dict[str, typing.Any]:
        if text is None and ssml is None:
            raise RuntimeError("output speech must be set text or ssml parameter")
        data = {}
        if text is not None:
            data["type"] = SpeechResponseType.PlainText.value
            data["text"] = text
        else:
            data["type"] = SpeechResponseType.Ssml.value
            data["ssml"] = ssml
        return data

    def output_speech(self, text=None, ssml=None):
        data = Response._output_speech_factory(text, ssml)
        self.__response["outputSpeech"] = data

    def card(self, ctype: CardResponseType, title=None, text=None, context=None, image=None):
        data = {"type": ctype.value}
        if title is not None:
            data["title"] = title

        if text is not None:
            data["text"] = text

        if context is not None:
            data["context"] = context

        if image is not None:
            data["image"] = image

        self.__response["card"] = data

    def reprompt(self, text=None, ssml=None):
        data = Response._output_speech_factory(text, ssml)
        self.__response["reprompt"] = {}
        self.__response["reprompt"]["outputSpeech"] = data

    @property
    def is_end_session(self) -> bool:
        return self.__end_session

    @is_end_session.setter
    def is_end_session(self, value: bool):
        self.__end_session = value

    @property
    def response(self) -> typing.Dict[str, typing.Any]:
        res = self.__response
        res["shouldEndSession"] = self.is_end_session
        return {
            "version": self.__version,
            "sessionAttributes": self.__session_attributes,
            "response": res
        }
