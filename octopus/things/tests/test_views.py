from django.core.urlresolvers import reverse
from django.test import RequestFactory, TestCase
from django.views.generic import CreateView

from test_plus.test import TestCase as TestPlusTestCase

from octopus.users.models import User
from ..views import ThingsNewCreateView


class TestThingsNewCreateView(TestCase):

    def test_inheritance(self):
        view = ThingsNewCreateView
        self.assertEqual(view.__base__, CreateView)

    def test_status_code(self):
        response = self.client.get('/things/new/')
        self.assertEqual(response.status_code, 200)

    def test_view_has_template_name_attribute(self):
        view = ThingsNewCreateView
        self.assertTrue(view.template_name)

    def test_view_template_name_attribute_is_correct(self):
        view = ThingsNewCreateView
        self.assertEqual(view.template_name, 'things/new.html')

    
