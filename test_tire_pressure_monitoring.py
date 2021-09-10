import unittest

from tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):

    # def test_do_something(self):
    #     alarm = Alarm()
    #     alarm.check()
    #     alarm.is_alarm_on

    def test_low_pressure(self):
        alarm = Alarm()
        alarm.check_value(15.4)
        self.assertTrue(alarm.is_alarm_on)

    def test_high_pressure(self):
        alarm = Alarm()
        alarm.check_value(21.1)
        self.assertTrue(alarm.is_alarm_on)

    def test_right_pressure(self):
        alarm = Alarm()
        alarm.check_value(20.4)
        self.assertFalse(alarm.is_alarm_on)


if __name__ == "__main__":
    unittest.main()
