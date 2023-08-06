########################################################################
#
# exsimcfg.py
#
#   EXSIM configuration
#
# Copyright (C) EXSIM Development Team
#
########################################################################

"""Configuration module of EXSIM (Experimental Simulator).

    This module implements a class that reads a configuration file,
    keeps the configuration in memory, and can be accessed for read only.

    It is based on the configparser library, which supports configuration
    files similar to INI files.

    Example of a config file:

        [DEPL]
        deployment-duration = 60

        [EPS]
        eoc = 28.0
        eoc-voltage = 28.0
        initial-voltage-noload = 28.0
        initial-internal-resistance = 1.0
"""

########################################################################
# Required packages
########################################################################

import configparser
import os

########################################################################
# Global variables
########################################################################


########################################################################
# Global methods
########################################################################


########################################################################
# Classes
########################################################################

class Cfg(object):
    """EXSIM configuration
    """

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise(FileNotFoundError(filename))
        cfg = configparser.ConfigParser()
        cfg.read(filename)
        try:
            self._deployment_duration = cfg['DEPL'].getint('deployment-duration')  # seconds (s)
            self._eoc = cfg['EPS'].getfloat('eoc')  # Volts (V)
            self._eoc_voltage = cfg['EPS'].getfloat('eoc-voltage')  # Volts (V)
            self._initial_voltage_noload = cfg['EPS'].getfloat('initial-voltage-noload')  # Volts (V)
            self._initial_internal_resistance = cfg['EPS'].getfloat('initial-internal-resistance')  # Volts (V)
        except (KeyError, ValueError) as err:
            print("Wrong configuration file:")
            raise(err)

    @property
    def depl_deployment_duration(self):
        return self._deployment_duration

    @property
    def eps_eoc(self):
        return self._eoc

    @property
    def eps_eoc_voltage(self):
        return self._eoc_voltage

    @property
    def eps_initial_voltage_noload(self):
        return self._initial_voltage_noload

    @property
    def eps_initial_internal_resistance(self):
        return self._initial_internal_resistance
