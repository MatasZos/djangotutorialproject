from django.test import SimpleTestCase
from django.urls import reverse


class UrlTests(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("polls:index")
        self.assertURLEqual(url, "/polls/")