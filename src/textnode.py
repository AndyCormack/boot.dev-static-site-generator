from enum import Enum


class TextType(Enum):
    Normal = "normal"
    Bold = "bold"
    Italic = "italic"
    Code = "code"
    Links = "link"
    Images = "image"


class TextNode:
    def __init__(self, text, text_type: TextType = TextType.Normal, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
