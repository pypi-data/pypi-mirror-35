########################################################################
#
# spacecraft.py
#
#   EXSIM satellite model.
#
# Copyright (C) 2018 EXSIM Development Team
#
########################################################################

from abc import abstractmethod
from simcore import vehicle, model
from exsim import exsimcfg

import random

########################################################################
# class Spacecraft
#
#   Satellite model
#
########################################################################


class Spacecraft(vehicle.Vehicle):
    """Satellite model.

    Units:
        Voltage: V (Volts)
        Current: A (Ampers)
        Time: s (seconds)
    """

    class BaseModel(model.Model):
        """Base for all spacecraft models.
        """
        def __init__(self, cfg=None):
            super().__init__()
            self._simclock = 0
            self._cfg = cfg
            self._conf = dict()
            self._submodels = list()

        def step(self, delta_simclock):
            for m in self._submodels:
                m.step(delta_simclock)
            self._simclock += delta_simclock

        @property
        def conf(self):
            return self._conf

        @property
        def submodels(self):
            return self._submodels

    class PoweredModel(BaseModel):
        """Base for all powered spacecraft models.
        """
        def __init__(self, cfg=None):
            super().__init__(cfg)
            self._power = False

        def power_on(self):
            if not self._power:
                self._power = True
                self._after_power_on()

        def power_off(self):
            if self._power:
                self._power = False
                self._after_power_off()

        def _after_power_on(self):
            pass

        def _after_power_off(self):
            pass

        # TODO Since this is a boolean, what about renaming it as
        # powered_on or just powered?
        @property
        def power(self):
            return self._power

    class Ttc(PoweredModel):
        def __init__(self, cfg=None):
            super().__init__(cfg)

    class Deployment(BaseModel):
        def __init__(self, cfg=None):
            super().__init__(cfg)
            self._deployed_status = False
            self._deployment_start_simclock = -1

        def deploy(self):
            self._deployment_start_simclock = self._simclock

        @property
        def deployed_status(self):
            return self._deployed_status

        def step(self, delta_simclock):
            super().step(delta_simclock)
            self._update_deployment()

        def _update_deployment(self):
            if not self._deployed_status:
                d = self._simclock - self._deployment_start_simclock
                if d >= self._cfg.depl_deployment_duration:
                    self._deployed_status = True

    class Battery(BaseModel):
        def __init__(self, cfg=None):
            super().__init__(cfg)
            # TODO Define _voltage_noload
            self._voltage_noload = 0.0
            self._internal_resistance = 0.0
            self._percentage_charged = 0.0
            self._current = 0.0
            self._initialized = False

        def step(self, delta_simclock):
            super().step(delta_simclock)

            if not self._initialized:
                self._initialize()
                self._initialized = True

            if self._current != 0.0:
                v_delta = self._current * self._internal_resistance * delta_simclock
                self._voltage_noload += v_delta

            self._update_percentage_charged()

        def _initialize(self):
            self._voltage_noload = self.conf['initial-voltage-noload']
            self._internal_resistance = self.conf['initial-internal-resistance']
            self._update_percentage_charged()

        def _update_percentage_charged(self):
            self._percentage_charged = (self._voltage_noload / self.conf['eoc']) * 100.0

        @property
        def voltage_noload(self):
            return self._voltage_noload

        @property
        def voltage(self):
            v_delta = self._current * self._internal_resistance
            return self._voltage_noload + v_delta

        @property
        def internal_resistance(self):
            return self._internal_resistance

        @property
        def percentage_charged(self):
            return self._percentage_charged

        @property
        def current(self):
            return self._current

        @current.setter
        def current(self, val):
            self._current = val

    class Eps(BaseModel):

        def __init__(self, cfg=None):
            super().__init__(cfg)
            self._bus_current = 0.0
            self._bus_voltage = 0.0
            # TODO Define eoc - Guess end-of-charge voltage
            self.conf['eoc'] = 28.0
            self.battery = Spacecraft.Battery(cfg)
            self.submodels.append(self.battery)

        @property
        def bus_current(self):
            return self._bus_current

        @property
        def bus_voltage(self):
            return self._bus_voltage

        def power_on(self):
            self._bus_voltage = self.conf['eoc']

        def step(self, delta_simclock):
            super().step(delta_simclock)

            self._update_current()

        def _update_current(self):
            # TODO Why negative current?
            curr = -5 * random.random()
            self._bus_current = curr
            self.battery.current = curr

    class PacketStore(BaseModel):
        def __init__(self, cfg=None):
            super().__init__(cfg)
            self._id = 0

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, val):
            self._id = val

    class Dhs(PoweredModel):
        def __init__(self, cfg=None):
            super().__init__(cfg)

            self._ps = dict()
            for i in range(5):
                ps = Spacecraft.PacketStore()
                ps.id = i
                self._ps[i] = ps

    def __init__(self, cfg=None):
        super().__init__()
        self._separated = False
        self.ttc = Spacecraft.Ttc()
        self.dep = Spacecraft.Deployment(cfg)
        self.eps = Spacecraft.Eps(cfg)
        self.dhs = Spacecraft.Dhs()
        self._submodels = [
            self.ttc,
            self.dep,
            self.eps,
            self.dhs]

    def step(self, delta_simclock):
        for m in self._submodels:
            m.step(delta_simclock)

    def separate(self):
        if not self._separated:
            self._separated = True
            self.ttc.power_on()
            self.dep.deploy()
            return True
        else:
            return False

    @property
    def separated(self):
        return self._separated
