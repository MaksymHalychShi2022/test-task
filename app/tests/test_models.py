import pytest
from django.contrib.auth import get_user_model
from test_task.app.models import Restaurant


@pytest.mark.django_db
def test_restaurant_creation():
    user = get_user_model().objects.create_user(username='owner', password='testpass123')
    restaurant = Restaurant.objects.create(name='My Restaurant', owner=user)
    assert restaurant.name == 'My Restaurant'
    assert restaurant.owner == user


@pytest.mark.django_db
def test_restaurant_deletion_with_user():
    user = get_user_model().objects.create_user(username='owner', password='testpass123')
    restaurant = Restaurant.objects.create(name='My Restaurant', owner=user)
    user.delete()
    assert Restaurant.objects.count() == 0
