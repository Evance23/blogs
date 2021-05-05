import unittest
from app.models import Comment
from app import db

class CommentModelTest(unittest.TestCase):
    """
    Test Class to test the comment class
    """
    def setUp(self):
        
        self.new_comment = Comment(comment = 'Amazing')
        
    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Amazing') 
        
    