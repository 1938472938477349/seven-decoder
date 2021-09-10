import random


class Sensor(object):
    # The reading of the pressure value from the sensor is simulated in this implementation.
    # Because the focus of the exercise is on the other class.

    _OFFSET = 16

    def pop_next_pressure_psi_value(self):
        pressure_telemetry_value = self.sample_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_pressure():
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value


class Alarm():

    def __init__(self):
        self._low_pressure_threshold = 17.0
        self._high_pressure_threshold = 21.0
        self._sensor = Sensor()
        self._is_alarm_on = False

    def check(self):
        self.check_value(self._sensor.pop_next_pressure_psi_value())

    def check_value(self, value):
        if value < self._low_pressure_threshold or self._high_pressure_threshold < value:
            self._is_alarm_on = True
        else:
            self._is_alarm_on = False

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
