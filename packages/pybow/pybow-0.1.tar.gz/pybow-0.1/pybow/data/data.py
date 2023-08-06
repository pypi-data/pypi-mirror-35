#!/usr/bin/env python3

import pandas as pd

from ..bow import Bow

# BECKHOFF (1964)

# Material data from Beckhoff (1964):
# MoE: modulus of elasticity, given in Pa;
#      given by Beckhoff as 3/4 * 12000 kp/cm^2.
# MoR: modulus of rupture, given in Pa;
#      given by Beckhoff as 625 kp/cm^2.
beckhoff1964 = {'yew': {'MoE': 8.875E9,
                        'MoR': 61.29E6}}

_kb1964_vrees1_df = pd.DataFrame([[14.0, 2.2, 1.4, 0.36, 0.6],
                                  [19.3, 3.0, 1.55, 0.59, 0.65],
                                  [39.8, 4.8, 1.9, 1.84, 0.81],
                                  [48.0, 5.4, 2.1, 2.41, 0.86],
                                  [56.3, 5.3, 2.05, 2.64, 0.91],
                                  [68.6, 4.0, 2.4, 3.0, 1.0],
                                  [83.8, 2.6, 3.4, 5.71, 1.45]],
                                 columns=['l', 'width', 'thickness', 'I',
                                          'e_belly'])
beckhoff1964_vrees = \
    Bow('Vrees', 'Beckhoff 1964, p.118',
        material='yew',
        description='Demonstrator dataset in Beckhoff 1964; amended one '
                    'centre data point to make bow length readable from '
                    'the measurements.',
        limbs=[[_kb1964_vrees1_df, True, ()]])


# JUNKMANNS (2013)

# Correlation factors from Junkmanns (2013):
# corrfac: a correlation factor for a Junkmanns bow strength value into
#          draw weight in lbf.
# spread: the percentual spread +/- from the mean correlation factor to the
#         extreme values.
junkmanns2013 = {'yew': {'corrfac': 24.95328,
                         'spread': 0.35},
                 'elm': {'corrfac': 25.17568,
                         'spread': 0.21}}

# The Rotten Bottom Bow artefact used for demonstrating Junkmanns’ method
_jj2013_rb1_df = pd.DataFrame([[0.0, 0.9, 0.75],
                               [8.0, 1.58, 0.84],
                               [18.0, 2.0, 1.16],
                               [28.0, 2.15, 1.21],
                               [38.0, 2.71, 1.49],
                               [48.0, 2.69, 1.5],
                               [58.0, 2.64, 1.52],
                               [63.0, 2.7, 1.65],
                               [68.0, 2.55, 1.97],
                               [78.0, 2.11, 2.45],
                               [88.0, 1.9, 3.3]],
                              columns=['l', 'width', 'thickness'])
_jj2013_rb2_df = pd.DataFrame([[0.0, 2.77, 1.51],
                               [5.0, 2.72, 1.65],
                               [15.0, 2.27, 2.32],
                               [25.0, 1.9, 3.3]],
                              columns=['l', 'width', 'thickness'])
junkmanns2013_rottenbottom = \
    Bow('Rotten Bottom', 'Junkmanns 2013, p.199',
        material='yew',
        description='Demonstrator dataset in Junkmanns 2013',
        tags=['type:bodman'],
        limbs=[[_jj2013_rb1_df, True, ()], [_jj2013_rb2_df, False, ()]])
