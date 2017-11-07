from django.core.urlresolvers import reverse
from django.test import RequestFactory, TestCase
from django.views.generic import TemplateView

from test_plus.test import TestCase as TestPlusTestCase

from octopus.users.models import User
from ..views import HomeTemplateView


class TestHomeTemplateView(TestCase):

    def test_view_inherits_from_TemplateView(self):
        view = HomeTemplateView
        self.assertEqual(view.__base__, TemplateView)

    def test_view_status_code_is_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_has_template_name_attribute(self):
        view = HomeTemplateView
        self.assertTrue(view.template_name)

    def test_view_template_name_attribute_is_correct(self):
        view = HomeTemplateView
        self.assertEqual(view.template_name, 'home/home.html')

    def test_anonimous_user_stays_on_home_view(self):
        response = self.client.get('/')
        user = response.context['user']
        self.assertTrue(user.is_anonymous)
        self.assertFalse(user.is_authenticated)
        self.assertEqual(response.context['view'].__class__, HomeTemplateView)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')


class TestHomeTemplateViewRedirection(TestPlusTestCase):

    def setUp(self):
        self.user = self.make_user()
        self.request = RequestFactory().get('/')
        self.request.user = self.user
        self.response = HomeTemplateView.as_view()(self.request)

    def test_authenticated_user_is_authenticated(self):
        view = HomeTemplateView()
        view.request = self.request
        self.assertTrue(view.request.user.is_authenticated)

    def test_view_status_code_is_302_for_authenticated_user(self):
        self.assertEqual(self.response.status_code, 302)

    def test_authenticated_user_is_redirected_to_correct_url(self):
        expected_url = reverse('things:new')
        given_url = self.response.url
        self.assertEqual(expected_url, given_url)

    def test_authenticated_user_is_redirected_to_correct_location(self):
        expected_location = reverse('things:new')
        given_location = self.response['location']
        self.assertEqual(expected_location, given_location)
