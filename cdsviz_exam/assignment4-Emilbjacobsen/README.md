# Assignment 4 self assigned

## Contribution
This code has been made in collaboration with others in class and have also used alot of code from this kaggle project.

https://www.kaggle.com/code/pierrenicolaspiquin/classifying-art-pieces


## Assignment description
This project trains 2 classifiersto tell the difference between different forms of art, on the same dataset. The dataset contains images from 5 different categories, drwaings, paintings, engravings, sculptures and iconographics and contains around 9000 images. The aim of this project is to see wether if classifier trained specifically on the data performs can compete with pretrained general purpose models, in this case the vgg16 model. 

A classification report, a loss curve and an accuracy curve will be made for each model to see how they compare to each other, they will be saved to the output folder

## Methods


These two scripts load the art datasets and use CNN's to classify the images into different categories. The dataset unzips to a validation, training split, but i redistributed the data into a train, val, test split to ensure that the classifaction report was based on unseen data

## Usage

### Hardware
I ran this script on a ucloud 32 cpu machine with 192 GB of memory and training the art classifier takes about 13 minutes and the pretrained takes around 25 minutes


### data
Data can be found here: 
https://www.kaggle.com/datasets/thedownhill/art-images-drawings-painting-sculpture-engraving

Unzip the the zip file to the data folder. 
Please keep in mind that when unzipping the data there seemes to be a few corrupted images, both the amount and which images seem to be random. This could have consequences for reproducibility so i have uploaded the exact dataset i used to google drive and they can be downloaded here:


### running the script
If using ucloud, please make sure to have venv installed:
sudo apt-get update
sudo apt-get install python3-venv

set working directory to assignment4-Emilbjacobsen and run:
bash setup.sh

For some reason the virtual environment wont activate from my sh file, if you have the same problem, please just run this with assignment1-vis-Emilbjacobsen as working directory after running setup.sh, you can tell its activated if its in a parentheses next to the coder in terminal:

source ./assignment2_viz_env/bin/activate


Then unzip the the zip file to the data folder and go to the src dir in terminal and paste this:

python3 data_prepper.py

this will convert the data to train, val, test split


Then just run the scripts from the src like so:

set working directory to assignment4-Emilbjacobsen and run:
bash setup.sh



python3 script_train_class.py

and

python3 script_vgg16.py





## Results
While both models have high performance, the pre trianed vgg16 model does outperfom the CNN classiffier i trained myself on all categories, but not by much, there is only a 0,4 difference in accuracy. Both models show lower f1 score in categories 0 and 1, this is most likely because these also contains the least amount of images, with 860 training images for the drawings category and 588 images for engravings, compared to 1612, 1350 and 1592 in the other categories. this suggest that both models would benefit from an expansion of the dataset.

Art trained CNN classifier report:

              precision    recall  f1-score   support

           0       0.72      0.53      0.61       185
           1       0.67      0.71      0.69       127
           2       0.83      0.96      0.89       347
           3       0.95      0.85      0.90       339
           4       0.81      0.88      0.84       290

    accuracy                           0.83      1288
   macro avg       0.80      0.78      0.79      1288
weighted avg       0.83      0.83      0.82      1288

vgg16 classifier report:

              precision    recall  f1-score   support

           0       0.69      0.64      0.66       185
           1       0.69      0.75      0.72       127
           2       0.93      0.97      0.95       347
           3       0.96      0.88      0.92       339
           4       0.88      0.93      0.91       290

    accuracy                           0.87      1288
   macro avg       0.83      0.83      0.83      1288
weighted avg       0.87      0.87      0.87      1288

The accuracy and loss curves suggests that the pretrained vgg16 model already starts overfitting around the the 7th to 10th epoch, which was expected, due to its relatively fewer trainable parameters.

The art CNN on the other hand seems to keep improving even by the 27th epoch.