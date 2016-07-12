from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item

class HomePaheViewTest(TestCase):

    # NOTE on csrf: to make the unit test work with csrf tokens, we need to make sure that we're always using the same HttpRequest
    # object, since for a different HttpRequest object, a different value of csrf token will be generated, so the assertEqual() tests
    # will fail.

    def test_home_page_uses_home_template(self):
        request = HttpRequest()  # represents the user's HTTP request
        response = home_page(request)  # just calling the view function directly
        
        # In the code above we're testing constants, which we should not do, so let's fix this
        # and test behaviour (expected content, and not constants).
        # Note, we did not remove the tests above, we only do that after we make sure that the tests
        # continue passing.
        expected_content = render_to_string('home.html', request=request)  # request=request to make sure the same csrf token is generated
        self.assertEqual(response.content.decode('utf-8'), expected_content)

    def test_home_page_can_store_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'new item'

        # request=request to make sure the same csrf token is generated
        expected_content = render_to_string('home.html', {'new_item_text': request.POST['item_text']}, request=request)

        response = home_page(request)

        self.assertEqual(expected_content, response.content.decode('utf8'))


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The 1st list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The 2nd list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The 1st list item')
        self.assertEqual(second_saved_item.text, 'The 2nd list item')
