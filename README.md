# Skin Cancer Classification with ViT, ResNet50, and EfficientNetB7

Dataset used: [HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

After conducting 27 experiments to fine-tune various settings such as learning rate, scheduler, weight decay rate, dropout rate, among others, the optimal configurations were identified for the Vision Transformer (ViT) model.

These optimal settings were then applied to train both ResNet50 and EfficientNetB7 models. Following the training process, the performance of all three models was rigorously evaluated to determine the most effective one.

Upon thorough assessment, it was found that the ViT model outperformed the others. Consequently, the ViT model was selected for deployment in a Gradio app, hosted on the Hugging Face platform.

Access the Gradio App in 
- [🤗 spaces](https://huggingface.co/spaces/sharren/skin-classification) or
- [Google Colab](https://colab.research.google.com/drive/1xRMiu9KqZvdnwdIZ_NYszRbgAt4I7-as?usp=sharing) or
- Download and run [Skin Cancer Classifier Gradio App.ipynb](https://github.com/tangsharren/imageClassifier-ham10000/blob/main/Skin%20Cancer%20Classifier%20Gradio%20App.ipynb) in this repo 

