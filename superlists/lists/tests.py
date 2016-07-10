from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest
from lists.views import home_page

class HomePaheViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # represents the user's HTTP request
        response = home_page(request)  # just calling the view function directly
        
        # In the code above we're testing constants, which we should not do, so let's fix this
        # and test behaviour (expected content, and not constants).
        # Note, we did not remove the tests above, we only do that after we make sure that the tests
        # continue passing.
        expected_content = render_to_string('home.html')
        self.assertEqual(response.content.decode('utf-8'), expected_content)

