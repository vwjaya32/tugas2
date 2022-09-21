from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class URLTests(TestCase):
    def test_html_status_code(self):
        response = self.client.get(reverse('mywatchlist:show_html'))
        
        self.assertEqual(response.status_code, 200)

    def test_xml_status_code(self):
        response = self.client.get(reverse('mywatchlist:show_xml'))
        
        self.assertEqual(response.status_code, 200)

    def test_json_status_code(self):
        response = self.client.get(reverse('mywatchlist:show_json'))
        
        self.assertEqual(response.status_code, 200)