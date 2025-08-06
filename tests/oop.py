from io import StringIO
import sys
import unittest
from activities.oop import Pet 

class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet("Luna", "cat")

    def test_initial_values(self):
        self.assertEqual(self.pet.name, "Luna")
        self.assertEqual(self.pet.pet_type, "cat")
        self.assertEqual(self.pet.energy, 100)

    def test_eat_increases_energy(self):
        self.pet.eat()
        self.assertEqual(self.pet.energy, 110)

    def test_sleep_increases_energy(self):
        self.pet.sleep()
        self.assertEqual(self.pet.energy, 120)

    def test_play_decreases_energy(self):
        self.pet.play()
        self.assertEqual(self.pet.energy, 85)

    def test_show_status_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.pet.show_status()
        sys.stdout = sys.__stdout__
        self.assertIn("Luna the cat has 100 energy", captured_output.getvalue())
