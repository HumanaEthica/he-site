from django.test import TestCase
from .models import Tag

# Create your tests here.

class ModelTests(TestCase):
    def tag_create(self):
        t = Tag("Tag name")
        
    # def create_localization_test():
    #     pass
    #     l = Localization("rua1", "cidade1", "cp1", "pais1")
    #     assert l.city == "cp1"

    # def user_create():
    #     pass

    # def user_lookup():
    #     pass

    # def user_modify():
    #     pass