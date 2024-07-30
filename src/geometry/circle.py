from math import pi


def calculate_area(r):
    """ 
    Calculate the area of a circle. 

    This uses the standard mathematical calculation: 

    $\pi r ^2$

    Parameters
    ----------
    r : float, the radius 

    Returns
    -------
    float : the area of the cirlce
    """
    area = pi * r **2
    return area


def calculate_circ(r):
    """ 
    Calculate the circumference of a circle. 

    Parameters
    ----------
    r : float, the radius 

    Returns
    -------
    float : the circumeference of the cirlce
    """
    circ = 2 * pi * r
    return circ


def calculate_diam(r):
    """
    Calculate the diameter of a circle.

    Parameters
    ----------
    r : float, the radius

    Returns
    -------
    float : the diameter of the circle
    """
    diam = 2 * r
    return diam
