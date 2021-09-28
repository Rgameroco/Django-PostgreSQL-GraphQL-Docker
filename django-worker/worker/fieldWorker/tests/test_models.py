from django.test import TestCase
import pytest
from fieldWorker.models import FieldWorker
# Create your tests here.
from mixer.backend.django import mixer
from hypothesis import strategies as st, given
pytestmark = pytest.mark.django_db


class TestStudentModel(TestCase):

    def test_worker_field_can_be_created(self):
        workerField = mixer.blend(FieldWorker, first_name='test 1',last_name='last name test')
        result = FieldWorker.objects.last()
        assert result.first_name == 'test 1'
        assert result.last_name == 'last name test'
        assert result.function == '4'
