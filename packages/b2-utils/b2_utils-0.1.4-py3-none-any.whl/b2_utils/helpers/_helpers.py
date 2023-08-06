import random

__all__ = [
    "random_hex_color",
]


def random_hex_color() -> str:
    return "#%06x".upper() % random.randint(0, 0xFFFFFF)
