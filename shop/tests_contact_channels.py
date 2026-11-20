"""Email-only contact form: every enquiry is saved and owner-notified."""

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactChannelTests(TestCase):
    def post_contact(self, **overrides):
        data = {
            'name': 'Ada Obi',
            'email': 'ada@example.com',
            'phone_number': '08031234567',
            'message': 'Please let me know if this item is available.',
            'contact_channel': ContactMessage.CHANNEL_EMAIL,
        }
        data.update(overrides)
        return self.client.post(reverse('shop:contact'), data)

    def test_email_contact_is_saved_and_returns_to_the_contact_page(self):
        response = self.post_contact()

        self.assertRedirects(response, reverse('shop:contact'), fetch_redirect_response=False)
        message = ContactMessage.objects.get()
        self.assertEqual(message.contact_channel, ContactMessage.CHANNEL_EMAIL)

    def test_email_is_required_for_a_reply(self):
        response = self.post_contact(email='')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(ContactMessage.objects.count(), 0)
