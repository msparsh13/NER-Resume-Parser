# NER Resume Parser

## Overview
It is Resume Parser made using spacy library using en_core_web_lg model

## Key Features
**NLP** : It utilises this
**Transferance learning** : A pretrained model which already has been trained on large corpus is trained on given dataset
**Named Entity Recognisation**

## Dependencies 
* Spacy
* tqdm
* Streamlit
* Sklearn

## Organisation of files
```
/project-root
||-- NER_PARSER.ipynb
||-- train-data.json
||-- ui.py
||==README.md
```

* **NER_PARSER.ipynb :** Its the creation of model
* **ui.py** Streamlit application that utilises model
* **train-data.json** NER Based dataset

