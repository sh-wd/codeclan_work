import unittest
from src.floor import Floor
from src.person import Person
from src.nakatomi_plaza import NakatomiPlaza

class TestNakatomiPlaza(unittest.TestCase):
    def setUp(self):
        self.john = Person("John McLain", 0)
        self.badguy1 = Person("Hans Gruber", 0)
        self.badguy2 = Person("Minion 1", 0)
        self.badguy3 = Person("Minion 2", 0)
        self.badguy4 = Person("Minion 3", 0)
        self.floor1 = Floor(1)
        self.floor2 = Floor(2)
        self.floor3 = Floor(3)
        self.nakatomi_plaza = NakatomiPlaza(self.floor1, self.floor2, self.floor3)
        
        
        

    def test_building_has_one_bad_guy_on_floor_1(self):
        self.nakatomi_plaza.add_to_floor(self.floor1, self.badguy4)
        self.assertEqual(1, len(self.nakatomi_plaza.floor1))

    @unittest.skip("Delete this line to run the test")
    def test_building_has_one_bad_guy_on_floor_2(self):
        self.nakatomi_plaza.add_to_floor(self.floor2, self.badguy3)
        self.assertEqual(1, len(self.nakatomi_plaza.floor2))

    @unittest.skip("Delete this line to run the test")
    def test_building_has_three_bad_guy_on_floor_3(self):
        self.nakatomi_plaza.add_to_floor(self.floor3, self.badguy1)
        self.nakatomi_plaza.add_to_floor(self.floor3, self.badguy2)
        self.nakatomi_plaza.add_to_floor(self.floor3, self.badguy3)
        self.assertEqual(3, len(self.nakatomi_plaza.floor3))

    @unittest.skip("Delete this line to run the test")
    def test_floor_can_be_cleared_of_bad_guys(self):
        self.nakatomi_plaza.add_to_floor(self.floor3, self.badguy1)
        self.nakatomi_plaza.add_to_floor(self.floor3, self.badguy2)
        self.nakatomi_plaza.add_to_floor(self.floor3, self.badguy3)
        self.nakatomi_plaza.smoke_em_like_it_aint_no_thang(self.john, self.floor3)
        self.assertEqual(0, len(self.nakatomi_plaza.floor3))
        self.assertEqual(3, self.john.number_of_kills)
        
        
        
