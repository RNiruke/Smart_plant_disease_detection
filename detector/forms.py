from django import forms
from utils.validators import validate_image_file

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        validators=[validate_image_file],
        widget=forms.FileInput(attrs={
            'accept': 'image/*',
            'class': 'form-control',
            'id': 'imageInput'
        }),
        label='Select Plant Leaf Image'
    )
