import pytest
from fieldWorker.models import FieldWorker

from mixer.backend.django import mixer

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestFieldWorkerAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        print(self.client, "self.client")
    def test_worker_field_list(self):
        fieldWorker = mixer.blend(FieldWorker, first_name='test 1',last_name='last name test')
        fieldWorker2 = mixer.blend(FieldWorker, first_name='test 2',last_name='last name test 2')

        url = reverse("field_worker_list")

        response = self.client.get(url)

        print(dir(response), "response")

        assert response.json != None
        assert len(response.json()) >= 2
        assert response.status_code == 200
        
    def test_worker_create(self):
        input_data = {
            "first_name": "TestCoder",
            "last_name": "Valencia",
            "function": "3",
        }
        url = reverse('field_worker_list')
        get_list = self.client.get(url)

        response = self.client.post(url,data=input_data)

        assert response.json() != None
        assert response.status_code == 201
        assert FieldWorker.objects.count() == 1

    def test_worker_detail(self):
        fieldWorker = mixer.blend(FieldWorker, pk=1, first_name='Andrea',last_name='Valencia',function='2')
        
        #field_worker_detail_api
        url = reverse('field_worker_detail_api',kwargs={"pk":1})
        response = self.client.get(url)
        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["first_name"] == "Andrea"
        assert response.json()["last_name"] == "Valencia"
        assert response.json()["function"] == "2"
    def test_student_delete_works(self):
        # create a student

        student = mixer.blend(FieldWorker, pk=1, first_name="Geoffrey")
        assert FieldWorker.objects.count() == 1

        url = reverse("field_worker_detail_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert FieldWorker.objects.count() == 0