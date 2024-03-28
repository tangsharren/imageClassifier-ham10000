# ResNet50
The ResNet50 model was trained using the TensorFlow framework and optimized settings identified from previous experiments with ViT models. 

Access with [Google Colab](https://colab.research.google.com/drive/1yasD7QSN9DN-_qeF4pmaBww8k3FRMwRV?usp=sharing) for a better rendering experience.

The best model configuration includes:
- Learning Rate: 1e-4
- Learning Rate Scheduler: Cosine with warmup
- Hair Removal: Enabled
- Class Weighting: Enabled
- Data Augmentation: Enabled
- Dropout Probability: 0.5
- Weight Decay: 1e-2
- Beta1: Default (0.9)
- Beta2: 0.99
- Epsilon: Default (1e-8)
