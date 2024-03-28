# LR & Scheduler Experiment
1. **Initial Learning Rate Experiment:**

Train ViT model separately with initial learning rates of **0.0001, 0.001, and 0.01** using the original dataset.

Utilize a Cosine learning rate scheduler during training.

Plot validation performance against learning rates to identify the optimal initial learning rate.

2. **Scheduler Comparison Experiment:**

Train models using different schedulers **(Cosine with Warmup, Cosine with Restarts, StepLR, ReduceLRonPlateau)** with the optimal initial learning rate

Compare validation performance by plotting against learning rates for each scheduler.
