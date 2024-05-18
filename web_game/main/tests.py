from django.test import TestCase
from django.test import TestCase
from .models import Image
from django.core.files import File
from django.conf import settings

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_game/web_game.settings")


# Create your tests here.
class GalleryModeTest(TestCase):

    def test_gallery_model_set_and_retrieve(self):
        image1 = Image(title='img1', image=File(open('gallery/test_images/test_image1.png', 'rb')))
        image1.save()
        image2 = Image(title='img2', image=File(open('gallery/test_images/test_image2.png', 'rb')))
        image2.save()

        all_images = Image.objects.all()

        self.assertEqual(len(all_images), 2)

        self.assertEqual(all_images[0].title, image1.title)

        self.assertEqual(all_images[0].image, image1.image)

        self.assertEqual(all_images[1].title, image2.title)

        self.assertEqual(all_images[1].image, image2.image)
# Create your tests here.
