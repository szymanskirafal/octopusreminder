from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from django.test import TestCase

from test_plus.test import TestCase as TestPlusTestCase

from octopus.users.models import User

from ..models import TimeStampedModel, Thing

class TestTimeStampedModel(TestCase):

    def test_model_has_fields(self):
        self.assertTrue(Thing.created)
        self.assertTrue(Thing.modified)

    def test_fields_classes(self):
        field = Thing._meta.get_field('created')
        class_expected = DateTimeField
        class_given = field.__class__
        self.assertEqual(class_expected, class_given)
        field = Thing._meta.get_field('modified')
        class_expected = DateTimeField
        class_given = field.__class__
        self.assertEqual(class_expected, class_given)

    def test_proper_values_of_boolean_fields(self):
        field = Thing._meta.get_field('created')
        self.assertTrue(field.auto_now_add)
        field = Thing._meta.get_field('modified')
        self.assertTrue(field.auto_now)


class TestThing(TestCase):

    def test_model_inheritance(self):
        inheritance_expected = TimeStampedModel
        inheritance_given = Thing.__base__
        self.assertEqual(inheritance_expected, inheritance_given)

    def test_model_has_fields(self):
        self.assertTrue(Thing.text)
        self.assertTrue(Thing.created_by)

    def test_field_class(self):
        field = Thing._meta.get_field('text')
        class_expected = CharField
        class_given = field.__class__
        self.assertEqual(class_expected, class_given)

    def test_field_max_length(self):
        max_length_expected = 200
        field = Thing._meta.get_field('text')
        max_length_given = field.max_length
        self.assertEqual(max_length_expected, max_length_given)

    def test_model_has_field_created_by(self):
        self.assertTrue(Thing._meta.get_field('created_by'))

    def test_created_by_class(self):
        field = Thing._meta.get_field('created_by')
        class_expected = ForeignKey
        class_given = field.__class__
        self.assertEqual(class_expected, class_given)

    def test_created_by_field_releted_to_user(self):
        field = Thing._meta.get_field('created_by')
        class_expected = User
        class_given = field.related_model
        self.assertEqual(class_expected, class_given)

    def test_str_method(self):
        user = User.objects.create(name='joe')
        thing = Thing.objects.create(text='test1', created_by=user)
        self.assertEqual(str(thing), 'test1')

    def test_ordering(self):
        self.assertEqual(Thing._meta.ordering, ['created'])

    def test_get_absolut_url(self):
        user = User.objects.create(name='joe')
        thing = Thing.objects.create(text='test1', created_by=user)
        thing = Thing.objects.get(id=1)
        self.assertEqual(thing.get_absolut_url(), '/things/detail/1/')
