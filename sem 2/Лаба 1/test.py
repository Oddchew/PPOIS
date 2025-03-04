import unittest
from unittest.mock import patch, mock_open
from Computer import Computer, HardDrive, Interface
from Keyboard.Key import Key
from Keyboard.Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse


class TestComputer(unittest.TestCase):
    def setUp(self):
        self.computer = Computer(3500, 4200, 16, 1000, "SSD")
        self.monitor = Monitor(100, 60)

    def test_install_os(self):
        self.computer.install_os("Linux")
        self.assertEqual(self.computer.hardDrive.OS["OS"], "Linux")

    def test_turn(self):
        first = self.monitor.get_monitor_text
        self.computer.turn(self.monitor)
        second = self.monitor.get_monitor_text
        self.assertNotEqual(first, second)


class TestCPU(unittest.TestCase):
    def test_update_OS(self):
        self.computer = Computer(3500, 4200, 16, 1000, "SSD")
        self.computer.cpu.update_OS(self.computer.hardDrive)
        self.assertEqual(self.computer.hardDrive.OS["Version"], 1.1)


class TestHardDrive(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save(self, mock_json_dump, mock_open):
        hard_drive = HardDrive(1000, "SSD")
        hard_drive.OS["OS"] = "Windows"
        hard_drive.save()
        mock_json_dump.assert_called_with(
            {"OS": "Windows", "Version": 1.0},
            mock_open(), ensure_ascii=False, indent=4)


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = Interface()

    def test_update_up(self):
        self.interface.update("Up")
        self.assertEqual(self.interface.choosed_el, -1)

    def test_update_down(self):
        self.interface.update("Down")
        self.assertEqual(self.interface.choosed_el, 1)

    def test_change_n(self):
        self.interface.change_n(-1)
        self.assertEqual(self.interface.n, 2)


class TestKey(unittest.TestCase):
    def setUp(self):
        self.key = Key('a')

    def test_press_release(self):
        self.key.press()
        self.assertTrue(self.key.pressed)
        self.key.release()
        self.assertFalse(self.key.pressed)

    def test_get_display_label(self):
        self.assertEqual(self.key.get_display_label(), "[a]")


class TestKeyboard(unittest.TestCase):
    def setUp(self):
        self.keyboard = Keyboard()
        self.key_a = next(key for row in self.keyboard.keys
                          for key in row if key.label == 'a')

    def test_initialization(self):
        self.assertEqual(self.keyboard.keys[0][0].label, 'Esc')

    def test_press_key(self):
        self.keyboard.press_key('a')
        self.assertTrue(self.key_a.pressed)

    def test_release_key(self):
        self.keyboard.press_key('a')
        self.keyboard.release_key('a')
        self.assertFalse(self.key_a.pressed)


class TestMouse(unittest.TestCase):
    def setUp(self):
        self.mouse = Mouse()

    def test_initialization(self):
        self.assertFalse(self.mouse.status)
        self.assertEqual(self.mouse.position, (0, 0))
        self.assertFalse(self.mouse.left_button.pressed)
        self.assertFalse(self.mouse.right_button.pressed)
        self.assertFalse(self.mouse.middle_button.pressed)

    def test_move(self):
        self.mouse.move(5, 10)
        self.assertEqual(self.mouse.position, (5, 10))

    def test_click_left(self):
        self.mouse.click_left()
        self.assertTrue(self.mouse.left_button.pressed)
        self.assertFalse(self.mouse.right_button.pressed)
        self.assertFalse(self.mouse.middle_button.pressed)

    def test_click_right(self):
        self.mouse.click_right()
        self.assertTrue(self.mouse.right_button.pressed)
        self.assertFalse(self.mouse.left_button.pressed)
        self.assertFalse(self.mouse.middle_button.pressed)

    def test_click_middle(self):
        self.mouse.click_middle()
        self.assertTrue(self.mouse.middle_button.pressed)
        self.assertFalse(self.mouse.left_button.pressed)
        self.assertFalse(self.mouse.right_button.pressed)

    def test_release_all(self):
        self.mouse.click_left()
        self.mouse.click_right()
        self.mouse.click_middle()
        self.mouse.release_all()
        self.assertFalse(self.mouse.left_button.pressed)
        self.assertFalse(self.mouse.right_button.pressed)
        self.assertFalse(self.mouse.middle_button.pressed)


if __name__ == '__main__':
    unittest.main()
