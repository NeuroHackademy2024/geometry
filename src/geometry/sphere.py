from math import pi


def calculate_volume(r):
    """ 
    Calculate the volume of a sphere. 

    This uses the standard mathematical calculation: 

    $(4 * \pi r ^3) / 3$

    Parameters
    ----------
    r : float, the radius 

    Returns
    -------
    float : the volume of the sphere
    """

    volume = (4 * pi * r **3) / 3
    return volume