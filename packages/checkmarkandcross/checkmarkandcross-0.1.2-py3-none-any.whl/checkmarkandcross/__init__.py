from os import path

from IPython.display import Image
import base64


def __get_file(checkmark: bool, size: int):
    filename = f'{"checkmark" if checkmark else "cross"}_{size}.png'
    return path.join(path.dirname(__file__), filename)


def image(checkmark: bool, size: int = 32) -> Image:
    return Image(filename=__get_file(checkmark, size))


def image_bytes(checkmark: bool, size: int = 32) -> bytes:
    with open(__get_file(checkmark, size), 'rb') as file:
        return file.read()


def image_base64(checkmark: bool, size: int = 32) -> str:
    b64data = base64.b64encode(image_bytes(checkmark, size)).decode('utf-8')
    return f'data:image/png;base64,{b64data}'


def image_html(checkmark: bool, size: int = 32, title: str = None) -> str:
    b64data = image_base64(checkmark, size)
    return f'<img src="{b64data}" title="{title}" alt="{title}">'
