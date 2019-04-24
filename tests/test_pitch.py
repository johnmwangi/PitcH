import unittest
from app.models import Pitches
from app import db

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch=Pitches(pitch="android app",author="john",title="galaxy",id=12)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitches))
    def test_init(self):
        self.assertEqual(self.new_pitch.pitch,"coding UI")
        self.assertEqual(self.new_pitch.author,"john")
        self.assertEqual(self.new_pitch.title,"React")
        self.assertEqual(self.new_pitch.id,12)
