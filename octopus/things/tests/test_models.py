from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.test import TestCase

from octopus.users.models import User

from ..models import TimeStampedModel, Thing


class TestThing(TestCase):

    def test_model_inheritance(self):
        inheritance_expected = TimeStampedModel
        inheritance_given = Thing.__base__
        self.assertEqual(inheritance_expected, inheritance_given)

    def test_model_has_field(self):
        self.assertTrue(Thing.text)

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
