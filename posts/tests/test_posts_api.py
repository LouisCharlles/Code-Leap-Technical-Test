import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from posts.models import Post


@pytest.mark.django_db
@pytest.mark.django_db
def test_post_crud_and_like_comment_cycle():
    client = APIClient()
    data = {'username': 'luis', 'title': 'hi', 'content': 'hello'}
    r = client.post('/api/posts/', data, format='json')
    assert r.status_code == 201
    post_id = r.json()['id']


    # like
    r = client.post(f'/api/posts/{post_id}/like/')
    assert r.status_code == 200
    assert r.json()['likes_count'] == 1


    # comment create
    cdata = {'username': 'luis', 'content': 'nice post'}
    r = client.post(f'/api/posts/{post_id}/comments/', cdata, format='json')
    assert r.status_code == 201
    comment_id = r.json()['id']


    # comment list
    r = client.get(f'/api/posts/{post_id}/comments/')
    assert r.status_code == 200
    assert r.json()['results'][0]['id'] == comment_id


    # patch post with wrong user
    r = client.patch(f'/api/posts/{post_id}/', {'title': 'new'}, format='json', HTTP_X_USERNAME='other')
    assert r.status_code == 403


    # patch post with owner
    r = client.patch(f'/api/posts/{post_id}/', {'title': 'new'}, format='json', HTTP_X_USERNAME='luis')
    assert r.status_code == 200
    assert r.json()['title'] == 'new'


    # delete comment as wrong user
    r = client.delete(f'/api/posts/{post_id}/comments/{comment_id}/', HTTP_X_USERNAME='other')
    assert r.status_code == 403


    # delete comment as owner
    r = client.delete(f'/api/posts/{post_id}/comments/{comment_id}/', HTTP_X_USERNAME='luis')
    assert r.status_code == 204