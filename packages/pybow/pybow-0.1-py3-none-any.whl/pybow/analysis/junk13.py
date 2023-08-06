#!/usr/bin/env python3
import logging
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def _get_bowfactors(ntnlength):
    """
    Get draw length and draw weight reduction factors from Junkmanns’ table.

    Junkmanns assumes draw length from a bow’s NTN length by a simple
    correlation table. A reduction factor for the resulting draw weight is
    supplied as well.

    Args:
        ntnlength (float): a bow’s nock-to-nock length. (in cm)

    Returns:
        tuple
        0: float: draw length (in cm)
        1: float: draw weight reduction factor (scalar)
    """
    jjfactors = np.array([[np.inf, 70.0, 1.00],
                          [150, 65.0, 0.88],
                          [140, 60.0, 0.78],
                          [130, 55.0, 0.69],
                          [120, 50.0, 0.59],
                          [110, 45.0, 0.52],
                          [100, 40.0, 0.42],
                          [90, 35.0, 0.34],
                          [80, 30.0, 0.26],
                          [70, 25.0, 0.17],
                          [60, 20.0, 0.09]])
    match = jjfactors[jjfactors[:, 0] > ntnlength][-1]
    return match[1], match[2]


def junkmanns2013(data, correlationfactor, spread=None, name=None):
    """
    Calculate bow parameters from a DataFrame of measurements after Junkmanns.

    This formula reconstructs Junkmanns’ simplified calculation method from
    Pfeil und Bogen – von der Altsteinzeit bis zum Mittelalter.
    Ludwigshaven 2013.

    It is a notably flawed and imprecise method, basing energy storage on
    section modulus proportions (w×t^2) instead of area moment of inertia
    (w×t^3), draw length by a tabular look-up from bow length and converting
    a strictly scalar result (‘Bogenstärke’ Bs) to units of force via an
    empirically derived correlation factor. (n=20 for yew, n=6 for elm)

    Args:
        data (pd.DataFrame): A dataframe containing a sequence of
          measurements for profiles along a half-bow’s length, nock to
          centre.
          As a minimum, data points for longitudinal position are required
          (data['l'], in cm, distance from nock), as well as width and
          thickness (in cm).
        correlationfactor (float): Junkmanns’ correlation factor for the wood
          species used. Junkmanns’ factors are supplied in pybow.data, along
          with their spread +/- of nominal result.

    Kwargs:
        spread (float): Percentual spread in a Junkmanns correlation factor.
          If given, upper and lower ends of the drawweight spread will be
          calculated.
        name (str): A name for the bow. If given, it will be inserted into the
          result pd.Series as name.

    Returns:
        tuple
        0: a pd.Series with draw weight, its lower and upper bounds in N,
          draw length, brace height, & effective bow length
          (nock-to-nock) in cm.
        1: a pd.DataFrame with profile data, according to the tables in
          Junkmanns, 2013.
    """
    df = data.copy()
    if 'Qs' not in df.columns:
        df['Qs'] = df['width'] * df['thickness']**2
        logger.debug("Required column Qs not found in DataFrame. " +
                     "Calculating values from columns width and thickness.")
    if 'Bw' not in df.columns:
        df['Bw'] = df['l'] / df['Qs']
        logger.debug("Required column Bw not found in DataFrame. " +
                     "Calculating values from columns l and Qs.")

    # NB.: excluding by values of l instead of just the first entry (where l=0)
    # because JJ ignores measurements like the nock ‘wings’ at l=0.5 in vrees-1
    Bw_mean = df[df['l'] > 2.0]['Bw'].mean()
    ntnlength = 2*df['l'].max()
    drawlength, reduction = _get_bowfactors(ntnlength)
    Bs = 100 / (Bw_mean * (ntnlength/100)**2)

    # 4.448 will convert draw weight from lbf to N
    drawweight = Bs * 4.448 * correlationfactor * reduction

    if spread is not None:
        drawweight_low = drawweight * (1-spread)
        drawweight_high = drawweight * (1+spread)
    else:
        drawweight_low = np.nan
        drawweight_high = np.nan
        logger.debug("No spread supplied. " +
                     "drawweight_high and drawweight_low set to NaN.")

    return pd.Series([drawweight,
                      drawweight_low,
                      drawweight_high,
                      drawlength,
                      ntnlength],
                     index=['drawweight',
                            'drawweight_low',
                            'drawweight_high',
                            'drawlength',
                            'ntnlength'],
                     name=name), df
