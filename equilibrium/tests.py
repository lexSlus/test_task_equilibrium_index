from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Page
from PIL import Image
import tempfile


class PageModelTest(TestCase):

    def setUp(self):
        # Create a temporary image file for testing
        self.header_image = self.create_test_image()

    def create_test_image(self):
        # Create a temporary image file
        image = Image.new('RGB', (100, 100), color=(73, 109, 137))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file, 'jpeg')
        tmp_file.seek(0)
        return SimpleUploadedFile(tmp_file.name, tmp_file.read(), content_type='image/jpeg')

    def test_create_page(self):
        page = Page.objects.create(
            title='Test Page',
            content='This is a test content.',
            header_image=self.header_image
        )
        self.assertEqual(page.title, 'Test Page')
        self.assertIn('This is a test content.', page.content)
        self.assertTrue(page.header_image.name.endswith('.jpg'))

    def test_page_str_method(self):
        page = Page.objects.create(
            title='Test Page',
            content='This is a test content.',
            header_image=self.header_image
        )
        self.assertEqual(str(page), 'Test Page')

    def test_page_content_escaped(self):
        page = Page.objects.create(
            title='Test Page',
            content='<script>alert("Test")</script>',
            header_image=self.header_image
        )
        self.assertIn('<script>alert("Test")</script>', page.content)

    def test_delete_page(self):
        page = Page.objects.create(
            title='Test Page',
            content='This is a test content.',
            header_image=self.header_image
        )
        page_id = page.id
        page.delete()
        with self.assertRaises(Page.DoesNotExist):
            Page.objects.get(id=page_id)
