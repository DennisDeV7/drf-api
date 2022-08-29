from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Dog

class DogTests(APITestCase):
  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(
      username="testuser1", password="pass"
    )
    testuser1.save()

    test_dog = Dog.objects.create(
      name="ace",
      owner=testuser1,
      description="Best dog ever.",
    )
    test_dog.save()

  def test_dogs_model(self):
    dog = Dog.objects.get(id=1)
    actual_owner = str(dog.owner)
    actual_name = str(dog.name)
    actual_description = str(dog.description)
    self.assertEqual(actual_owner, "testuser1")
    self.assertEqual(actual_name, "ace")
    self.assertEqual(
      actual_description, "Best dog ever."
    )

  def test_get_dog_list(self):
    url = reverse("dog_list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    dogs  = response.data
    self.assertEqual(len(dogs), 1)
    self.assertEqual(dogs["name"], "ace")

  def test_get_dog_by_id(self):
    url = reverse("dog_detail", args=(1, ))
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    dog = response.data
    self.assertEqual(dog["name"], "ace")

  def test_create_dog(self):
    url = reverse("dog_list")
    data = {"owner": 1, "name": "gus", "description": "Another great dog"}
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    dogs = Dog.objects.all()
    self.assertEqual(len(dogs), 2)
    self.assertEqual(Dog.objects.get(id=2).name, "gus")

  def test_update_dog(self):
    url = reverse("dog_detail", args=(1, ))
    data = {
      "owner": 1,
      "name": "ace",
      "description": "Best dog ever.",
    }
    response = self.client.put(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    dog = Dog.objects.get(id=1)
    self.assertEqual(dog.name, data["name"])
    self.assertEual(dog.owner.id, data["owner"])
    self.assertEqual(dog.description, data["description"])

  def test_delete_dog(self):
    url = reverse("dog_detail", args=(1,))
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    dogs = Dog.objects.all()
    self.assertEqual(len(dogs), 0)

