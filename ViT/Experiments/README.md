
# ViT Hyperparameter Tuning Experiments


Experiment Plan:
1. **Initial Learning Rate Experiment:**
- Train ViT model separately with initial learning rates of **0.0001, 0.001, and 0.01** using the original dataset.
- Utilize a Cosine learning rate scheduler during training.
- Plot validation performance against learning rates to identify the optimal initial learning rate.

2. **Scheduler Comparison Experiment:** 
- Train models using different schedulers **(Cosine with Warmup, Cosine with Restarts, StepLR, ReduceLRonPlateau)** with the optimal initial learning rate
- Compare validation performance by plotting against learning rates for each scheduler.

3. **Data Preprocessing Experiments:**
- Train models with both the original dataset and a cleaned dataset (**hair noises removed**).
- Evaluate and compare performance between the two datasets.

4. **Data Augmentation Experiment:**
- Apply data augmentation techniques to the optimal dataset.
- Train models with augmented data and compare performance with models trained without augmentation.

5. **Class Weighting Experiment:**
- Apply balanced class weights to the optimal dataset.
- Train models with class weighting and compare performance with models without weighting.

6. **Dropout Probability Experiment** :
- Train models separately with different dropout probabilities (**0.2, 0.3, 0.4, 0.5**).
- Evaluate models and identify the optimal dropout rate.

7. **Weight Decay Experiment**:
- Train models separately with different weight decay values (**1e-2, 1e-3, 1e-4, 1e-5**).
- Evaluate models and identify the optimal weight decay value.

8. **Optimizer Parameters Experiment**:
- Train models separately with different values for **beta1 (0.85, 0.88, 0.95)** and **beta2 (0.99, 0.995, 0.9995)**.
- Evaluate models and identify the optimal values for beta1 and beta2.

9. **Epsilon Experiment**:
- Train models separately with different epsilon values (**1e-9, 5e-9, 1e-7**).
- Evaluate models and identify the optimal epsilon value.

***Early stopping** is employed: Stop training if there is no improvement in the evaluation metric (in this case, a decrease in validation loss) for 10 evaluation steps.*

## Folder structure
```bash
1. LR & Scheduler Experiment/
    - 1.1 ExptLR/
        - 0.0001_ExptLR.ipynb
        - 0.001_ExptLR.ipynb
        - 0.01_ExptLR.ipynb

    - 1.2 ExptScheduler/
        - Cosine Warmup_ExptLR.ipynb
        - Cosine Restarts_ExptLR.ipynb
        - Reduce on Plateau_ExptLR.ipynb
        - Step_ExptLR.ipynb

2. Removed Hair/
    - Removed Hair_ExptDS.ipynb

3. Imbalance/
    - Augmentation_ExptImb.ipynb
    - Class Weight_ExptImb.ipynb

4. Overfitting/ 
    - 4.1 Dropout/
        - 0.0001_ExptLR.ipynb
        - 0.001_ExptLR.ipynb
        - 0.01_ExptLR.ipynb
    
    - 4.2 AdamW/
        - 4.2.1 Weight Decay/
            - 1e-2 Wt Decay_ExptOverfit.ipynb
	        - 1e-3 Wt Decay_ExptOverfit.ipynb
	        - 1e-4 Wt Decay_ExptOverfit.ipynb
	        - 1e-5 Wt Decay_ExptOverfit.ipynb

        - 4.2.2 Beta1/
            - 0.85 beta1_ExptOverfit.ipynb
	        - 0.88 beta1_ExptOverfit.ipynb
	        - 0.95 beta1_ExptOverfit.ipynb
	        
        - 4.2.3 Beta2/
            - 0.99 beta2_ExptOverfit.ipynb
	        - 0.995 beta2_ExptOverfit.ipynb
	        - 0.9995 beta2_ExptOverfit.ipynb
	        
        - 4.2.4 Epsilon/
            - 1e-9 epsilon_ExptOverfit.ipynb
	        - 5e-9 epsilon_ExptOverfit.ipynb
	        - 1e-7 epsilon_ExptOverfit.ipynb
```

## Hugging Face Model Hub
Access the model card and insightful training metrics for each trained model on the Hugging Face Hub by clicking the hyperlink provided below:

Learning Rate
- [0.0001](https://huggingface.co/sharren/vit-lr-0.0001/tree/main)
- [0.001](https://huggingface.co/sharren/vit-lr-0.001/tree/main)
- [0.01](https://huggingface.co/sharren/vit-lr-0.01/tree/main)

Learning Rate Schedulers
- [Cosine with Warmup](https://huggingface.co/sharren/vit-lr-cosine-warmup/tree/main)
- [Cosine with Restarts ](https://huggingface.co/sharren/vit-lr-cosine-restarts/tree/main)
- [Reduce LR on Plateau ](https://huggingface.co/sharren/vit-lr-reduce-plateau/tree/main)
- [Step](https://huggingface.co/sharren/vit-lr-step/tree/main)

Cleaned Dataset
- [Removed Hair](https://huggingface.co/sharren/vit-ds-processed)

Addressing Data Imbalance
- [Data Augmentation](https://huggingface.co/sharren/vit-augmentation)
- [Balanced Class Weighting](https://huggingface.co/sharren/vit-class-weight)

Dropout 
- [0.2](https://huggingface.co/sharren/vit-dropout-0.2)
- [0.3](https://huggingface.co/sharren/vit-dropout-0.3)
- [0.4](https://huggingface.co/sharren/vit-dropout-0.4)
-  [0.5](https://huggingface.co/sharren/vit-dropout-0.5)

AdamW
 - Weight Decay 
			 - [1e-2](https://huggingface.co/sharren/vit-weight-decay-1e-2)
			 - [1e-3](https://huggingface.co/sharren/vit-weight-decay-1e-3)
			 - [1e-4](https://huggingface.co/sharren/vit-weight-decay-1e-4)
			 - [1e-5](https://huggingface.co/sharren/vit-weight-decay-1e-5)
 - Beta1
			 - [0.85](https://huggingface.co/sharren/vit-beta1-0.85)
			 -  [0.88](https://huggingface.co/sharren/vit-beta1-0.88)
			 - [0.95](https://huggingface.co/sharren/vit-beta1-0.95)
 - Beta2
			 - [0.99](https://huggingface.co/sharren/vit-beta2-0.99)
			 - [0.995](https://huggingface.co/sharren/vit-beta2-0.995)
			 -  [0.9995](https://huggingface.co/sharren/vit-beta2-0.9995)
 - Epsilon 
			- [1e-9](https://huggingface.co/sharren/vit-epsilon-1e-9)
			- [5e-9](https://huggingface.co/sharren/vit-epsilon-5e-9)
			- [1e-7](https://huggingface.co/sharren/vit-epsilon-1e-7)
