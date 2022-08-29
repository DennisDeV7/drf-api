from django.urls import path
from .views import DogList, DogDetail

urlpatterns = [
  path("", DogList.as_view(), name="dog_list"),
  path("<int:pk>/", DogDetail.as_view(), name="dog_detail"),
]