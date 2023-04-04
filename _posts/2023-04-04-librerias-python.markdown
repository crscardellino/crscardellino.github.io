---
layout: post
title: "Python: Herramientas útiles"
date: 2023-04-04 11:30:00 -0300
tags: python tools libraries
---

En este post haré un listado de herramientas útiles para Python. Pensado
especialmente para Jr. (o incluso Ssrs) que estén por hacer una entrevista en
Python. Estos son sin ningún orden en particular, simplemente son algunas de las
herramientas que más suelo utilizar:

**`collections`**: Una librería con estructuras de datos de colecciones, más allá de
diccionarios o listas, super útil para muchas cosas (diccionarios ordenados,
diccionarios con valores por defecto, `Counter`).

**`itertools`**: Una de las "desventajas" de Python (por algo como C o Java) es
que es "más lento". Y es verdad, no vas a tener el mismo poder de optimización.
Pero a la hora de iterar, itertools ofrece varias cosas mucho más optimizadas
que hacerla "a mano" en puro código Python.

**`operator`**: Módulo con varias funciones y operadores para trabajar de manera
más eficiente (un ejemplo clásico es itemgetter para obtener valores de un
diccionario u algún otro tipo de colección).

**`functools`**: Higher order programming en Python (funciones parciales, reduce
y varias cosas más para lidiar c*on funciones en alto orden).

**`contextlib`**: Una librería para trabajar con "Context Managers" (i.e. los
bloques `with`), si no saben lo que es un Context Manager, les recomiendo que lo
averigüen.

[**`requests`**](https://docs.python-requests.org/en/master/): Una librería
simple para trabajar con requests HTTP (muy útil para construir e interactuar
con APIs).

[**iPython**](https://ipython.org): Una consola interactiva para hacer más ameno
el REPL de Python. En general viene mucho de la mano de
[Jupyter](https://jupyter.org)

[**`joblib`**](https://joblib.readthedocs.io/en/latest/): Para realizar
"Embarrassingly parallel for loops". Si bien Python cuenta con su módulo para
hacer multiprocesamiento, en lo personal prefiero joblib por su simpleza.

[**`lxml`**](https://lxml.de) /
[**BeautifulSoup**](https://crummy.com/software/BeautifulSoup/bs4/doc/):
Un par de librerías eficientes para el manejo de XML/HMTL (en lo personal
prefiero lxml para XML y BeautifulSoup para HMTL, pero son intercambiables en
muchos aspectos).

[**`pytest`**](https://docs.pytest.org/): Una librería excelente y muy completa
para la escritura de tests unitarios.
