pneumonia = '''
Pneumonia is an infection that inflames the air sacs in one or both lungs. 
The air sacs may fill with fluid or pus (purulent material), 
causing cough with phlegm or pus, fever, chills, and difficulty breathing. 
A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.
Pneumonia can range in seriousness from mild to life-threatening. 
It is most serious for infants and young children, people older than age 65, 
and people with health problems or weakened immune systems.
#### Symptoms
The signs and symptoms of pneumonia vary from mild to severe, 
depending on factors such as the type of germ causing the infection, 
and your age and overall health. 
Mild signs and symptoms often are similar to those of a cold or flu, but they last longer.
#### Signs and symptoms of pneumonia may include:
* Chest pain when you breathe or cough
* Confusion or changes in mental awareness (in adults age 65 and older)
* Cough, which may produce phlegm
* Fatigue
* Fever, sweating and shaking chills
* Lower than normal body temperature (in adults older than age 65 and people with weak immune systems)
* Nausea, vomiting or diarrhea
* Shortness of breath
Newborns and infants may not show any sign of the infection. 
Or they may vomit, have a fever and cough, 
appear restless or tired and without energy, or have difficulty breathing and eating.
#### When to see a doctor
See your doctor if you have difficulty breathing, 
chest pain, persistent fever of 102 F (39 C) or higher, or persistent cough, 
especially if you're coughing up pus.
#### It's especially important that people in these high-risk groups see a doctor:
* Adults older than age 65
* Children younger than age 2 with signs and symptoms
* People with an underlying health condition or weakened immune system
* People receiving chemotherapy or taking medication that suppresses the immune system
For some older adults and people with heart failure or chronic lung problems, pneumonia can quickly become a life-threatening condition.
'''


covid19 = '''
Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.
Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age. 
The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when it’s your turn and follow local guidance.
The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell.
#### Symptoms of COVID-19
* Fever or chills
* Cough
* Shortness of breath or difficulty breathing
* Fatigue
* Muscle or body aches
* Headache
* New loss of taste or smell
* Sore throat
* Congestion or runny nose
* Nausea or vomiting
* Diarrhea
#### When to Seek Emergency Medical Attention
**Look for emergency warning signs* for COVID 19:**
* Trouble breathing
* Persistent pain or pressure in the chest
* New confusion
* Inability to wake or stay awake
* Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone
'''

vit_base_patch_16 = '''
# vit-base-patch16-224-finetuned-pneumonia-detection
This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0938
- Accuracy: 0.9728
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3
### Training results
| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2082        | 0.99  | 20   | 0.1462          | 0.9402   |
| 0.0832        | 1.98  | 40   | 0.0998          | 0.9658   |
| 0.0517        | 2.96  | 60   | 0.0938          | 0.9728   |
### Framework versions
- Transformers 4.38.2
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
'''
