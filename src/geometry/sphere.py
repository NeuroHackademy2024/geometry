from math import pi

def calculate_volume(r):
  """ 
    Calculate the volume of a sphere. 

    This uses the standard mathematical calculation: 

    $\(4/3) pi r ^3$

    Parameters
    ----------
    r : float, the radius 

    Returns
    -------
    float : the volume of the sphere
    """
    volume = (4/3) * pi * r **3
    return volume


def calculate_surface_area(r):
    """ 
    Calculate the surface area of a sphere. 

    This uses the standard mathematical calculation: 

    $4\pi r ^2$

    Parameters
    ----------
    r : float, the radius 

    Returns
    -------
    float : the surface area of the sphere
    """
    surface_area = 4 * pi * r **2
    return surface_area
