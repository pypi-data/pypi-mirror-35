#!/usr/bin/env python3
import numpy as np


# Physical Property Functions
# Rectangle
def rect_I(w, t):
    """Return second moment of area for rectangular cross-sections.

    I_rect = (w×t^3)/12
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return (w * t**3) / 12


def rect_W(w, t):
    """Return section modulus for rectangular cross-sections.

    W_rect = (w×t^2)/6
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return (w * t**2) / 6


def rect_e_back(w, t):
    """Return distance centroid–back for rectangular cross-sections.

    e_back_rect = t/2
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return t / 2


def rect_e_belly(w, t):
    """Return distance centroid–belly for rectangular cross-sections.

    e_belly_rect = t/2
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return rect_e_back(w, t)


def rect_e(w, t):
    """Return maximum centroid distance for rectangular cross-sections.

    e_rect = t/2
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return rect_e_back(w, t)


# Ellipse
def round_I(w, t):
    """Return second moment of area for elliptic cross-sections.

    I_round = pi/4 × [(w/2)×(t/2)^3]
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    a = t/2
    b = w/2
    return (np.pi/4) * (b * a**3)


def round_W(w, t):
    """Return section modulus for elliptic cross-sections.

    W_round = pi/4 × [(w/2)×(t/2)^2]
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    a = t/2
    b = w/2
    return (np.pi/4) * (b * a**2)


def round_e_back(w, t):
    """Return distance centroid–back for elliptic cross-sections.

    e_back_round = t/2
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return t / 2


def round_e_belly(w, t):
    """Return distance centroid–belly for elliptic cross-sections.

    e_belly_round = t/2
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return round_e_back(w, t)


def round_e(w, t):
    """Return maximum centroid distance for elliptic cross-sections.

    e_round = t/2
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return round_e_back(w, t)


# Half-ellipse (round back/flat belly)
def halfround_I(w, t):
    """Return second moment of area for semi-elliptic cross-sections.

    I_halfround = (pi/8 - 8/9pi) × (w/2)×t^3
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    b = w/2
    return (np.pi/8 - 8/(9*np.pi)) * b * t**3


def halfround_W(w, t):
    """Return section modulus for semi-elliptic cross-sections.

    W_halfround = [(9pi^2-64) / (3pi-4)] × [(w/2)t^2 / 24]
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    b = w/2
    return ((9*np.pi**2 - 64) / (3*np.pi - 4)) * ((b*t**2) / 24)


def halfround_e_back(w, t):
    """Return distance centroid–back for semi-elliptic cross-sections.

    e_back_halfround = (1 - 4/3pi) × t
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return (1 - 4/(3*np.pi)) * t


def halfround_e_belly(w, t):
    """Return distance centroid–belly for semi-elliptic cross-sections.

    e_belly_halfround = t - e_back_halfround

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return t - halfround_e_back(w, t)


def halfround_e(w, t):
    """Return maximum centroid distance for semi-elliptic cross-sections.

    e_halfround = (1 - 4/3pi) × t
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return halfround_e_back(w, t)


# English style half-ellipse (round belly/flat back)
def english_I(w, t):
    """Return second moment of area for english style cross-sections.

    I_english = (pi/8 - 8/9pi) × (w/2)×t^3
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return halfround_I(w, t)


def english_W(w, t):
    """Return section modulus for english style cross-sections.

    W_english = [(9pi^2-64) / (3pi-4)] × [(w/2)t^2 / 24]
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return halfround_W(w, t)


def english_e_back(w, t):
    """Return distance centroid–back for english style cross-sections.

    e_back_english = t - e_belly_english

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return halfround_e_belly(w, t)


def english_e_belly(w, t):
    """Return distance centroid–belly for english style cross-sections.

    e_belly_english = (1 - 4/3pi) × t
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return halfround_e_back(w, t)


def english_e(w, t):
    """Return maximum centroid distance for english style cross-sections.

    e_english = (1 - 4/3pi) × t
    Source: Lueger 1904

    Args:
        w: width
        t: thickness

    Returns:
        A scalar.
    """
    return halfround_e_back(w, t)


# Trapezium
def trap_I(w, t, ratio):
    """Return second moment of area for trapezoid cross-sections.

    I_trap = (w^2 + 4wW + W^2)/(w+W) × t^3/36
    Source: Lueger 1904

    Args:
        w: width
        t: thickness
        ratio: the ratio of back width to belly width

    Returns:
        A scalar.
    """
    sw = ratio * w
    return (sw**2 + 4*sw*w + w**2) / (sw+w) * t**3/36


def trap_W(w, t, ratio):
    """Return section modulus for trapezoid cross-sections.

    W_trap = (w^2 + 4wW + W^2)/(w+2W) × t^2/12
    Source: Lueger 1904

    Args:
        w: width
        t: thickness
        ratio: the ratio of back width to belly width

    Returns:
        A scalar.
    """
    sw = ratio * w
    return (sw**2 + 4*sw*w + w**2) / (sw + 2*w) * t**2/12


def trap_e_back(w, t, ratio):
    """Return distance centroid–back for trapezoid cross-sections.

    e_back_trap = (w+2W)/(w+W) * t/3
    Source: Lueger 1904

    Args:
        w: width
        t: thickness
        ratio: the ratio of back width to belly width

    Returns:
        A scalar.
    """
    sw = ratio * w
    return (sw + 2*w) / (sw+w) * t/3


def trap_e_belly(w, t, ratio):
    """Return distance centroid–belly for trapezoid cross-sections.

    e_belly_trap = t - e_back_trap

    Args:
        w: width
        t: thickness
        ratio: the ratio of back width to belly width

    Returns:
        A scalar.
    """
    return t - trap_e_back(w, t, ratio)


def trap_e(w, t, ratio):
    """Return maximum centroid distance for trapezoid cross-sections.

    e_trap = (w+2W)/(w+W) * t/3
    Source: Lueger 1904

    Args:
        w: width
        t: thickness
        ratio: the ratio of back width to belly width

    Returns:
        A scalar.
    """
    return trap_e_back(w, t, ratio)


# Bundle Property Functions
def _bundlefunc(funcs, props, args):
    """Return the results of functions looked up in a dict, for args.

    Args:
        funcs (dict): A dictionary to look up functions in
        props (list): A list of funcs keys to return
        args: Arguments to feed into functions

    Returns:
        A tuple of results, if props contains more than one item.
        Just the plain result otherwise.
    """
    if len(props) == 1:
        return funcs[props[0]](*args)
    else:
        return tuple(funcs[prop](*args) for prop in props)


def rect(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for rectangular profiles.

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': rect_I,
             'W': rect_W,
             'e_back': rect_e_back,
             'e_belly': rect_e_belly,
             'e': rect_e}
    return _bundlefunc(funcs, props, [w, t])


def round(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for elliptical profiles.

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': round_I,
             'W': round_W,
             'e_back': round_e_back,
             'e_belly': round_e_belly,
             'e': round_e}
    return _bundlefunc(funcs, props, [w, t])


def halfround(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for half-round profiles. (flat belly)

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': halfround_I,
             'W': halfround_W,
             'e_back': halfround_e_back,
             'e_belly': halfround_e_belly,
             'e': halfround_e}
    return _bundlefunc(funcs, props, [w, t])


def english(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for half-round profiles. (flat back)

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': english_I,
             'W': english_W,
             'e_back': english_e_back,
             'e_belly': english_e_belly,
             'e': english_e}
    return _bundlefunc(funcs, props, [w, t])


def trap50(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for trapezoid profiles with ratio 0.5.

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': trap_I,
             'W': trap_W,
             'e_back': trap_e_back,
             'e_belly': trap_e_belly,
             'e': trap_e}
    return _bundlefunc(funcs, props, [w, t, 0.5])


def trap66(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for trapezoid profiles with ratio 0.66.

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': trap_I,
             'W': trap_W,
             'e_back': trap_e_back,
             'e_belly': trap_e_belly,
             'e': trap_e}
    return _bundlefunc(funcs, props, [w, t, 2/3])


def trap75(w, t, props=['I', 'W', 'e']):
    """Return beam theory properties for trapezoid profiles with ratio 0.75.

    Args:
        w: width
        t: thickness

    Kwargs:
        props (list): A list of beam theory properties to return.
          Allowed values: 'I', 'W', 'e', 'e_back', 'e_belly'
          Default: ['I', 'W', 'e']

    Returns:
        A tuple of results if props contains more than one item.
        Just the plain result otherwise.
    """
    funcs = {'I': trap_I,
             'W': trap_W,
             'e_back': trap_e_back,
             'e_belly': trap_e_belly,
             'e': trap_e}
    return _bundlefunc(funcs, props, [w, t, 0.75])
