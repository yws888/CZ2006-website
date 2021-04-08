from django.test import TestCase

from django.urls import reverse

class ViewsTestCase(TestCase):
    def setUp(self):

        """Define url"""
        # self.login_url = reverse('login')
        self.leaderboard_url = reverse('leaderboard')
        self.topics_url = reverse('topics')

        self.questions_url = reverse('questions')
        self.questions_submit_url = reverse('questions_submit')

# Create your tests here.

