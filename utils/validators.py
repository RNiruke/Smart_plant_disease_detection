from django.core.exceptions import ValidationError
import os

ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp']
MAX_SIZE_MB = 5

def validate_image_file(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(
            f'Unsupported file "{ext}". '
            f'Allowed: {", ".join(ALLOWED_EXTENSIONS)}'
        )
    if file.size > MAX_SIZE_MB * 1024 * 1024:
        raise ValidationError(
            f'Image too large. Maximum size is {MAX_SIZE_MB}MB.'
        )
