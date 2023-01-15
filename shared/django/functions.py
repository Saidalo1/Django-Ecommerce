import os
from datetime import datetime
from string import digits, ascii_letters

from PIL import Image, ImageChops
from django.core.exceptions import ValidationError

from root.settings import BASE_DIR


# Delete default image of object
def delete_main_photo(model, pk):
    if model.objects.filter(id=pk).exists() and model.objects.get(id=pk).image.url:
        image_url = model.objects.get(id=pk).image.url
        os.remove(BASE_DIR + image_url)


# Delete all images of object
def delete_all_photos(model, object_pk, content_type_pk):
    if model.objects.filter(object_id=object_pk, content_type_id=content_type_pk).exists():
        images_of_cpu = model.objects.filter(object_id=object_pk, content_type_id=content_type_pk)
        for item in images_of_cpu:
            os.remove(BASE_DIR + item.image.url)
            item.delete()


# Sort image dirs of cpu by date and slug
def upload_name_cpu(instance, filename):
    date = datetime.now().strftime('%Y/%m/%d')
    return f'csp/cpu/images/{date}/default-image/{instance.id}-id/{filename}'


# Sort image dirs of video_card by date and slug
def upload_name_video_card(instance, filename):
    date = datetime.now().strftime('%Y/%m/%d')
    return f'csp/video-card/images/{date}/default-image/{instance.id}-id/{filename}'


# Find difference between old and new images
def has_difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    if image_1.size == image_2.size:
        result = ImageChops.difference(image_1, image_2)
        if result.getbbox() is None:
            # difference not found
            return False
    # difference found
    return True


# Username validation
def validate_username(username):
    match = ascii_letters + digits + '_'
    if not all([x in match for x in username]) or not (4 <= len(username) <= 150) or not username[0].isalpha():
        raise ValidationError(
            "Username can only contain letters, numbers, '_', and underscores, and must be between 4 and 150 "
            "characters long")

