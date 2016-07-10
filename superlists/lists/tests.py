from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePaheViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # represents the user's HTTP request
        response = home_page(request)  # just calling the view function directly
        self.assertTrue(response.content.decode('utf-8').startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', response.content.decode('utf-8'))
        self.assertTrue(response.content.decode('utf-8').endswith('</html>'))
