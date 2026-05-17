---
title: Procesando Datos con Spark (I) - Configurando Apache Spark y Apache Zeppelin
date: 2018-12-19 18:00:00 -0300
category: data science
tags:
  - data science
  - tools
  - scala
  - spark
---

<sup><sub>(Post original en
[Medium](https://medium.com/@crscardellino/procesando-datos-con-spark-i-configurando-apache-spark-y-apache-zeppelin-b8dbda672aa4).
Esto es para archivo.)</sub></sup>

## Un poco de contexto (pueden saltearlo)

Hola a todos y gracias por tomarse un tiempo para leer mi artículo. A diferencia de todo lo anterior que he publicado (que está relacionado a mi trabajo), este será el primero de una serie de recursos para aprender ciencia de datos en español.

La motivación de hacerlo en español es que, además de ser mi lengua nativa, el viernes 7 de diciembre del 2018, en la [Facultad de Matemática, Astronomía, Física y Computación](http://www.famaf.unc.edu.ar/) (FAMAF para la comunidad), en la [Universidad Nacional de Córdoba](https://www.unc.edu.ar/) (Argentina), se dio el cierre de la Diplomatura en [Ciencia de Datos, Aprendizaje Automático y sus Aplicaciones](http://diplodatos.famaf.unc.edu.ar/) (créanme, el título iba a ser más largo). Este fue un proyecto conjunto entre los docentes de FAMAF (los que nos dedicamos a Ciencia de Datos y Aprendizaje Automático) y el [Córdoba Technology Cluster](https://www.cordobatechnology.com/) y se realizó con el objetivo de formar recursos humanos especializados en ciencia de datos en Córdoba y la región.

Más allá de ser una experiencia muy positiva el haber podido aportar a la comunidad local mis conocimientos sobre el tema y ver cómo estos eran aprovechados por profesionales de diversas áreas (programadores, biólogos, economistas, etc.), me hizo darme cuenta lo valioso que puede llegar a ser para mucha gente el conocimiento que uno tiene y más aún los pocos recursos que hay en el idioma de uno (algo que marcaron mucho a lo largo de la diplomatura). Y es verdad, la mayoría (por no decir todos) de los recursos de aprendizaje se encuentran en inglés, en un mundo donde el español es una lengua que no carece de representación.

Es en base a esto que decidí dedicar un poco de mi tiempo a hacer divulgación en español, para que más hispanohablantes puedan hacer uso de los conocimientos existentes hoy en día.

## Introducción a Spark

No solo hago difusión y divulgación vía Internet o dando cursos o diplomaturas.  También lo hago en el trabajo. Que puedo decir, la docencia es una vocación para mi.

Precisamente, en el trabajo, estoy organizando una serie de charlas que sean introductorias a mis colegas al área de ciencia de datos. Lo sometí a votación y, a pesar que mi mayor experiencia es en el reino de Python, mis colegas se sienten más intrigados por Spark (probablemente porque muchos de ellos tengan conocimientos de Java). Cómo sea, decidí hacer una serie de tutoriales que inicien a mis compañeros en el mundo de Spark y mi idea es también utilizar una serie de artículos para transmitir dicho conocimiento.

### ¿Qué es Apache Spark?

[Spark](https://spark.apache.org/) es una librería, escrita originalmente en [Scala](https://www.scala-lang.org/) (un lenguaje muy elegante de programación funcional con diseño orientado a objetos, les recomiendo revisarlo si no lo hicieron aún), cuyo objetivo es servir de motor para hacer análisis y procesamiento de datos a gran escala mediante cómputo distribuido. Tiene la gran ventaja de poder utilizarse con diversos lenguajes (Scala, Python, R, Java y SQL) y correr sobre diversos sistemas (e.g., [EC2](https://github.com/amplab/spark-ec2), [Hadoop YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html), [Mesos](https://mesos.apache.org/), [Kubernetes](https://kubernetes.io/)) y poder obtener datos de diversas fuentes (e.g.  [HDFS](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html), [Cassandra](https://cassandra.apache.org/), [HBase](https://hbase.apache.org/), [Hive](https://hive.apache.org/)).

Además, cuenta con diversas librerías integradas para diversos motivos, entre ellas, una para hacer consultas estructuradas utilizando [SQL](https://spark.apache.org/sql/), y otra para realizar tareas de [Aprendizaje Automático](https://spark.apache.org/mllib/).

Esta es una explicación un poco rápida sobre lo que es Spark, que es lo que necesitamos a fines prácticos. Si quieren una explicación un tanto más detallada (aunque sin ser excesivamente técnica) les recomiendo el siguiente video (aunque lamentablemente está en inglés):

<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 2em;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/tDVPcqGpEnM?si=zr0zTwYyqmk4h3sb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


### ¿Qué es Apache Zeppelin?

[Apache Zeppelin](http://zeppelin.apache.org/) es un **notebook basado en una aplicación web**, que sirve para hacer documentos, que sirven para hacer análisis de datos de manera interactiva, ejecutar código, mostrar visualizaciones, etc. En particular, Zeppelin tiene soporte nativo para Spark (ya sea localmente o conectándose a un clúster).

Si bien Zeppelin no es necesario para el trabajo con Spark (de hecho, a la hora de programar un pipeline de Spark es mejor pensarlo como una [aplicación autocontenida](https://spark.apache.org/docs/latest/quick-start.html#self-contained-applications)), la verdad es que a la hora de hacer análisis exploratorio de datos, o escribir prototipos que sean fáciles de probar (_quick and dirty_), un notebook (no solo Zeppelin, también [Jupyter](https://jupyter.org/) también se puede configurar para trabajar con [Scala y Spark](https://medium.com/@bogdan.cojocar/how-to-run-scala-and-spark-in-the-jupyter-notebook-328a80090b3b)) es una herramienta muy útil.

## Instalación y configuración

### Apache Zeppelin

Hay muchas formas de correr Spark. Si bien la forma predilecta sería a través de un clúster (como vimos, hay varios sistemas sobre los que Spark puede correr), la verdad es que para iniciarnos es siempre más sencillo instalarlo localmente.  En particular, Apache Zeppelin viene con una instalación por defecto de Spark que puede utilizarse sin demasiadas configuraciones extras (más allá de instalar Apache Zeppelin). Para eso podemos descargar Zeppelin 0.7.3 desde [este enlace](http://archive.apache.org/dist/zeppelin/zeppelin-0.7.3/zeppelin-0.7.3-bin-all.tgz) y (una vez descargado y descomprimido), ejecutar Zeppelin con el siguiente comando:

```
~/zeppelin-dir $ bin/zeppelin-daemon.sh start
```

Luego de eso, podemos acceder a [http://localhost:8080](http://localhost:8080) para ver la página principal de Zeppelin:

<span class="fig-box">
    ![La página de inicio de Zeppelin]({static}/assets/img/spark/zeppelin-intro.webp)
    <span class="caption">La página de inicio de Zeppelin (cuando accedemos a [http://localhost:8080](http://localhost:8080))</span>
</span>

Para parar Zeppelin, simplemente corren lo siguiente:

```
~/zeppelin-dir $ bin/zeppelin-daemon.sh stop
```

Lo otro bueno de Zeppelin es que tiene una imagen de [Docker](https://www.docker.com/) que pueden utilizar sin grandes problemas, simplemente corriendo el siguiente comando (se los recomiendo por simplicidad):

```
$ docker run -p 8080:8080 --rm --name zeppelin apache/zeppelin:0.7.3
```

Nuevamente, luego de eso accedemos a la dirección [http://localhost:8080](http://localhost:8080).

Si prestaron atención, la versión de Zeppelin que estoy utilizando es la 0.7.3, mientras que la última versión estable de Zeppelin es la 0.8.0 (y la 0.9.0 es la que está en etapa de desarrollo). La razón por la que decidí ir por la versión 0.7.3 es que hay un error en [la versión 0.8.0 que no está permitiendo leer archivos *csv*](https://stackoverflow.com/questions/51195187/cannot-read-csv-file-apache-zeppelin-0-8), puede que el error sea de Zeppelin o del Spark que viene con dicho Zeppelin, como sea, la versión anterior no presenta el error y es más que suficiente para nuestros fines.

Una vez adentro, podemos crear un nuevo notebook (donde dice **Create new note**), dónde definimos un nombre (e.g. "Introducción a Spark") y elegir el intérprete por defecto (_spark_ en este caso), luego podemos ver el notebook en blanco:

<span class="fig-box">
    ![Notebook de Zeppelin en blanco.]({static}/assets/img/spark/zeppelin-blank.webp)
    <span class="caption">Notebook de Zeppelin en blanco.</span>
</span>

### Apache Spark

Si bien la instalación anterior es todo lo que necesitamos realmente para poder comenzar a experimentar con Spark y hacer una análisis de datos básicos (que quedará para la próxima entrega de esta serie de tutoriales), también es útil instalar Spark localmente (es el primer paso para, eventualmente, ponerlo a correr en un clúster o algún otro servidor dedicado). Además sirve para poder luego escribir y probar en menor escala aplicaciones de Spark autocontenidas para que luego sean corridas en un clúster.

Para instalar Apache Spark, primero lo tenemos que descargar desde la [página oficial](https://spark.apache.org/downloads.html). La última versión (la que vamos a utilizar en esta serie de tutoriales) es la 2.4.0. Les recomiendo descargar la versión [pre-compilada para Hadoop 2.7](https://www.apache.org/dyn/closer.lua/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz).

Luego de descargado y descomprimido, pueden ejecutar una consola interactiva de Spark (en Scala) con el siguiente comando:

```
~/spark-dir $ bin/spark-shell --master local[2]
```

Además de esto hay varias formas de [ejecutar una aplicación en Spark](https://spark.apache.org/docs/latest/quick-start.html), que veremos eventualmente. Por ahora es todo lo que necesitan para que tener Spark corriendo localmente en su máquina.

## Finalizando

Describí el proceso para instalar y configurar Apache Zeppelin y Apache Spark.

Este es el primero de una serie de artículos, en español, donde hablaré de herramientas y notas sobre cómo hacer ciencia de datos. En particular este es el primero de una serie de artículos donde introduciré el framework Spark, y cómo utilizarlo para hacer análisis de datos a gran escala.

Trataré de no colgarme para la próxima entrega y tenerla antes del año nuevo (aunque no puedo prometer nada).

¡Gracias por leer!
