import json
from dataclasses import dataclass
from types import SimpleNamespace

from dataclasses_json import dataclass_json


@dataclass
class Image:
    src: str
    name: str
    hOffset: int
    vOffset: int
    alignment: str


@dataclass
class Text:
    data: str
    size: int
    style: str
    name: str
    hOffset: int
    vOffset: int
    alignment: str
    onMouseUp: str


@dataclass
class Window:
    title: str
    name: str
    width: int
    height: int


@dataclass
class Widget:
    debug: str
    window: Window
    image: Image
    text: Text


@dataclass_json
@dataclass
class SampleJson:
    widget: Widget


def return_json_as_typed_object() -> SampleJson:
    with open('sample.json') as json_file:
        json_dict = json.load(json_file)
        json_object = SampleJson.from_dict(json_dict)
    return json_object


def return_json_as_dynamic_object():
    with open('sample.json') as json_file:
        obj = json.load(json_file, object_hook=lambda x: SimpleNamespace(**x))
    return obj
