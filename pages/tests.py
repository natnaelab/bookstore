from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """
        test the homepage status code
        must equal to 200 (OK) status code
        """
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """test if it displays the right home template"""
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)