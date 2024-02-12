from .models import UploadImage
from .forms import ImageForm

from django.shortcuts import render

from pathlib import Path
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_DIR = list(Path(__file__).resolve().parents)[-5] / "models" / "2"


MODEL = tf.keras.models.load_model(MODEL_DIR)
CLASS_NAMES = ['chenille', 'leaf beetle', 'grasshoper', 'healthy', 'puceron']


def home(request):
    context = {
        "image_url": "/media/images/default.png",
        "home_page": True
    }
    return render(request, 'CornPest/index.html', context)


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = UploadImage(image_file=request.FILES['image_file'])
            new_image.save()
            image_url = new_image.image_file.url
            class_name, confidence = process_image(f"/home/jiem/Projects/projet_datascience/App/CornPest/{image_url}")
            context = {
                "image_url": image_url,
                "class_name": class_name,
                "confidence": confidence
            }
            return render(request, "CornPest/index.html", context=context)
    else:
        form = ImageForm()

    context = {
        "form": form
    }
    
    return render(request, "CornPest/upload.html", context=context)



def to_jpg(image_path):
    image = Image.open(image_path)
    jpg_image_path = f"{str(image_path).split('.')[0]}.jpg"
    image = image.convert("RGB")
    image.save(jpg_image_path)
    print(jpg_image_path)
    return jpg_image_path


def process_image(image_path):
    image_path = Path(image_path)
    print(image_path.suffix)
    print(3*"\n")
    if image_path.suffix in [".png", ".jpeg"]:
        print("convertie")
        image_path = to_jpg(image_path)

    image = Image.open(image_path)
    image = image.resize((128, 128))
    image_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100*(np.max(predictions[0])), 2)
    

    return predicted_class, confidence
