# Skin Cancer Classification with ViT, ResNet50, and EfficientNetB7

Dataset used: [HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

Conducted 27 experiments to determine the optimal settings (e.g., learning rate, augmentation, weight decay rate, dropout rate, etc.) for the ViT model. 

Optimal settings identified were applied to train ResNet50 and EfficientNetB7 models.

The performance of the 3 models is evaluated to identify the best model. 

The best model, ViT, is then used to be deployed into a Gradio app hosted on hugging face space.

[Gradio App](https://huggingface.co/spaces/sharren/skin-classification)
