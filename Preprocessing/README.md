In this section, we will

1. Combines both folders into a single folder (all_images_dir)
2. Reorganize the combined folders into 7 subfolders based on their labels (data_dir)
The reorganized structure is as follows:
```
reorganized/
...nv/
......nv_image_1.jpg
......nv_image_2.jpg
...mel/
......mel_image_1.jpg
......mel_image_2.jpg
...bkl/
......bkl_image_1.jpg
......bkl_image_2.jpg
...bcc/
......bcc_image_1.jpg
......bcc_image_2.jpg
...akiec/
......akiec_image_1.jpg
......akiec_image_2.jpg
...vasc/
......vasc_image_1.jpg
......vasc_image_2.jpg
...df/
......df_image_1.jpg
......df_image_2.jpg
```
3. Splits the reorganized data into train and test sets
4. Stores the train and test sets in Google Drive (train_dir and test_dir)
5. Creates train, test, and val tf.data.Dataset from image files in respective directory
6. Stores the val sets in Google Drive (val_dir)
7. Push the original sets to 🤗 in [here](https://huggingface.co/datasets/sharren/originalSkin)
8. Preprocess the original dataset to remove hair noises
9. Push the preprocessed dataset to 🤗 in [here](https://huggingface.co/datasets/sharren/processedSkin)

