import unittest

import FreeSimpleGUI as sg


class MyTestCase(unittest.TestCase):
    def test_open_and_close_global_psg_settings(self):
        sg.popup_ok("In the settings window (next window) press OK button to continue the test.")
        ok_pressed = sg.main_global_pysimplegui_settings()
        self.assertEqual(ok_pressed, True)


if __name__ == '__main__':
    unittest.main()
