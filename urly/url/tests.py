from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from url.models import url


class TestChirp(TestCase):

    def setUp(self):
        user = User.objects.create_user('bob', 'bob@bob.com', password='password')
        url = Url.objects.create(author=user, message='my test message')

    def test_is_recent(self):
        url = Url.objects.get(pk=1)

        self.assertTrue(url.is_recent())

    def test_get_tag_count(self):
        Url = Url.objects.get(pk=1)
        url.tag_set.create(name="Test1")
        url.tag_set.create(name="Test2")

        self.assertEqual(url.get_tag_count(), len(url.tag_set.all()))

class TestChirpList(TestCase):

    def setUp(self):
        user = User.objects.create_user('bob', 'bob@bob.com', password='password')
        url = Url.objects.create(author=user, message='my test message')

    def test_time(self):
        client = Client()
        response = client.get(reverse('list_chirps'))

        self.assertEqual(len(response.context_data['chirp_list']), 1)
        self.assertEqual(response.status_code, 200)