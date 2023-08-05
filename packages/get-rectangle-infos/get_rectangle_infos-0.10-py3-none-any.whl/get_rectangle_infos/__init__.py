from flatten_everything import flatten_everything
from more_itertools import chunked
from collections import namedtuple

rectinfos = namedtuple(
    "Rect",
    [
        "format_1x4",
        "format_4x2",
        "format_2x2",
        "height",
        "width",
        "area",
        "center",
    ],
)


def get_rectangle_information(rect):
    rect = list(flatten_everything(rect))
    rect1, rect2, rect3 = None, None, None
    if len(rect) not in [4, 8]:
        raise ValueError("I need either 4 or 8 numbers to calculate the rectangle")
    if len(rect) == 4:
        X1, Y1, X2, Y2 = rect
        rect1 = tuple(rect)
        rect2 = [(X1, Y1), (X2, Y1), (X2, Y2), (X1, Y2)]
        rect3 = [tuple(p) for p in (chunked(rect, 2))]
    elif len(rect) == 8:
        rect1 = rect[0], rect[1], rect[4], rect[5]
        rect2 = [tuple(p) for p in (chunked(rect, 2))]
        rect3 = [tuple(p) for p in (chunked(rect1, 2))]
    height = rect1[3] - rect1[1]
    width = rect1[2] - rect1[0]
    area = height * width
    centerx = rect1[0] + width // 2
    centery = rect1[1] + height // 2
    result = rectinfos(
        format_1x4=rect1,
        format_4x2=rect2,
        format_2x2=rect3,
        height=height,
        width=width,
        area=area,
        center=(centerx, centery),
    )

    return result
