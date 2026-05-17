---
title: Procesando Datos con Spark (y IV) - Corriendo una aplicación con PySpark
date: 2019-03-15 19:25:00 -0300
category: data science
tags:
  - data science
  - tools
  - natural language processing
  - python
  - scala
  - spark
---

<sup><sub>(Post original en
[Medium](https://medium.com/@crscardellino/procesando-datos-con-spark-y-iv-corriendo-una-aplicaci%C3%B3n-con-pyspark-5c26e828465d).
Esto es para archivo.)</sub></sup>

Finalizando (al menos por ahora) esta entrega de artículos de introducción a Spark, haré muestra de cómo podemos hacer para crear (y correr) una aplicación con PySpark y Python.

La razón de elegir Python y no Scala para esta última parte, es que Python es mucho más sencillo de configurar a la hora de correr una aplicación de Spark de lo que es Scala (también necesita mucho menos *boilerplate* en el código). Python es muy útil a la hora de prototipar y probar cosas (aunque, a la hora de tener código en producción y para que escale adecuadamente, mi recomendación es hacerlo en Scala o Java).

## **Configurando el entorno de PySpark**

Para trabajar con PySpark necesitarán tener dos cosas instaladas:

1. Un entorno Python: Personalmente aboco por el uso de Python ≥ 3.5. Sin embargo también se puede utilizar Python 2.7 (de todas maneras, lo desaconsejo fuertemente). En particular, recomiendo utilizar [Anaconda](https://anaconda.org/), o al menos crear un entorno con [virtualenv](https://virtualenv.pypa.io/en/latest/). Para el caso particular de la aplicación que se verá en este artículo, se necesita tener instalado [numpy](http://www.numpy.org/) en el entorno Python que se vaya a utilizar.
2. PySpark: Para eso necesitan instalar [Spark](http://spark.apache.org/downloads.html) en su máquina local. En este tutorial se explicará como utilizar el [clúster autocontenido de Spark,](https://spark.apache.org/docs/latest/spark-standalone.html) por lo que no recomiendo instalar la versión de PySpark desde PyPi.

## **Aplicación: LDA para análisis de temas en documentos del InfoLEG**

En este caso en particular, vamos a utilizar el algoritmo de [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) para hacer análisis de temas (mejor conocido como *topic modelling*) de leyes.

En particular, nuestro conjunto de datos serán las leyes de la República Argentina, contenidas en el corpus del [InfoLEG](http://www.infoleg.gob.ar/). Este es un corpus que compilé (obtenido desde la página oficial del Ministerio de Justicia y Derechos Humanos), con casi todas las leyes, decretos, normas, artículos, resoluciones, etc. vigentes en Argentina a la fecha de abril del 2018.

### **Obteniendo el corpus**

El corpus puede obtenerse en [este enlace](https://cs.famaf.unc.edu.ar/~ccardellino/divulgacion/infoleg.txt.bz2). En esta versión simplifiqué algunas cosas y preprocesé los datos como para este artículo. El corpus consiste de un archivo donde cada línea representa un documento (ley, artículo, decreto, norma, etc.).

Descarguen y descompriman el archivo:

```bash
curl -O https://cs.famaf.unc.edu.ar/\~ccardellino/divulgacion/infoleg.txt.bz2
bunzip2 infoleg.txt.bz2
```

El archivo descomprimido es bastante grande. Tiene casi 1 GB de puro texto plano (son alrededor de 120 mil documentos).

Si tienen un clúster disponible, pueden correr el análisis de LDA en todo el corpus. Pero si van a probar desde una máquina de escritorio o una laptop con recursos limitados, recomiendo tomar sólo una parte (e.g. sólo los primeros 100 documentos).

### **Latent Dirichlet Allocation (LDA)**

LDA es un algoritmo utilizado en Procesamiento de Lenguaje Natural que sirve para extraer temas de documentos (agrupando dichos documentos de acuerdo a los temas con los que sean más afines) y describir esos temas en base a un conjunto de términos (palabras).

Es una técnica de *clustering* que sirve para agrupar datos (en temas) y explicarlos (ver de que hablan los temas). Puede ser considerado como un tipo de [*soft clustering*](https://en.wikipedia.org/wiki/Fuzzy_clustering), dado que los datos pueden pertenecer a más de un clúster (tema en el caso de LDA).

No es la idea de este artículo ver en detalle que es LDA, hay mejores lecturas para eso. Simplemente me pareció interesante la idea de aplicarlo y ver que se obtiene.

## **Creando una aplicación Spark**

Hasta ahora hemos visto como ejecutar código Spark bien desde la consola de Spark, o desde un notebook de Apache Zeppelin. Esto es útil para hacer prototipado, ver cosas rápidas, o hacer análisis de resultados (con gráficos y demás).

Sin embargo, a la hora de automatizar procesos (i.e. ejecutar códigos de manera reiterativa, crear pipelines o bien trabajar con grandes volúmenes de manera más eficiente), es mejor crear una aplicación autocontenida de Spark que pueda ser corrida luego sobre un clúster de Spark.

Las aplicaciones de Spark pueden estar escritas en cualquiera de los lenguajes soportados por Spark. En particular, a la hora de trabajar con Python, es sencillamente hacer un código (script) de Python que levante una instancia de una sesión de Spark (que es la encargada de crear los `Dataset`) y luego se ejecute como cualquier código Python.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Infoleg LDA").getOrCreate()
```

Cargamos el archivo del corpus de InfoLEG (ya descomprimido) en un `Dataset`:

```python
text = spark.read.text("path/to/infoleg.txt")
```

En la variable `text` tenemos nuestro conjunto de datos. Una tabla de una sola columna, donde cada fila representa un documento.

### **Preprocesando los datos**

Antes de poder ejecutar el algoritmo de LDA, debemos preprocesar un poco los datos, ya que la [implementación de LDA de Spark](https://spark.apache.org/docs/latest/ml-clustering.html#latent-dirichlet-allocation-lda) no toma texto plano.

### **Tokenización**

El proceso de [_tokenization_](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization) (también conocido como segmentación léxica) es necesario para separar el texto en tokens (e.g. palabras). Spark ofrece una [tokenización muy sencilla](https://spark.apache.org/docs/latest/ml-features.html#tokenizer) donde separa palabras mediante espacios. Sin embargo, esto puede dar lugar a que haya palabras con signos de puntuación pegados, que sean tratadas distintas a la palabra sin el signo de puntuación.

La segmención léxica es un proceso no trivial que, si bien está altamente trabajado, requiere muchas veces de modelos estadísticos o incluso de aprendizaje automático para hacerse bien. Dado que no es ese el objetivo de este artículo, optaremos por hacer una simplificación y simplemente separar a las palabras mediante todos aquellos símbolos que no sean letras (ignoraremos números en esta instancia).

Ahora bien, Spark trae un tipo de tokenización mediante [expresiones regulares](http://www.regular-expressions.info/), con una clase llamada `RegexTokenizer`, que sirve para hacer cosas un poco más complejas. En este caso nos sirve para separar las palabras dejando únicamente las letras. Nuevamente, esto dista de ser completo, pero es buena opción.

Ahora, la expresión regular por defecto que iría en este caso, es algo del estilo `[^a-zA-Z]+`, el problema es que eso sirve para inglés, no así español, que tiene caracteres con tilde o la letra Ñ.

Aprovechando que el archivo del corpus está codificado en `UTF-8 Unicode` podemos hacer uso de la expresión regular `[^\p{L}]` que separará los tokens mediante caracteres que no sean letras del español (e.g. espacios, números, signos de puntuación, etc.). Respecto a este punto, tengo una recomendación: trabajen siempre con el encoding `UTF-8 Unicode` para el español, se ahorrarán muchos problemas (averigüen sobre `iconv` para conversión entre `UTF-8` y `ISO-8859-1`, que es el otro encoding muy utilizado para archivos del español). Este es otro motivo por el cuál utilizar Python 3, que tiene cadenas unicode por defecto y ahora muchos dolores de cabeza.

Finalmente, el código para crear el tokenizer es el siguiente:

```python
from pyspark.ml.feature import RegexTokenizer

tokenizer = RegexTokenizer(inputCol="value", outputCol="words", pattern=r"[^\p{L}]+")
```

En este caso `"value"` es la única columna del conjunto de datos `text`, declarado más arriba, que es la columna que tomará el tokenizer para aplicar la tokenización; `"words"` es el nombre de la columna resultante de aplicar la tokenización sobre la columna de entrada; finalmente, `pattern` es el patrón (la expresión regular) que se utilizará para separar las palabras.

### **Remover palabras “vacías”**

Una práctica necesaria al hacer análisis de texto es la remoción de palabras “vacías” (*stopwords*), que son palabras como conectores, preposiciones, artículos, etc. que no ayudan a dar semántica y aparecen en grandes cantidades, sumando ruido.

Spark también [tiene una opción](https://spark.apache.org/docs/latest/ml-features.html#stopwordsremover) para eso:

```python
from pyspark.ml.feature import StopWordsRemover

remover = StopWordsRemover(stopWords=StopWordsRemover.loadDefaultStopWords("spanish"), inputCol="words", outputCol="tokens")
```

Una vez que tenemos el tokenizer y el filtro, lo aplicamos sobre el conjunto de datos original y obtenemos el conjunto de datos con las leyes tokenizadas:

```python
tokenizedLaw = remover.transform(tokenizer.transform(text))
```

### **Contando palabras**

Los datos son representados con un [modelo de bolsa de palabras](https://en.wikipedia.org/wiki/Bag-of-words_model), pesado mediante un [tf-idf](https://es.wikipedia.org/wiki/Tf-idf).

Para el primero, utilizaremos la clase [`CountVectorizer`](https://spark.apache.org/docs/latest/ml-features.html#countvectorizer), creamos un contador y transformamos el conjunto de datos:

```python
from pyspark.ml.feature import CountVectorizer

counter = CountVectorizer(inputCol="tokens", outputCol="term_frequency", minDF=5)
counterModel = counter.fit(tokenizedLaw)
vectorizedLaw = counterModel.transform(tokenizedLaw)
```

Primero creamos el contador, establecemos que el mínimo de documentos en los que tiene que aparecer una palabra para ser considerada (`minDF`) son 5. Luego entrenamos el modelo (mediante `counter.fit`), y vectorizamos los datos (mediante `counter.transform`). Esto podría haberse hecho en una misma línea de código, pero necesitamos más adelante el modelo entrenado para buscar el vocabulario.

El paso siguiente es aplicar `IDF` sobre el conteo de palabras. Esto sirve para pesar los términos de acuerdo a la cantidad de documentos en los que aparezcan, lo cual sirve para hacer más importantes a las palabras que están fuertemente asociadas a ciertos documentos:

```python
from pyspark.ml.feature import IDF

idf = IDF(inputCol="term_frequency", outputCol="tf_idf")
tfidfLaw = idf.fit(vectorizedLaw).transform(vectorizedLaw)
```

### **LDA**

El paso final, sobre el conjunto de datos ya preprocesado, es efectivamente ejecutar el algoritmo de LDA y revisar los temas obtenidos:

```python
from pyspark.ml.clustering import LDA

lda = LDA(k=10, maxIter=10, featuresCol="tf_idf")
model = lda.fit(tfidfLaw)
```

LDA, como cualquier otro algoritmo de aprendizaje automático, tiene una serie de hiperparámetros que requieren trabajarse, experimentarse, etc. para encontrar la mejor solución. En este caso lo simplificaremos. El valor `k` del algoritmo, es la cantidad de temas (*topics*) que hay que descubrir. Por supuesto, esto requeriría muchos experimentos para encontrar el mejor valor, en este caso nos limitaremos a revisar que información hay con 10 temas, con un máximo de iteraciones de 10 también.

Una vez entrenado el modelo de LDA, para describir los temas, necesitamos indexar los términos a los índices que les asignó el modelo de `CountVectorizer` visto más arriba:

```python
from pyspark.sql.functions import udf

topics = model.describeTopics()
vocabulary = counterModel.vocabulary

def map_idx_to_term(indices):
   return [vocabulary[idx] for idx in indices]

described_topics = topics.withColumn("terms", udf(map_idx_to_term)(topics["termIndices"]))

for idx, row in enumerate(described_topics.select("terms").collect(), start=1):
   print("Tema %d: %s" % (idx, row.terms[1:-1]))
```

La función `map_idx_to_term` es una función [definida por el usuario](https://docs.databricks.com/spark/latest/spark-sql/udf-scala.html) que sirve para tomar una lista de índices, y devolver una lista de palabras asociadas a esos índices en el vocabulario del modelo de conteo.

Lo que hacemos es describir los temas de acuerdo a los términos más importantes y luego imprimirlos por pantalla.

## **Ejecutando una aplicación Spark**

Bueno, en este punto, ya tenemos nuestra aplicación Python para correr sobre PySpark. Si bien podríamos haber ejecutado toda esta aplicación dentro de un notebook de Zeppelin, la idea es que, al tener una aplicación autocontenida, se pueda correr en un clúster Spark.

Ahora bien, este artículo explica como hacer esto localmente en un clúster corriendo en su máquina. Si bien en teoría, el proceso para correr esto es similar que para un verdadero clúster distribuido de Spark, en la práctica la configuración del clúster no es para nada trivial, y no está en el alcance de este artículo.

Para correr esto en el clúster de Spark local de su máquina, asumiendo que ya tienen todo instalado, pueden ejecutar el siguiente comando desde una consola:

```bash
> $SPARK_HOME/bin/spark-submit --master local[*] spark-infoleg.py
```

Dónde `$SPARK_HOME` apunta al directorio base de Spark, `--master local[*]` es la dirección del clúster (en este caso es local), y `spark-infoleg.py` es el script que contiene el código anterior.

Si ejecuto este código, se imprimirá por pantalla un montón de información de logging (no lo configuramos y por defecto imprime mucha información), y entre esto, imprimirá algo del estilo:

> - **Tema 1:** técnica, republica, producción, desarrollo, comisión, personal, autoridad, institucional, nacionales, tareas
> - **Tema 2:** trabajo, convenio, partes, t, acuerdo, empresa, fojas, colectivo, n, gremial
> - **Tema 3:** responsables, régimen, impuesto, salud, deberá, comercio, operaciones, bienes, responsable, fiscal
> - **Tema 4:** republica, entidades, certificados, consumo, salud, código, personas, hacienda, aduanero, importación
> - **Tema 5:** banco, ref, comunicacion, central, enlace, deuda, títulos, autorizado, financiero, financiamiento
> - **Tema 6:** abril, comercio, octubre, costo, presentaciones, autenticada, contradicción, citada, sujeto, normas
> - **Tema 7:** justicia, modificatorias, resulte, articulo, homologados, plazos, congreso, causa, plazo, judiciales
> - **Tema 8:** destinados, norma, tres, implementación, competentes, caso, legislación, anonima, titulares, obligación
> - **Tema 9:** productores, impuesto, párrafo, º, agricultura, pesca, monto, interior, sustitúyese, ley
> - **Tema 10:** trabajo, nº, articulo, t, partes, empresa, acuerdo, trabajadores, fojas, convenio

Estos temas no están muy trabajados. Como dije anteriormente, hay que hacer más experimentos para tener resultados más precisos (o, en este caso, temas mejor definidos).

Lo que se puede observar a simple vista de los resultados, es que los documentos del **Tema 2** tiene que ver con leyes laborales, convenios de trabajo, etc. El **Tema 3** tiene que ver con cuestiones impositivas. El **Tema 4** con cosas de aduana e importación. El **Tema 7** con cuestiones jurídicas. Bastante bien para haber hecho algo a la primera con parámetros bastante estándar.

## **Finalizando**

Bueno, con esto finalizo, al menos por ahora, mis entregas de Spark en español. Es tiempo de trabajar en otra cosa (¡de lo contrario me aburro!).

El código de este artículo puede encontrarse un [repositorio de Github](https://github.com/crscardellino/spark-infoleg). Tiene algunos cambios en el script, que son para hacerlo un poco más dinámico mediante el uso de la librería [`argparse`](https://docs.python.org/3/library/argparse.html), además de que, para evitar que se tenga que buscar el resultado entre un montón de prints de debugging, ofrece la posibilidad de guardarlo a un archivo.

Por lo demás, sigue los mismos parámetros y les recomiendo que lo utilicen. Es más, si bien esto está pensado para InfoLEG, en la práctica el script del repositorio es agnóstico del archivo de entrada, simplemente hace la suposición de que tiene un documento por línea.

¡Muchas gracias por leer!
