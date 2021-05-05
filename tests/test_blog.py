import unittest
from app.models import Blog, User
from app import db


class BlogModelTest(unittest.TestCase):
    """
    Test class to test the behaviour of the class
    """
    def setUp(self):
        self.user_marya = User(username='Maryam', password='apple', email='marya@gmail.com')
        self.new_blog = Blog(id=1, title='sky', content='Best blog', user_id=self.user_marya.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'sky')
        self.assertEquals(self.new_blog.content, 'Best blog')
        self.assertEquals(self.new_blog.user_id, self.user_marya.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    