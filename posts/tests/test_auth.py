import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_jwt_auth_flow():
# Create a user
    User.objects.create_user(username='jwtuser', password='pass1234')
    client = APIClient()


    # Obtain token
    r = client.post('/api/auth/token/', {'username': 'jwtuser', 'password': 'pass1234'}, format='json')
    assert r.status_code == 200
    token = r.json()['access']


    # Create a post using JWT
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    data = {'username': 'jwtuser', 'title': 'jwt post', 'content': 'hello'}
    r = client.post('/api/posts/', data, format='json')
    assert r.status_code == 201


    post_id = r.json()['id']
    # Update with JWT
    r = client.patch(f'/api/posts/{post_id}/', {'title': 'updated'}, format='json')
    assert r.status_code == 200
    assert r.json()['title'] == 'updated'