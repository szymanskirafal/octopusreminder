from django.core.urlresolvers import reverse, resolve
from django.test import TestCase

from octopus.home.views import HomeTemplateView

class TestHomeURLs(TestCase):

    def test_slash_calls_HomeTemplateView_class(self):
        match = resolve('/')
        class_view_called = match.func.__dict__['view_class']
        expected_class_of_view = HomeTemplateView().__class__
        self.assertEqual(class_view_called, expected_class_of_view)

    def test_slash_calls_view_named_home(self):
        view_name_called = resolve('/').view_name
        view_name_expected = 'home'
        self.assertEqual(view_name_called, view_name_expected)

    def test_reverse_view_named_home_gives_correct_path(self):
        path_to_view_called = reverse('home')
        view_path_expected = '/'
        self.assertEqual(path_to_view_called, view_path_expected)
