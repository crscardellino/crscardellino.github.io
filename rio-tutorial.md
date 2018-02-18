---
layout: page
title: "Train and visualize a model in TensorFlow"
permalink: /rio-tutorial/
---

# Overview

This TensorFlow tutorial, held in the [25º Escuela de Verano de Ciencias
Informáticas de la Universidad Nacional de Río
Cuarto](http://dc.exa.unrc.edu.ar/rio/), focuses on practical aspects of
implementing and training deep learning models.  We will follow, step by step,
the implementation of neural networks models with TensorFlow and its comparison
with Scikit Learn, focusing on the impact of tuning hyperparameters and
architectures. To keep track of results we will use the visualization tool
Tensorboard and show its functionalities.

### Objective

The goal of this tutorial is for you to learn how to build models in
Tensorflow. You will apply them to a standard document classification dataset,
and keep track of the experiments' performance with Tensorboard, a
visualization tool. 

### Who is this course aimed to?

We strongly recommend to have covered some machine learning basic concepts
previously, as we wont cover them during the tutorial:

- What is a classifier? What is a logistic regression classifier?
- Basic evaluation: metrics like accuracy, precision, and recall. What is the
  train and test split for?
- What is gradient descent and what is a cost function?

# Technical requirements

This tutorial is based in [Jupyter notebooks](http://jupyter.org/) we uploaded
to the [Github platform](https://github.com/PLN-FaMAF/tensorflowTutorial2018).
The notebook named as [**Part 0:
Configuration**](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_0.ipynb)
(which can be rendered directly from Github) has all the software and data
requirements needed to configure the environment. It should be followed before
taking the tutorial in the conference.

### Course slides

The slides shown in the tutorial presentation are available [using this
link](https://docs.google.com/presentation/d/1fmycn9foRpdmqS9rRMNR3nz-rfklhq65aZhYIBlASIo).

### Software

The software packages we are using are Python 3.5 (obtained through conda)
along Numpy, Scipy, Jupyter, and the
[Tensorflow](https://www.tensorflow.org/versions/r1.4/install/) (version 1.4)
libraries. 

Please refer to the
[notebook](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_0.ipynb)
for detailed explanation.

### Dataset

The dataset we will use is a pre-processed version of the [20 Newsgroup
Corpus](http://qwone.com/~jason/20Newsgroups/) for document classification.
[Part 1 of the
tutorial](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_1.ipynb)
is optional and explains how this dataset is obtained.  In any case it is
possible to download the dataset directly to use in Tensorflow from part 2 and
after of the tutorial.

Please refer to the
[notebook](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_0.ipynb)
for detailed explanation and download link.

# Structure

The Jupyter notebooks of the tutorial contain code and explanations that the
attendees can download, execute and modify during the talk. It will comprise
the following parts:

### Introduction and environment setup

This part is covered by the [Part 0:
Configuration](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_0.ipynb)
notebook. It has the instruction to configure the environment and download the
dataset to use.

### Dataset preprocessing (optional)

This part is covered by the [Part 1: Dataset
Preprocessing](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_1.ipynb)
notebook. It explains the dataset we are using to experiment with Tensorflow
and how we process it to have the final version ready.

### Scikit Learn

This part is covered by the [Part 2: Scikit
Learn](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_2.ipynb)
notebook. It explains the implementation of a neural network using Scikit Learn
API. This is explored as a comparison point to the TensorFlow approach.

### TensorFlow's API

This part is covered by the [Part 3: TensorFlow's
API](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_3.ipynb)
notebook. This part explores the backbone of TensorFlow and how it can be used
to create models from scratch.

### TensorFlow DNNClassifier

This part is covered by the [Part 4: TensorFlow
DNNClassifier](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_4.ipynb)
notebook. This explore a simpler API offered by the newer versions of
TensorFlow to create a neural network model.

### Using Tensorboard

This part is covered by the [Part 5: Using
Tensorboard](https://github.com/PLN-FaMAF/tensorflowTutorial2018/blob/master/tensorflow_tutorial_5.ipynb)
notebook. It showcases the visualization tool that comes along with TensorFlow,
named Tensorboard. This part works on how to visualize the progression of a
neural network training.

---

# About the authors

### [Milagro Teruel](https://cs.famaf.unc.edu.ar/~mteruel/)

> I'm a Computer Scientist based in Córdoba, Argentina. I'm currently pursuing a
> PhD in Computing under the direction of Laura Alonso Alemany at Universidad
> Nacional de Córdoba and Marcelo Luis Errecalde, from the Universidad Nacional
> de San Luis. 

### [Cristian Cardellino](http://crscardellino.me)

> I have a degree in Computer Sciences from Universidad Nacional de Córdoba,
> Argentina, and I am finishing my PhD. in the area of machine learning applied
> to natural language processing.
