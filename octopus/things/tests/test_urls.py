from django.core.urlresolvers import reverse, resolve
from django.test import TestCase

from ..views import ThingsNewCreateView

class TestThingsNewUrl(TestCase):
    def test_new_reverse(self):
        self.assertEqual(reverse('things:new'), '/things/new/')

    def test_new_resolve(self):
        self.assertEqual(resolve('/things/new/').view_name, 'things:new')

    def test_things_new_calls_ThingsNewCreateView_class(self):
        match = resolve('/things/new/')
        class_view_called = match.func.__dict__['view_class']
        expected_class_of_view = ThingsNewCreateView().__class__
        self.assertEqual(class_view_called, expected_class_of_view)

    def test_view_name(self):
        view_name_called = resolve('/things/new/').view_name
        view_name_expected = 'things:new'
        self.assertEqual(view_name_called, view_name_expected)

    def test_reverse_gives_correct_path(self):
        path_to_view_called = reverse('things:new')
        view_path_expected = '/things/new/'
        self.assertEqual(path_to_view_called, view_path_expected)
