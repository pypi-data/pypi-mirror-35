#!/usr/bin/env python3
import logging
import numpy as np
import pandas as pd

from ..props import halfround

logger = logging.getLogger(__name__)


def _estimate_braceheight(drawlength):
    """
    Calculate an approximate brace height.

    Brace height, the distance from bowstring to bow when braced, but not
    drawn, is not only a matter of artefact properties, but also usage culture
    and shooter preference. Therefore, it can only be inferred with a degree of
    plausibility. Beckhoff assumed a brace height of 17 cm for the Vrees
    artefact without explaining his reasoning.

    Working from the assumption that generally, draw length falls close to
    limb length, and the latter is a measure more closely related to the
    working parts of the bow, and therefore a better base for guessing draw
    length from than NTN bow length (which may or may not include a stiff
    handle part).

    Args:
        drawlength (float): The bow’s draw length. (in cm)

    Returns:
        float: An assumed brace height. (in cm)
    """
    return drawlength*0.225


def _estimate_bowrating(ntnlength, drawlength):
    """
    Give a very approximate guess for a Beckhoff-G.

    Beckhoff’s ‘Bogengütefaktor’ (‘bow goodness’) G is a tough one.
    In ‘Die eisenzeitlichen Kriegsbogen von Nydam’, Offa 20/1963, he describes
    the method for deriving it as taking equally spaced draw force values from
    a bow’s force–draw curve and dividing their mean by maximum draw weight.
    A linear increase in draw weight results in a G of 0.5.

    A low (<0.5) value is both an indicator for an unpleasant phenomenon called
    ‘stacking’, and its correlating lower energy storage compared to a
    non-stacking bow.

    Without a testable artefact, this value must be either guessed from
    experience or approximated from bow and limb/draw length with a lot of
    hand-wringing.

    Args:
        ntnlength (float): Nock-to-nock length of the bow. (in cm)
        drawlength (float): Draw length of the bow. (in cm)

    Returns:
        float: A shamefully guessed approximation of G. (scalar)
    """
    # *flails arms* *waves hands*
    return 0.23783*ntnlength/drawlength


def _estimate_draw_force_roundup(force):
    """
    Round up maximum permissible force roughly like Beckhoff.

    Beckhoff calculates a maximum permissible force to reach yew’s flexural
    strength at the Vrees artefact’s profiles ranging from 26.8 kp to 36.6 kp.
    He continues calculating with a value slightly rounded-up from the strict
    minimum: 28 kp. This simulates the magnitude of his rounding by converting
    to kp, adding 1 & rounding to the next int, then converting back to N.

    Args:
        force (float): The force value to be rounded up. (in N)

    Returns:
        float: The rounded-up value. (in N)
    """
    return np.ceil(force/9.807+1)*9.807


def _calculate_max_force(l, W, MoR):
    """
    Return the force at nock that causes maximum strain at profile.

    Args:
        l (float): Profile distance to nock, i.e. lever length. (in cm)
        W (float): Profile’s section modulus. (in cm^3)
        MoR (float): Material’s modulus of rupture. (in Pa)

    Returns:
        float: Amount of force to make profile reach limit. (in N)
    """
    # convert MoR from Pa (N/m^2) to N/cm^2
    MoR = MoR*1E-4
    return (W/l) * MoR


def _calculate_mean_I(F, limblength, MoR):
    """
    Approximate I for whole bow after Beckhoff.

    To approximate a mean area moment of inertia for the entire bow, Beckhoff
    assumes l/S (nock distance, section modulus) to be constant, then
    calculates an S for the bow’s centre and derives an area moment of inertia
    from it under assumption of a half-circle cross-section.

    Since beam theory assumes a constant I, this value gets multiplied with
    (‘mathematically and empirically derived’) 0.425, to account for the bow’s
    taper.

    Args:
        F (float): Maximum permissible force to pull a limb. (in N)
        limblength (float): distance from nock to bow centre. (in cm)
        MoR (float): Material’s flexural strength. (in Pa)

    Returns:
        float: Beckhoff’s approximation of I. (in cm^4)
    """
    # convert MoR from Pa (N/m^2) to N/cm^2
    MoR = MoR*1E-4
    # step 1: transpose W to centre, based on P and constant l/W
    W_centre = (F/MoR) * limblength
    # step 2: calculate I_centre from W_centre with beckhoffs approximations:
    # W_semicircle := d^3/31
    # I_semicircle := d^4/145
    d = (W_centre * 31) ** (1/3.0)
    I_centre = d**4 / 145
    # step 3: multiply with 0.425 to account for tapered profile
    return 0.425 * I_centre


def _calculate_deflection(I_mean, ntnlength, P, MoE):
    """
    Calculate a bow’s deflection after Beckhoff.

    Args:
        I (float): The bow’s mean area moment of inertia. (in cm^4)
        ntnlength (float): The bow’s effective (NTN) length. (in cm)
        P (float): The force pushing the bow’s centre. (in N)
        MoE (float): The material’s modulus of elasticity. (in Pa)

    Returns:
        float: The distance of deflection between tips and centre.
          (in cm)
    """
    # convert MoE from Pa (N/m^2) to N/cm^2
    MoE = MoE*1E-4
    return (P * ntnlength**3) / (48 * MoE * I_mean)


def _calculate_limb_capacity(F, deflection, braceheight):
    """
    Calculate a limb’s work capacity after Beckhoff.

    Args:
        F (float): The force pushing the bow’s centre. (in N)
        deflection (float): The amount of tip deflection. (in cm)
        braceheight (float): The bow’s brace height. (in cm)

    Returns:
        float: The limb’s work capacity. (in J)
    """
    return 0.5 * F * (deflection - (braceheight**2)/deflection) / 100


def _calculate_draw_weight(energy, G, drawlength, braceheight):
    """
    Calculate draw weight after Beckhoff.

    Args:
        energy (float): The bow’s work capacity. (in J)
        G (float): The bow’s ‘Bogengüte’ factor. (scalar)
        drawlength (float): The bow’s draw length. (in cm)
        braceheight (float): The bow’s brace height. (in cm)

    Returns:
        float: The force required to bring the bow to full draw. (in N)
    """
    # convert dl, s_p from cm to m
    drawlength = drawlength/100
    braceheight = braceheight/100
    powerstroke = drawlength - braceheight
    return energy / (G * powerstroke)


def beckhoff1964(data, MoE, MoR, name=None,
                 shape=halfround, G=None, braceheight=None,
                 strict=False):
    """
    Calculate bow properties from a DataFrame of measurements after Beckhoff.

    This formula reconstructs Beckhoff’s calculation in ‘Der Eibenbogen von
    Vrees’ in: Die Kunde N.F. 15 (1964) as accurately as possible, amending
    Beckhoff’s manual work and judgements from experience with formulaic
    approximations where necessary.

    Args:
        data (pd.DataFrame): A dataframe containing a sequence of measurements
          for profiles along a half-bow’s length, nock to centre. As a minimum,
          data points for longitudinal position are required (data['l'], in cm,
          distance to nock), as well as width and thickness (data['width'] and
          data['thickness'], in cm). Optionally, columns data['I'] (in cm^4),
          data['e_belly'] (in cm), and data['W_belly'] (in cm^3) can be
          provided.
        MoE (float): modulus of elasticity for the bow’s material. (in Pa)
        MoR (float): modulus of rupture for the bow’s material. (in Pa)

    Kwargs:
        name (str): A name for the bow. If given, it will be inserted into the
          result pd.Series as name.
        shape (function): A bundle function to supply limb cross-section
          properties. As a default, a semi-elliptical cross-section with flat
          belly is assumed.
        G (float): A Beckhoff bow goodness factor; 0.5 for a linear draw force
          increase, smaller values for a stacking bow, larger for a convex
          force-draw curve. If no value is provided, a rough approximation will
          be estimated.
        braceheight (float): Bow brace height. If no value is provided, a rough
          approximation will be estimated. (in cm)
        strict (bool): Indicates whether to calculate bending force
          strictly by material stress levels or apply an approximation of
          Beckhoff’s rounding up. (default)

    Returns:
        tuple
        0: a pd.Series with draw weight in N, draw length, brace height, set,
          & effective bow length (nock-to-nock) in cm, and work capacity in J.
        1: a pd.DataFrame with profile data, according to the table in
          Beckhoff, 1964.
    """
    df = data.copy()
    required_columns = {'I', 'e_belly'}
    for col in required_columns.difference(df.columns):
        df[col] = shape(df['width'], df['thickness'], [col])
        logger.debug("Required column %s not found in DataFrame. " +
                     "Calculated from supplied function.",
                     col)
    if 'W_belly' not in df.columns:
        df['W_belly'] = df['I'] / df['e_belly']
        logger.debug("Required column W_belly not found in DataFrame. " +
                     "Calculated from columns I and e_belly")

    if 'l/W_belly' not in df.columns:
        df['l/W_belly'] = df['l'] / df['W_belly']
        logger.debug("Required column l/W_belly not found in DataFrame. " +
                     "Calculated from columns l and W_belly")
    if 'F' not in df.columns:
        df['F'] = _calculate_max_force(df['l'], df['W_belly'], MoR)
        logger.debug("Required column F not found in DataFrame. " +
                     "Calculated from function")

    limblength = df['l'].max()
    ntnlength = 2 * limblength
    stringfollow = ntnlength / 25.0

    if strict:
        maxforce = df['F'].min()
    else:
        maxforce = _estimate_draw_force_roundup(df['F'].min())
        logger.debug("Applying Beckhoff’s draw force round-up. " +
                     "Rounded up from %s to %s",
                     df['F'].min(),
                     maxforce)

    I_centre = _calculate_mean_I(maxforce, limblength, MoR)

    maxdeflection = _calculate_deflection(I_centre, ntnlength, 2*maxforce, MoE)
    drawlength = 2*maxdeflection

    if braceheight is None:
        braceheight = _estimate_braceheight(drawlength)
        logger.debug('No braceheight supplied. Calculating an estimate.')

    energy = 2*_calculate_limb_capacity(maxforce, maxdeflection, braceheight)

    if G is None:
        G = _estimate_bowrating(ntnlength, drawlength)
        logger.debug('No G supplied. Calculating an estimate.')

    drawweight = _calculate_draw_weight(energy, G, drawlength, braceheight)

    # TODO centralise series index, series data from dict
    return pd.Series([drawweight,
                      drawlength,
                      braceheight,
                      ntnlength,
                      stringfollow,
                      energy],
                     index=['drawweight',
                            'drawlength',
                            'braceheight',
                            'ntnlength',
                            'set',
                            'energy'],
                     name=name), df
