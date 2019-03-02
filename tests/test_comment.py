import unittest
from app.models import Comment,User,Post

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.user_wecode = User(id=12345,username = 'Wecode',password = 'potato', email = 'wecode@wecode')
        self.new_comment = Comment(id=12345,name='Review for movies',post_id=12345)

    # def test_save_comment(self):
    #     self.new_comment.save_comment()
    #     self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        # self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
