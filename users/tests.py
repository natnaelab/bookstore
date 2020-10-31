from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='nati',
            email='nati@email.com',
            password='pass1234'
        )
        self.assertEqual(user.username, 'nati')
        self.assertEqual(user.email, 'nati@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='natisu',
            email='natisu@email.com',
            password='pass1234'
        )
        self.assertEqual(admin_user.username, 'natisu')
        self.assertEqual(admin_user.email, 'natisu@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
