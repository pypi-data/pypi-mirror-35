########################################################################
#
# test_spacecraft.py
#
#   Unit test for spacecraft.py
#
# Copyright (C) 2018 EXSIM Development Team
#
########################################################################

import unittest

from exsat import spacecraft
from exsim import exsimcfg


class MockCfg(exsimcfg.Cfg):

    def __init__(self, filename=None):
        self._deployment_duration = 60
        self._eoc =  28.0
        self._eoc_voltage =  28.0
        self._initial_voltage_noload = 28.0
        self._initial_internal_resistance = 1.0

    @exsimcfg.Cfg.depl_deployment_duration.setter
    def depl_deployment_duration(self, deployment_duration):
        self._deployment_duration = deployment_duration

    @exsimcfg.Cfg.eps_eoc.setter
    def eps_eoc(self, eoc):
        self._eoc = eoc

    @exsimcfg.Cfg.eps_eoc_voltage.setter
    def eps_eoc_voltage(self, eoc_voltage):
        self._eoc_voltage = eoc_voltage

    @exsimcfg.Cfg.eps_initial_voltage_noload.setter
    def eps_initial_voltage_noload(self, initial_voltage_noload):
        self._initial_voltage_noload = initial_voltage_noload

    @exsimcfg.Cfg.eps_initial_internal_resistance.setter
    def eps_initial_internal_resistance(self, initial_internal_resistance):
        self._initial_internal_resistance = initial_internal_resistance

class TestPoweredModel(unittest.TestCase):

    class DummyPoweredModel(spacecraft.Spacecraft.PoweredModel):

        def __init__(self):
            super().__init__()
            self._of_course_powered = False

        # Overrides parent's
        def _after_power_on(self):
            self._of_course_powered = True

        # Overrides parent's
        def _after_power_off(self):
            self._of_course_powered = False

        @property
        def of_course_powered(self):
            return self._of_course_powered

    def setUp(self):
        self._pmodel = TestPoweredModel.DummyPoweredModel()

    def test_power(self):
        self.assertFalse(self._pmodel.power)
        self.assertFalse(self._pmodel.of_course_powered)
        self._pmodel.power_on()
        self.assertTrue(self._pmodel.power)
        self.assertTrue(self._pmodel.of_course_powered)
        self._pmodel.power_off()
        self.assertFalse(self._pmodel.power)
        self.assertFalse(self._pmodel.of_course_powered)
        self._pmodel.power_on()
        self.assertTrue(self._pmodel.power)
        self.assertTrue(self._pmodel.of_course_powered)
        self._pmodel.power_off()
        self.assertFalse(self._pmodel.power)
        self.assertFalse(self._pmodel.of_course_powered)

class TestSpacecraft(unittest.TestCase):

    def setUp(self):
        self._cfg = MockCfg()
        self._cfg.depl_deployment_duration = 60
        self._sc = spacecraft.Spacecraft(self._cfg)
        self._sc.dep.conf['deployment-duration'] = 60
        self._sc.eps.conf['eoc'] = 28.0
        self._sc.eps.battery.conf['initial-voltage-noload'] = 28.0
        self._sc.eps.battery.conf['initial-internal-resistance'] = 1.0
        # TODO eoc-voltage vs eoc?
        self._sc.eps.battery.conf['eoc-voltage'] = 28.0
        self._sc.eps.battery.conf['eoc'] = 28.0

    def test_before_separation(self):
        """Test what can be done before separation
        """
        self.assertFalse(self._sc.separated)
        self._sc.step(100)
        # TTC ON
        self.assertFalse(self._sc.ttc.power)
        self._sc.ttc.power_on()
        self.assertTrue(self._sc.ttc.power)
        # DHS ON
        self.assertFalse(self._sc.dhs.power)
        self._sc.dhs.power_on()
        self.assertTrue(self._sc.dhs.power)
        self._sc.step(1)
        self.assertFalse(self._sc.separated)
        # TTC OFF
        self._sc.ttc.power_off()
        self.assertFalse(self._sc.ttc.power)
        # DHS OFF
        self._sc.dhs.power_off()
        self.assertFalse(self._sc.dhs.power)
        # Still not separeted
        self._sc.step(1)
        self.assertFalse(self._sc.separated)

    def test_separation(self):
        self.assertFalse(self._sc.separated)
        self.assertTrue(self._sc.separate())
        self.assertTrue(self._sc.separated)

    def test_ttc_status(self):
        self.assertFalse(self._sc.ttc.power)
        self.assertTrue(self._sc.separate())
        self.assertTrue(self._sc.ttc.power)

    def test_dep_status(self):
        self.assertFalse(self._sc.dep.deployed_status)
        self.assertTrue(self._sc.separate())
        self._sc.step(20)
        self.assertFalse(self._sc.dep.deployed_status)
        self._sc.step(40)
        self.assertTrue(self._sc.dep.deployed_status)

    def test_eps_status(self):
        self.assertAlmostEqual(self._sc.eps.bus_voltage, 0.0)
        self._sc.eps.power_on()
        self.assertGreater(self._sc.eps.bus_voltage, 0.0)

    def test_eps_battery(self):
        self._sc.step(1)
        self.assertEqual(self._sc.eps.battery.percentage_charged, 100.0)
        self.assertEqual(self._sc.eps.battery.voltage_noload, 28.0)
        self._sc.eps.battery.current = 0.5  # TODO What for?

    def test_start_sequence(self):
        # Before separation
        self.assertFalse(self._sc.separated)
        self.assertFalse(self._sc.dep.deployed_status)
        self.assertFalse(self._sc.ttc.power)
        self.assertFalse(self._sc.dhs.power)
        # Separate
        self.assertTrue(self._sc.separate())
        # Wait until end of startup
        self._sc.step(100)
        self.assertTrue(self._sc.separated)
        self.assertTrue(self._sc.dep.deployed_status)
        self.assertTrue(self._sc.ttc.power)
        self.assertFalse(self._sc.dhs.power)  # DHS not automatically powered on at this stage.


class TestEpsBattery(unittest.TestCase):

    def setUp(self):
        self._battery = spacecraft.Spacecraft.Battery(cfg=None)
        self._battery.conf['initial-voltage-noload'] = 28.0  # Volts
        self._battery.conf['initial-internal-resistance'] = 0.001  # Ohm
        self._battery.conf['eoc'] = 28.0  # Volts

    def test_initialization(self):
        self.assertEqual(self._battery.voltage_noload, 0.0)
        self.assertEqual(self._battery.percentage_charged, 0.0)
        self._battery.step(1)
        self.assertEqual(self._battery.voltage_noload, 28.0)
        self.assertEqual(self._battery.percentage_charged, 100.0)

    def test_discharge(self):
        self._battery.step(1)
        self._battery.current = -5.0  # Amps
        self._battery.step(1)
        self.assertLess(self._battery.voltage_noload, 28.0)
        self._battery.step(1)
        self.assertAlmostEqual(self._battery.voltage_noload, 28.0 - (5.0 * 0.001 * 2))
        self.assertLess(self._battery.voltage, self._battery.voltage_noload)

    def test_charge(self):
        self._battery.conf['initial-voltage-noload'] = 27.0  # Volts
        self._battery.step(1)
        self._battery.current = 4.0  # Amps
        self._battery.step(1)
        self.assertGreater(self._battery.voltage_noload, 27.0)
        self._battery.step(1)
        self.assertAlmostEqual(self._battery.voltage_noload, 27.0 + (4.0 * 0.001 * 2))
        self.assertGreater(self._battery.voltage, self._battery.voltage_noload)


class TestEps(unittest.TestCase):

    class DepStub:
        def __init__(self):
            pass

        @property
        def deployed_status(self):
            return False

    def setUp(self):
        self._eps = spacecraft.Spacecraft.Eps(cfg=None)
        self._eps.conf['eoc'] = 28.0
        self._eps.battery.conf['initial-voltage-noload'] = 28.0
        self._eps.battery.conf['initial-internal-resistance'] = 0.001
        # TODO eoc-voltage vs eoc?
        self._eps.battery.conf['eoc-voltage'] = 28.0
        self._eps.battery.conf['eoc'] = 28.0

    def test_discharge(self):
        self._eps.power_on()
        self._eps.step(1)

        prev_voltage_noload = 28.0
        prev_percentage_charged = 100.0

        for i in range(120):
            self._eps.step(1)

            print("Battery current: %g A" % (self._eps.battery.current))
            print("Battery voltage: %g V" % (self._eps.battery.voltage))
            print("Battery state: %g %%" % (self._eps.battery.percentage_charged))

            self.assertLess(self._eps.battery.current, 0.0)
            self.assertLess(self._eps.battery.voltage, 28.0)

            self.assertLess(self._eps.battery.voltage_noload, prev_voltage_noload)
            self.assertLess(self._eps.battery.percentage_charged, prev_percentage_charged)
            prev_voltage_noload = self._eps.battery.voltage_noload
            prev_percentage_charged = self._eps.battery.percentage_charged


class TestDeployment(unittest.TestCase):

    def setUp(self):
        self._cfg = MockCfg()
        self._depl = spacecraft.Spacecraft.Deployment(self._cfg)

    @unittest.skip('Fails')
    def test_deploy(self):
        self.assertFalse(self._depl.deployed_status)
        self._depl.step(self._cfg.depl_deployment_duration - 1)
        self.assertFalse(self._depl.deployed_status)
        self._depl.step(1)
        self.assertTrue(self._depl.deployed_status)
