from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='sanix',
            email='sanix@gmail.com',
            password='sanix2020'
        )
        self.assertEqual(user.username, 'sanix')
        self.assertEqual(user.email, 'sanix@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()    
        admin_user = User.objects.create_superuser(
            username='sanixadmin',
            email='sanixadmin@gmail.com',
            password='testadmin123'
        )
        self.assertEqual(admin_user.username, 'sanixadmin')
        self.assertEqual(admin_user.email, 'sanixadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)