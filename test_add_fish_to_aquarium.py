import unittest
import add_fish_to_aquarium from add_fish

class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["rabbit"]}
        self.assertEqual(actual, expected)
