from django.core.urlresolvers import reverse, resolve
from django.test import TestCase

from ..views import *


class TestThingsNewUrl(TestCase):
    def test_url_reverse(self):
        self.assertEqual(reverse('things:new'), '/things/new/')

    def test_url_resolve(self):
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

class TestThingsListUrl(TestCase):

    def test_url_resolve(self):
        self.assertEqual(resolve('/things/list/').view_name, 'things:list')

    def test_url_reverse(self):
        self.assertEqual(reverse('things:list'), '/things/list/')

    def test_url_calls_proper_class_of_view(self):
        match = resolve('/things/list/')
        class_view_called = match.func.__dict__['view_class']
        expected_class_of_view = ThingsListView().__class__
        self.assertEqual(class_view_called, expected_class_of_view)

    def test_url_calls_proper_name_of_view(self):
        view_name_called = resolve('/things/list/').view_name
        view_name_expected = 'things:list'
        self.assertEqual(view_name_called, view_name_expected)

class TestThingsDetailUrl(TestCase):

    def test_url_resolve(self):
        self.assertEqual(resolve('/things/detail/1/').view_name, 'things:detail')

    def test_url_reverse(self):
        self.assertEqual(reverse('things:detail', args=[1]), '/things/detail/1/')

    def test_url_calls_proper_class_of_view(self):
        match = resolve('/things/detail/1/')
        class_view_called = match.func.__dict__['view_class']
        expected_class_of_view = ThingsDetailView().__class__
        self.assertEqual(class_view_called, expected_class_of_view)

    def test_url_calls_proper_name_of_view(self):
        view_name_called = resolve('/things/detail/1/').view_name
        view_name_expected = 'things:detail'
        self.assertEqual(view_name_called, view_name_expected)

class TestThingsEditUrl(TestCase):

    def test_url_resolve(self):
        self.assertEqual(resolve('/things/edit/1/').view_name, 'things:edit')

    def test_url_reverse(self):
        self.assertEqual(reverse('things:edit', args=[1]), '/things/edit/1/')

    def test_url_calls_proper_class_of_view(self):
        match = resolve('/things/edit/1/')
        class_view_called = match.func.__dict__['view_class']
        expected_class_of_view = ThingsEditUpdateView().__class__
        self.assertEqual(class_view_called, expected_class_of_view)

    def test_url_calls_proper_name_of_view(self):
        view_name_called = resolve('/things/edit/1/').view_name
        view_name_expected = 'things:edit'
        self.assertEqual(view_name_called, view_name_expected)

class TestThingsThingSavedUrl(TestCase):

    def test_url_resolve(self):
        self.assertEqual(resolve('/things/thing-saved/').view_name, 'things:saved')

    def test_url_reverse(self):
        self.assertEqual(reverse('things:saved'), '/things/thing-saved/')

    def test_url_calls_proper_class_of_view(self):
        match = resolve('/things/thing-saved/')
        class_view_called = match.func.__dict__['view_class']
        expected_class_of_view = ThingsThingSavedTemplateView().__class__
        self.assertEqual(class_view_called, expected_class_of_view)

    def test_url_calls_proper_name_of_view(self):
        view_name_called = resolve('/things/thing-saved/').view_name
        view_name_expected = 'things:saved'
        self.assertEqual(view_name_called, view_name_expected)
