import os
import json
import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np
import timm
import albumentations as A
from albumentations.pytorch import ToTensorV2
from django.conf import settings

# ── Paths ────────────────────────────────────────────────────
CLASS_MAPPING_PATH = os.path.join(settings.BASE_DIR, 'models_ai', 'class_mapping.json')
MODEL_PATH = os.path.join(settings.BASE_DIR, 'models_ai', 'plant_disease_best.pth')

# ── Load class names ─────────────────────────────────────────
def load_class_names():
    with open(CLASS_MAPPING_PATH, 'r') as f:
        mapping = json.load(f)
    class_names = [mapping[str(i)] for i in range(len(mapping))]
    return class_names

CLASS_NAMES = load_class_names()

# ── Model architecture (must match training exactly) ─────────
class PlantDiseaseModel(nn.Module):
    def __init__(self, num_classes=38, pretrained=False):
        super().__init__()
        self.backbone = timm.create_model(
            'tf_efficientnetv2_s',
            pretrained=pretrained,
            num_classes=0
        )
        in_features = self.backbone.num_features
        self.classifier = nn.Sequential(
            nn.BatchNorm1d(in_features),
            nn.Linear(in_features, 512),
            nn.BatchNorm1d(512),
            nn.Linear(512, num_classes)
        )

    def forward(self, x):
        features = self.backbone(x)
        return self.classifier(features)

# ── Model cache ───────────────────────────────────────────────
_model = None
_device = None

# ── Load model ────────────────────────────────────────────────
def load_model():
    global _model, _device
    if _model is not None:
        return _model, _device

    _device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

    checkpoint = torch.load(MODEL_PATH, map_location=_device)
    num_classes = checkpoint.get('num_classes', 38)

    model = PlantDiseaseModel(num_classes=num_classes, pretrained=False)
    model.load_state_dict(checkpoint['model_state'])
    model.to(_device)
    model.eval()

    _model = model
    return _model, _device

# ── Preprocessing (must match training exactly) ───────────────
IMG_SIZE = 300
MEAN = [0.485, 0.456, 0.406]
STD  = [0.229, 0.224, 0.225]

tta_transforms = [
    A.Compose([
        A.Resize(IMG_SIZE, IMG_SIZE),
        A.Normalize(MEAN, STD),
        ToTensorV2()
    ]),
    A.Compose([
        A.Resize(IMG_SIZE, IMG_SIZE),
        A.HorizontalFlip(p=1.0),
        A.Normalize(MEAN, STD),
        ToTensorV2()
    ]),
    A.Compose([
        A.Resize(IMG_SIZE, IMG_SIZE),
        A.VerticalFlip(p=1.0),
        A.Normalize(MEAN, STD),
        ToTensorV2()
    ]),
    A.Compose([
        A.Resize(IMG_SIZE, IMG_SIZE),
        A.RandomRotate90(p=1.0),
        A.Normalize(MEAN, STD),
        ToTensorV2()
    ]),
]

# ── Predict ───────────────────────────────────────────────────
def predict_disease(image_path):
    try:
        model, device = load_model()
    except Exception as e:
        return {'error': str(e), 'success': False}

    try:
        image_np = cv2.imread(str(image_path))
        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    except Exception as e:
        return {'error': f'Cannot open image: {str(e)}', 'success': False}

    model.eval()
    logits_sum = None
    with torch.no_grad():
        for tfm in tta_transforms:
            aug = tfm(image=image_np)['image'].unsqueeze(0).to(device)
            logits = model(aug)
            logits_sum = logits if logits_sum is None else logits_sum + logits

    probs = F.softmax(logits_sum / len(tta_transforms), dim=1)[0]
    top3_probs, top3_idxs = probs.topk(3)

    top_idx = top3_idxs[0].item()
    top_conf = top3_probs[0].item() * 100
    class_name = CLASS_NAMES[top_idx]

    parts = class_name.split('___')
    plant = parts[0].replace('_', ' ').strip()
    disease_raw = parts[1].replace('_', ' ').strip().title() if len(parts) > 1 else 'Unknown'
    is_healthy = 'healthy' in disease_raw.lower()
    disease = 'Healthy' if is_healthy else disease_raw

    top3 = [
        {
            'class': CLASS_NAMES[top3_idxs[i].item()].replace('___', ' → ').replace('_', ' '),
            'confidence': round(top3_probs[i].item() * 100, 2)
        }
        for i in range(3)
    ]

    return {
        'success': True,
        'error': None,
        'class_name': class_name,
        'plant': plant,
        'disease': disease,
        'is_healthy': is_healthy,
        'confidence': round(top_conf, 2),
        'top3': top3,
    }
