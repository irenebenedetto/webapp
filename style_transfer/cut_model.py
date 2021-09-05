import torch
from torchvision import models
import pickle


cnn = models.vgg19(pretrained=True).features.to('cpu').eval()[:12]
print(cnn)
with open('./style_transfer/checkpoints/model.pkl', 'wb') as f:
    pickle.dump(cnn, f)
