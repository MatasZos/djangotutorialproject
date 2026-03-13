from django.test import LiveServerTestCase
from urllib.request import urlopen


class PollLiveServerTests(LiveServerTestCase):
    def test_index_page_loads_from_live_server(self):
        response = urlopen(f"{self.live_server_url}/polls/")
        self.assertEqual(response.status, 200)