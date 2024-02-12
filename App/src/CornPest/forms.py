from django import forms


class ImageForm(forms.Form):
    image_file = forms.ImageField(
        label="Veuillez Choisir Une Image",
        help_text="Format accepte : png, jpg, jpeg"
    )
