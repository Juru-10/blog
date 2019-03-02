import unittest
from app.models import Pitch,User

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_wecode = User(id=12345,username = 'Wecode',password = 'potato', email = 'wecode@wecode')
        self.new_post = Post(name="ttttttttttcfcfghgh",user_id=12345,posted= 12/2/2008 )

    # def test_save_pitch(self):
    #     self.new_pitch.save_pitch()
    #     self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):

        # self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitches) == 1)
