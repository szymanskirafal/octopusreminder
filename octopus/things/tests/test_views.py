from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
from django.test import RequestFactory, TestCase
from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from test_plus.test import TestCase as TestPlusTestCase

from octopus.users.models import User
from octopus.things.models import Thing

from ..views import *


class TestThingsNewCreateView(TestCase):

    def test_inheritance(self):
        view = ThingsNewCreateView
        self.assertEqual(view.__base__, LoginRequiredMixin)
        self.assertTrue(issubclass(view, generic.CreateView))

    def test_view_has_template_name_attribute(self):
        view = ThingsNewCreateView
        self.assertTrue(view.template_name)

    def test_view_template_name(self):
        view = ThingsNewCreateView
        self.assertEqual(view.template_name, 'things/new.html')

    def test_view_fields_attribute(self):
        view = ThingsNewCreateView
        self.assertTrue(view.fields)

    def test_view_fields_value(self):
        view = ThingsNewCreateView
        self.assertEqual(view.fields, ['text'])

    def test_view_fields_attribute(self):
        view = ThingsNewCreateView
        self.assertTrue(view.success_url)

    def test_view_fields_value(self):
        view = ThingsNewCreateView
        self.assertEqual(view.success_url, reverse('things:saved'))

    def test_status_coded(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
        response = self.client.get('/things/new/')
        self.assertTrue(response.status_code, 200)

    def test_user_create_new_thing(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
        response = self.client.post('/things/new/', {'text':'test7'})
        print('resp: ', response)
        print('resp dict: ', response.__dict__)



class TestThingsNewCreateViewRediretsNotAuthUsers(TestPlusTestCase):

    def setUp(self):
        self.request = RequestFactory().get('/things/new/')
        self.request.user = AnonymousUser()
        self.response = ThingsNewCreateView.as_view()(self.request)

    def test_view_redirects_not_authenticated_users(self):
        self.assertTrue(self.response.status_code, 302)

    def test_not_authenticated_user_is_redirected_to_correct_url(self):
        expected_url = reverse('account_login') + '?next=/things/new/'
        given_url = self.response.url
        self.assertEqual(expected_url, given_url)

    def test_not_authenticated_user_is_redirected_to_correct_location(self):
        expected_location = reverse('account_login') + '?next=/things/new/'
        given_location = self.response['location']
        self.assertEqual(expected_location, given_location)



class TestThingsListViewAttributes(TestCase):

    def test_view_inheritance(self):
        view = ThingsListView
        self.assertEqual(view.__base__, LoginRequiredMixin)
        self.assertTrue(issubclass(view, generic.ListView))

    def test_view_has_model_attribute(self):
        view = ThingsListView
        self.assertTrue(view.model)

    def test_view_model(self):
        model_given = ThingsListView.model
        model_expected = Thing
        self.assertEqual(model_expected, model_given)

    def test_view_has_template_name_attribute(self):
        view = ThingsListView
        self.assertTrue(view.template_name)

    def test_view_template_name(self):
        view = ThingsListView
        self.assertEqual(view.template_name, 'things/list.html')

    def test_view_has_context_object_name_attribute(self):
        self.assertTrue(ThingsListView.context_object_name)

    def test_context_object_name(self):
        context_object_name_expected = 'things'
        context_object_name_given = ThingsListView.context_object_name
        self.assertEqual(context_object_name_expected, context_object_name_given)


class TestListViewRediretsNotAuthUsers(TestPlusTestCase):

    def setUp(self):
        self.request = RequestFactory().get('/things/list/')
        self.request.user = AnonymousUser()
        self.response = ThingsListView.as_view()(self.request)

    def test_view_redirects_not_authenticated_users(self):
        self.assertTrue(self.response.status_code, 302)

    def test_not_authenticated_user_is_redirected_to_correct_url(self):
        expected_url = reverse('account_login') + '?next=/things/list/'
        given_url = self.response.url
        self.assertEqual(expected_url, given_url)

    def test_not_authenticated_user_is_redirected_to_correct_location(self):
        expected_location = reverse('account_login') + '?next=/things/list/'
        given_location = self.response['location']
        self.assertEqual(expected_location, given_location)


class TestThingsListViewQuery(TestPlusTestCase):

    def setUp(self):
        self.user = self.make_user()
        self.user2 = self.make_user(username='joe')
        self.user3 = self.make_user(username='ryan')
        self.request = RequestFactory().get('/things/list/')
        self.request.user = self.user
        self.thing1 = Thing.objects.create(text='test1', created_by=self.user)
        self.thing2 = Thing.objects.create(text='test2', created_by=self.user)
        self.thing3 = Thing.objects.create(text='test3', created_by=self.user2)
        self.thing4 = Thing.objects.create(text='test1', created_by=self.user2)
        self.response = ThingsListView.as_view()(self.request)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_number_of_elements_in_queryset(self):
        view = ThingsListView()
        view.request = self.request
        testuser = self.request.user
        number_expected = len(Thing.objects.all().filter(created_by = testuser))
        number_given = len(self.response.context_data['object_list'])
        self.assertEqual(number_expected, number_given)

    def test_queryset_returned_by_view_is_created_by_current_user(self):
        view = ThingsListView()
        view.request = self.request
        testuser = self.request.user
        queryset_expected = Thing.objects.all().filter(created_by = testuser)
        queryset_returned = self.response.context_data['object_list']
        self.assertEqual(list(queryset_returned), list(queryset_expected))
        self.assertEqual(len(queryset_returned), len(queryset_expected))

    def test_query_does_not_contains_any_thing_created_by_any_other_user(self):
        view = ThingsListView()
        view.request = self.request
        testuser = self.request.user

        queryset_returned = self.response.context_data['object_list']
        queryset_expected = Thing.objects.all().filter(created_by = testuser)
        queryset_not_wanted = Thing.objects.all().exclude(created_by = testuser)

        list_of_elements_in_queryset_returned = list(queryset_returned)
        list_of_elements_that_should_be_in_queryset = list(queryset_expected)
        list_of_elements_that_should_not_be_in_queryset = list(queryset_not_wanted)

        self.assertEqual(list_of_elements_in_queryset_returned, list_of_elements_that_should_be_in_queryset)
        self.assertNotIn(list_of_elements_that_should_not_be_in_queryset, list_of_elements_in_queryset_returned)

    def test_expected_things_are_in_template(self):
        response = self.response
        text = 'test1'
        self.assertContains(response, text)

    def test_not_wanted_things_are_not__in_template(self):
        response = self.response
        text = 'i do not want this text in template'
        self.assertNotContains(response, text)


class TestThingsDetailView(TestCase):

    def test_view_inheritance(self):
        view = ThingsDetailView
        self.assertEqual(view.__base__, LoginRequiredMixin)
        self.assertTrue(issubclass(view, generic.DetailView))

    def test_view_has_model_attribute(self):
        view = ThingsDetailView
        self.assertTrue(view.model)

    def test_view_model(self):
        model_given = ThingsDetailView.model
        model_expected = Thing
        self.assertEqual(model_expected, model_given)

    def test_view_has_template_name_attribute(self):
        view = ThingsDetailView
        self.assertTrue(view.template_name)

    def test_view_template_name(self):
        view = ThingsDetailView
        self.assertEqual(view.template_name, 'things/detail.html')

    def test_view_has_context_object_name_attribute(self):
        self.assertTrue(ThingsListView.context_object_name)

    def test_context_object_name(self):
        context_object_name_expected = 'thing'
        context_object_name_given = ThingsDetailView.context_object_name
        self.assertEqual(context_object_name_expected, context_object_name_given)


class TestDetailViewForNotAuthenticatedUsers(TestPlusTestCase):

    def setUp(self):
        self.request = RequestFactory().get('/things/detail/1/')
        self.request.user = AnonymousUser()
        self.response = ThingsDetailView.as_view()(self.request, pk=1)

    def test_view_redirects_not_authenticated_users(self):
        self.assertTrue(self.response.status_code, 302)

    def test_not_authenticated_user_is_redirected_to_correct_url(self):
        expected_url = reverse('account_login') + '?next=/things/detail/1/'
        given_url = self.response.url
        self.assertEqual(expected_url, given_url)

    def test_not_authenticated_user_is_redirected_to_correct_location(self):
        expected_location = reverse('account_login') + '?next=/things/detail/1/'
        given_location = self.response['location']
        self.assertEqual(expected_location, given_location)


class TestThingsDetailViewForAuthenticatedUsers(TestPlusTestCase):

    def setUp(self):
        self.user = self.make_user()
        self.request = RequestFactory().get('/things/detail/1/')
        self.request.user = self.user

    def test_status_code(self):
        thing = Thing.objects.create(text='test1', created_by=self.user)
        response = ThingsDetailView.as_view()(self.request, pk=3)
        self.assertEqual(response.status_code, 200)

    def test_zobject(self):
        thing = Thing.objects.create(text='test1', created_by=self.user)
        response = ThingsDetailView.as_view()(self.request, pk=4)
        obj = response.context_data['object']
        self.assertEqual(obj.text, 'test1')
        self.assertEqual(obj.pk, 4)
        self.assertEqual(obj.created_by.username, 'testuser')


class TestThingsListViewQuery(TestPlusTestCase):

    def setUp(self):
        self.user = self.make_user()
        self.user2 = self.make_user(username='joe')
        self.user3 = self.make_user(username='ryan')
        self.request = RequestFactory().get('/things/detail/1/')
        self.request.user = self.user
        self.thing1 = Thing.objects.create(text='test1', created_by=self.user)
        self.thing2 = Thing.objects.create(text='test2', created_by=self.user)
        self.thing3 = Thing.objects.create(text='test3', created_by=self.user2)
        self.thing4 = Thing.objects.create(text='test1', created_by=self.user2)
        self.response = ThingsListView.as_view()(self.request)

    def test_expected_things_are_in_template(self):
        response = self.response
        text = 'test1'
        self.assertContains(response, text)

    def test_not_wanted_things_are_not__in_template(self):
        response = self.response
        text = 'i do not want this text in template'
        self.assertNotContains(response, text)
