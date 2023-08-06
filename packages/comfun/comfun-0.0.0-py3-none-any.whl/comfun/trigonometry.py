import math
from decimal import Decimal


def get_angle_adj_hyp(adj: Decimal, hyp: Decimal, unit: str = "deg") -> Decimal:
    """
    Get angle between adjacent and hypothenuse of a right triangle.
    :param adj: length of the adjacent (ankathete)
    :param hyp: length of the hypothenuse
    :param unit: "deg" or "rad"
    :return:
    """
    cos_alpha = adj / hyp
    angle = Decimal(math.acos(cos_alpha))
    if unit.lower() == "deg":
        angle = Decimal(math.degrees(angle))
    return angle


def get_angle_opp_hyp(opp: Decimal, hyp: Decimal, unit: str = "deg") -> Decimal:
    """
    Get angle between opposite and hypothenuse of a right triangle.
    :param opp: length of the opposite (Gegenkathete)
    :param hyp: length of the hypothenuse
    :param unit: "deg" or "rad"
    :return:
    """
    sin_alpha = opp / hyp
    angle = Decimal(math.asin(sin_alpha))
    if unit.lower() == "deg":
        angle = Decimal(math.degrees(angle))
    return angle


def get_angle_opp_adj(opp: Decimal, adj: Decimal, unit: str = "deg") -> Decimal:
    """
    Get angle between opposite and adjacent of a right triangle.
    :param opp: length of the opposite (Gegenkathete)
    :param adj: length of the adjacent (Ankathete)
    :param unit: "deg" or "rad"
    :return:
    """
    tan_alpha = opp / adj
    angle = Decimal(math.asin(tan_alpha))
    if unit.lower() == "deg":
        angle = Decimal(math.degrees(angle))
    return angle

