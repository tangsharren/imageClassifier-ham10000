# Skin Cancer Classification with ViT, ResNet50, and EfficientNetB7

Dataset used: [HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

After conducting 27 experiments to fine-tune various settings such as learning rate, scheduler, weight decay rate, dropout rate, among others, the optimal configurations were identified for the Vision Transformer (ViT) model.

These optimal settings were then applied to train both ResNet50 and EfficientNetB7 models. Following the training process, the performance of all three models was evaluated to determine the most effective one.

Upon thorough assessment, it was found that the ViT model outperformed the others. Consequently, the ViT model was selected for deployment in a Streamlit app, hosted on the Hugging Face platform.

## Model Performance Summary
|Model     |Accuracy    |Precision|Recall |F1          |
|--|--|--|--|--|
|ViT    | 0.8623  |0.8584| 0.8623 | 0.8596 
| ResNet50| 0.7864   | 0.8023    | 0.7735 | 0.7872 |
| EfficientNetB7| 0.7479   | 0.7706    | 0.7307 | 0.7494 |

Access the Streamlit App in [🤗 spaces](https://huggingface.co/spaces/sharren/skin-classification-streamlit) 
