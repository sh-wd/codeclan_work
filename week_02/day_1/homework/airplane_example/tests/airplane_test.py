import unittest
from src.airplane import Airplane

class AirplaneTest(unittest.TestCase):
    def setUp(self):
        crew = ["Cpt Beefheart", "Charles Bronson", "Yul Brenner"]
        self.airplane = Airplane("Boeing 747", crew, "Miami")


    def test_airplane_has_type(self):
        self.assertEqual("Boeing 747", self.airplane.type)


    def test_airplane_has_crew(self):
        self.assertEqual(3, len(self.airplane.crew))


    def test_can_add_new_member_to_crew(self):
        new_member = "Jeff"
        self.airplane.add_member(new_member)
        self.assertEqual(4, len(self.airplane.crew))



    def test_if_it_is_the_right_day_to_stop_sniffing_glue(self):
        self.assertEqual("This is the wrong day to stop sniffing glue", self.airplane.check_glue())

    def test_check_if_crew_member_is_called_shirley_not_found(self):
        self.assertEqual("Don't call me Shirley", self.airplane.hasShirley())
        
    def test_check_if_crew_member_is_called_shirley_found(self):
        self.airplane.add_member("Shirley")
        self.assertEqual("Please, call me Shirley", self.airplane.hasShirley())

