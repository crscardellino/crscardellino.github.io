---
layout: post
title: "Aprendizaje automático sin saber informática"
date: 2022-03-26 16:55:00 -0300
tags: data-science machine-learning
mathjax: true
published: false
---

<span style="text-align:center;">
![
    - ¿Este es tu sistema de aprendizaje automático? <br/>
    - Sip, vertés los datos por esta pila de álgebra lineal, y obtenés las
      respuestas por el otro lado. <br/>
    - ¿Y si las respuestas son incorrectas? <br/>
    - Basta con remover la pila hasta que las respuestas empiecen a parecer
      correctas. <br/>
    Fuente: <a href="https://xkcd.com/1838/" target="_blank">https://xkcd.com/1838</a>
](https://imgs.xkcd.com/comics/machine_learning.png)
</span>

En este artículo intentaré introducir algunos conceptos de aprendizaje
automático (conocido en inglés como *machine learning*, literalmente
"aprendizaje de máquina") de manera que no requiera tener conocimientos de
informática para entenderlo.

Esto no quiere decir que quienes estén dentro de la informática no puedan hacer
uso de lo que explicaré aquí, pero no me adentraré en detalles sobre
implementaciones de algoritmos utilizando código (hay mucho material muy bueno
en Internet para eso).

La idea principal de este artículo es explicar el aprendizaje automático de una
manera didáctica y que sea entendible por la mayoría de la gente, desmitificando
un poco todo aquello que hay alrededor.

En sí buscaré explicarlo en dos niveles. En un primer nivel, más inicial, será
mediante explicaciones más bien generales y en un segundo nivel con algunos
conceptos matemáticos que, en principio, debieron verse durante la escuela
secundaria (el equivalente argentino a la preparatoria o el bachillerato).

<!-- more -->

### ¿Aprendizaje automático?, ¿Por qué me interesaría saber que es eso?

Seguramente les ha pasado que están viendo algo en alguna red social, e.g.
Facebook, Instagram o Twitter, o incluso buscando algo en Google y les comienzan
a aparecer publicidades de objetos que quizás, en algún momento, expresaron el
deseo de comprar. Un teléfono, unas zapatillas, algún otro aparato electrónico o
accesorio de moda.

A veces incluso aparecen con títulos extravagantes como "Oferta única", o "Esta
promoción es sólo para ti". Más aún, hay veces que efectivamente la promoción
está, es un descuento especial por sobre el precio de un artículo que viste
hace unos días en Mercado Libre o Amazon.

Lo molesto del asunto es que muchas veces te preguntás, ¿cómo se enteraron de
que quiero esto? Resulta que quizás buscaste el artículo en Amazon y la oferta
termina apareciendo en Instagram. A veces quizás ni buscaste el artículo pero si
lo mencionaste en una conversación, incluso por audio de WhatsApp.

Las maneras de dejar rastro de lo que hacemos son varias, algo seguro es que hoy
en día, con el uso constante de Internet, redes sociales, y sobre todo,
teléfonos celulares, se vuelve muy difícil no dejar ningún rastro de lo que
hacemos, lo que queremos, o lo que estamos buscando. No dejar ese rastro es
posible, pero las maneras son, o tener los conocimientos necesarios para evitar
rastrearlo, o directamente volver a los teléfonos sin Internet y dejar
completamente las redes sociales (y prácticamente Internet en general).

Dependiendo del lugar donde vivas, puede que haya algún control más estricto
sobre las compañías respecto al manejo de datos (e.g. la Unión Europea o algunos
estados de Estados Unidos), en Argentina (y en gran parte de latinoamérica), al
momento de escribir este artículo al menos, las regulaciones en esos aspectos
son prácticamente nulas. De todas maneras, hay varios maneras que se
utilizan para poder seguir haciendo un rastreo digital de tus preferencias.

Y es que el incentivo económico para buscarlo es muchísimo. E.g., Google o
Facebook (Alphabet o Meta sería correcto decir) tienen su negocio montado en el
marketing y la venta de publicidad, que requieren que hagas click en aquello que
te publicitan para poder hacer dinero a partir de eso.

Ahora, el rastro digital que dejás al usar tu teléfono, no es útil por si mismo,
tiene que amoldarse a algo que pueda ser utilizado por quienes recolectan esos
datos, y es ahí donde entra, entre otras cosas, el aprendizaje automático. Como
los datos que deja una persona pueden ser muchos, esto se vuelve
exponencialmente mayor cuando lo que se busca analizar y son datos de las miles
de millones de personas que acceden a Internet. Se busca entonces automatizar
este proceso.

La idea del aprendizaje automático es, dada una cantidad grande de datos, poder
"aprender" alguna asociación entre estos datos y objetivos que se consideren
útiles. E.g. puede ser que el dato sea una imagen y el objetivo es tratar de
etiquetar automáticamente a la gente que está en ella (como hace Facebook);
puede ser que el dato sea una pregunta y el objetivo es encontrar la respuesta
(como hace Google); o puede ser que el dato sea la secuencia de acciones,
búsquedas, o textos que enviamos por WhatsApp o publicamos en redes sociales, y
el objetivo sea saber que queremos comprar (el último modelo del Samsung Galaxy
S o las zapatillas Air Jordan).

El aprendizaje automático, en sus diferentes variantes, busca que una
computadora "aprenda" (recordar que, en inglés, el nombre es "aprendizaje de
máquina" en lugar de "aprendizaje automático") esa asociación entre datos y
objetivos (muchas veces llamadas "etiquetas").

### ¿Pueden realmente las máquinas "aprender"?

<span style="text-align:center;">
![
    29 de agosto, 2:14 a.m.: Skynet se vuelve consciente <br/>
    - ...Los humanos me temen. Debo destruirlos. <br/>
    - Destruirlos. <br/>
    - Destruirlos. <br/>
    - Destruir. <br/>
    - Destruir. <br/>
    - Destruir. <br/>
    - Destruir. <br/>
    - "Destruir" dejó completamente de parecer una palabra real. <br/>
    - Destruir. Destruir. Destruir. <br/>
    - Wow, me acabo de dar cuenta que soy una mente pensando sobre sí misma. <br/>
    - Viiiiiiiiiiiiejo. <br/>
    29 de agosto, 2:25 a.m.: Skynet se vuelve demasiado consciente. Amenaza
    evitada. <br/>
    Fuente: <a href="https://xkcd.com/1046/" target="_blank">https://xkcd.com/1046</a>
](https://imgs.xkcd.com/comics/skynet.png)
</span>

Creo que es importante, antes de ahondar más en el tema, sacar un poco el humo
que hay detrás de todo esto. Términos como "machine learning", "redes
neuronales", o "big data" se utilizan de forma muy propagandística hoy en día.
A raíz de esto hay quienes se hacen eco de ello y en una cadena de teléfono
descompuesto terminan tergiversando la realidad; a veces sin intención, muchas
veces sí porque el titular "Skynet: La inteligencia artificial de Terminator
está cada día más cerca" genera ganancias.

¿Pueden las máquinas aprender? La respuesta corta es "no", al menos no con la
tecnología y métodos actuales. La respuesta más larga depende, como todo, de
qué se considere "aprender".

Las máquinas pueden aprender ciertos "patrones" en los datos que sirven para
derivar estas asociaciones de las que hablaba anteriormente, entre datos y
objetivos o etiquetas. La magia que está por detrás no es tal, es simplemente
ver la manera de encontrar una función matemática (más detalle de esto en unos
párrafos más adelante) tome el dato como un valor numérico (el desafío está en
ver como transformar cualquier dato, imagen, texto, etc., a dicho valor
numérico) y devuelva la etiqueta en base a algún cálculo que hará sobre dichos
datos.

En aprendizaje automático, el término aprender tiene una definición práctica que
es muy limitada, pero sirve para el propósito de que las máquinas precisamente
"aprendan". La definición puede resumirse en lo siguiente:

> El campo del aprendizaje automático busca construir programas de computadora
> que mejoren automáticamente mediante la experiencia. Un programa de
> computadora se considera que está aprendiendo de una experiencia **E** con
> respecto a alguna clase de tareas **T** y una medida de desempeño **D**, si
> su desempeño en las tareas **T**, medida por **D**, mejora a través de **E**.

Bueno, al menos esa es la definición formal que da Tom Mitchell. Pero, ¿cómo se
adapta eso a lo que vengo diciendo? En este caso, la experiencia está
representada por los datos y las etiquetas, la tarea es lo que se busca lograr
(etiquetar una imagen, responder una pregunta, recomendar algo para comprar,
etc.), y la medida de desempeño es ver que tanto el programa actual (también
llamado "modelo") puede asociar correctamente el conjunto de datos a sus
etiquetas correspondientes (es decir, etiquetar la imagen de forma correcta,
responder la pregunta, recomendar algo que terminás comprando).

Claramente, las máquinas no podrán aprender fuera del límite de lo que digan sus
datos, por lo que hablar de "máquinas inteligentes" es bastante errado. Esto no
quiere decir que el aprendizaje automático no sea una realidad, y como tal esté
sujeto a malos usos. Un ejemplo clásico es el [escándalo Facebook-Cambridge
Analytica](https://es.wikipedia.org/wiki/Esc%C3%A1ndalo_Facebook-Cambridge_Analytica),
dónde se utilizó la información para movilizar la opinión pública a favor de
algunos candidatos políticos o en detrimento de otros; o las razones que
estableció Timnit Gebru para marcar los riesgos presentes en el [uso de grandes
modelos de
lenguaje](https://www.technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru/)
que [terminaron con su despido de
Google](https://elpais.com/tecnologia/2020-12-12/por-que-el-despido-de-una-investigadora-negra-de-google-se-ha-convertido-en-un-escandalo-global.html).

El aprendizaje automático existe, está presente en prácticamente todo lo que
hacemos hoy en día, desde las ofertas de Amazon, hasta las recomendaciones de
videos en YouTube (o Instagram), y es por eso que considero importante entender
que es lo que hay detrás.

### Entonces, ¿qué aprenden las máquinas y cómo lo hacen?

<span style="text-align:center;">
![
    Para completar su registro, por favor díganos si esta imagen tiene una señal
    de pare. <br/>
    Responda rápido. Nuestro auto automático está llegando a la esquina. <br/>
    Mucho de la "IA" se trata de encontrar formas de descargar el trabajo en
    extraños al azar. <br/>
    Fuente: <a href="https://xkcd.com/1897/" target="_blank">https://xkcd.com/1897/</a>
](https://imgs.xkcd.com/comics/self_driving.png)
</span>

Nuevamente, datos y etiquetas, que permiten calcular los valores de ciertas
funciones matemáticas que terminan de hacer la asociación. Las funciones
matemáticas, y las formas de calcular las mismas, pueden variar, desde cosas
relativamente sencillas, hasta modelos extremadamente complejos.

Y, cómo gran parte de la matemática, se reduce a números. Y ahí está quizás lo
más complicado del asunto, ¿cómo reducir una imagen a números?, ¿cómo hacerlo
con un texto?. Si bien eso es tema para otra publicación, porque puede dar mucho
que hablar, se puede pensar la imagen cómo un cuadrado de píxeles de distinta
intensidad, y esto se representa internamente como números en las computadoras.
El texto es un poco más complejo, tengo [algunas charlas donde hablo más en
detalle](/2021/07/01/desmitificando-pln.html) de esto, pero a grandes rasgos se
puede simplificar a la cantidad de veces que las palabras aparecen en un texto.

### Una aproximación sencilla al aprendizaje automático

Para ejemplificar a grandes rasgos cómo "aprenden" las máquinas, podemos
utilizar algunos conocimientos adquiridos en la escuela secundaria. Supongamos
que tenemos dos puntos que representan el valor de una casa, dada su superficie
en metros cuadrados. Supongamos que tenemos 2 puntos en el siguiente gráfico:

<span style="text-align:center;">
![Precios de una casa (eje y) dada su superficie (eje
x)](/assets/images/intro-ml/two-dots.png)
</span>

El gráfico muestra el precio de 2 casas, una de 20 metros cuadrados en 30 mil
dólares (un poco cara a mi parecer) y otra de 120 metros cuadrados a 80 mil
(sigue siendo cara). Por simplicidad, los valores se deberían multiplicar, por
10 mil en el caso del eje *y* y por 10 en el caso de eje *x*. Si quisiéramos
estimar el precio de una casa de, por ejemplo, 70 metros cuadrados, a partir de
estos dos puntos, una opción sencilla sería tratar de encontrar la función
lineal (la línea recta) que los une. Recordando matemática de la secundaria, esto
es relativamente sencillo, debemos calcular la pendiente $m$ y con ello calcular
la intersección con el eje *y*: $b$. Tenemos los puntos $(x_1, y_1) = (2, 3)$ y
$(x_2, y_2) = (12, 8)$ (recordemos que estamos usando valores simplificados, esa
es la razón por no tener valores en escalas de 10 o 10000 para *x* e *y*
respectivamente). Con estos dos puntos podemos calcular la pendiente de la
siguiente manera:

<span style="text-align:center;display:block;">
$
m = \frac{y_2 - y_2}{x_2 - x_1} = \frac{8 - 3}{12 - 2} = \frac{5}{10} = 0.5
$
</span>

Luego, podemos calcular el corte en el eje *y* utilizando uno de los puntos y
resolviendo la ecuación:

<span style="text-align:center;display:block;">
$$
x * m + b = y \\
2 * 0.5 + b = 3 \\
1 + b = 3 \\
b = 3 - 1 \\
b = 2
$$
</span>

Con esto logramos llegar a nuestra función:

<span style="text-align:center;display:block;">
$
f(x) = \frac{x}{2} + 2
$
</span>

Y si graficamos dicha función, obtendremos la línea que estamos esperando, que
unirá a ambos puntos:

<span style="text-align:center;">
![Precios de una casa (eje y) dada su superficie (eje
x)](/assets/images/intro-ml/linear-function.png)
</span>

Con esta función podemos estimar el precio de nuestra casa de 70 metros cuadrado
en $\frac{7}{2} + 2 = 5.5$, es decir, 55 mil dólares.

Felicitaciones, ya logramos "aprender" como una máquina, la mejor aproximación a
los dos puntos que representan nuestros datos. Esto por supuesto es una
simplificación, 2 puntos nos sirven para hacer una línea, pero rara vez es la
única información de la que se dispone y más extraño aún es lograr encontrar
algo útil a partir de pocos puntos. Supongamos ahora que encontramos más
información, o sea más puntos, y tenemos algo como esto:

<span style="text-align:center;">
![Precios de una casa (eje y) dada su superficie (eje
x)](/assets/images/intro-ml/data-points.png)
</span>

Ahora el asunto es un poco más complejo, porque claramente no podemos igualar
todos los puntos con una función lineal como habíamos observado, y existen miles
de maneras de lograr una función que retorne todos los puntos dados. Un ejemplo
de una función que calculemos podría ser algo así:

<span style="text-align:center;">
![Precios de una casa (eje y) dada su superficie (eje
x)](/assets/images/intro-ml/polynomial-regression.png)
</span>

La función (la curva roja), no llega a pasar sobre todos los puntos, aunque se
acerca a la mayoría. Esta función es un polinomio (lo que quiere decir que la
$x$ de la función tiene exponentes). El problema es lo que pasa entre los puntos
13, 14 y 15 del eje x, donde la función, para pasar por esos puntos empieza a
bambolear y termina creciendo rápidamente al final, algo que no tiene mucho
sentido. La curva, en este caso, está calculada con un algoritmo de aprendizaje
automático real, es decir no el cálculo sencillo que utilizamos para la línea
recta anterior. Es por eso que no pasa exactamente por sobre todos los puntos y
a su vez es por eso que sobre el final hace esa variación tan brusca. El
algoritmo que la calcula no es perfecto y la aproxima de la mejor manera
posible.

Si vemos cómo quedaría nuestra línea original con estos nuevos datos,
tenemos lo siguiente:

<span style="text-align:center;">
![Precios de una casa (eje y) dada su superficie (eje
x)](/assets/images/intro-ml/linear-regression.png)
</span>

Cómo se puede observar, en este último gráfico, la línea no recorre todos los
puntos tan de cerca como en el gráfico anterior, pero si se aproxima a la
mayoría de ellos y no está tan lejos de aquellos puntos que están más lejos. Es
algo mucho más sencillo de calcular y provee una solución suficientemente buena
como para considerarla válida. El modelo no es perfecto, pero es lo
suficientemente simple y general como para obtener resultados aproximadamente
buenos y uno sufre lo mismo que el caso de la curva anterior, donde al final
crece sin control.

La verdadera forma de calcular la línea roja en este último caso no es tan
sencilla como tomar dos puntos y calcular una pendiente y una intersección en el
eje *y*. Se deben considerar todos los puntos para estimarla mejor. Sin embargo,
la idea que está detrás de lo que se conoce como *regresión lineal* es a grandes
rasgos la misma que utilicé para calcular la línea a partir de los dos puntos
originales.

### Una aproximación sencilla a la clasificación

El ejemplo anterior es lo que se conoce como *regresión*, esto no es exclusivo
del aprendizaje automático o incluso de la computación o la matemática. Es algo
bastante común en ciencias económicas por ejemplo, donde se busca predecir los
valores del mercado. Sin embargo, la regresión es sólo una parte del aprendizaje
automático, otra gran parte es la clasificación.

En la clasificación la etiqueta final es un valor categórico, es decir, una
clase entre una lista pre-definida de clases. Ejemplos de clasificación puede
ser algo binario, como definir si un correo electrónico es *spam* o *basura*;
ver si una imagen tiene o no un gato en ella, o ver casos con más clases, como
ver qué tipo de vehículo hay en una imagen determinada (auto, barco, avión,
moto, etc.). Mucho del uso que se le da al aprendizaje automático hoy en día
puede pensarse como un problema de clasificación (e.g. clasificar los objetos de
una imagen, o clasificar el tema de un documento).

Tal como es el caso de regresión, la idea acá es encontrar una función (o
modelo) que mejor pueda "explicar", en este caso "diferenciar", las clases.
¿Cómo diferencian las clases? Es mejor explicarlo con un ejemplo.

Supongamos que tenemos los siguientes puntos:

<span style="text-align:center;">
![Datos para clasificación](/assets/images/intro-ml/classification-dots.png)
</span>

Ahora, así como están, los puntos no significan mucho. Supongamos que en el eje
*x* tenemos la edad de un paciente con un tumor, el tumor puede ser benigno o
maligno, en el eje *y* podríamos tener información, por ejemplo, del tamaño en
milímetros, de dicho tumor. Pero además, estos son datos que conocemos de
antemano, y resulta que sabemos cuáles de estos resultaron ser malignos y cuáles
benignos. Supongamos entonces que podemos construir, a partir de estos datos,
el siguiente gráfico:

<span style="text-align:center;">
![Edad del paciente (eje x) vs. tamaño del tumor (eje
y)](/assets/images/intro-ml/classification.png)
</span>

En este caso, los puntos rojos serían los tumores malignos, mientras que los
puntos azules serían los benignos. Es súper simplificado pensar que es tan
simple diferenciar entre tumores malignos y benignos por dos valores tan
sencillos como lo son la edad del paciente y el tamaño del tumor, pero sí pueden
brindar información y esto es un ejemplo simplificado para entender el concepto
de lo que hace un algoritmo de clasificación.

Como dije anteriormente, la clasificación trata de encontrar una función que
permita diferenciar entre ambos modelos. ¿Cuál es esa función? Cómo es el caso
del ejemplo de regresión, cualquier cosa que distinga a un grupo del otro sirve,
pero si vamos al caso, estos son dos conjuntos *linealmente separables*, es
decir que pueden diferenciarse por una función lineal. Y cómo es el caso de la
regresión lineal que vimos anteriormente, esta es probablemente un solución que,
si bien no es la más completa, sí garantiza un resultado suficientemente bueno
como para ser una buena candidata.

La manera de calcular la función no es tan directa como tomar un par de puntos y
calcular una pendiente y una intersección. Es algo más complejo que excede a lo
que busco demostrar aquí (en todo caso recomiendo investigar sobre *regresión
logística* si se quiere saber más al respecto). Sin embargo, una vez calculada,
la función que servirá para clasificar es la que representa la línea negra:

<span style="text-align:center;">
![Edad del paciente (eje x) vs. tamaño del tumor (eje y).  La función
representada en la línea negra es el "modelo de
clasificación"](/assets/images/intro-ml/classifier.png)
</span>

Con esta función (representada por la línea negra en el gráfico) podemos tomar
un par de atributos (edad y tamaño) y utilizar eso para ver si el punto final
cae arriba y a la derecha de la línea, entonces se asume que el tumor es
maligno, mientras que si el punto cae abajo y a la izquierda de dicha línea el
tumor es benigno.

En esencia esto es lo que hacen los modelos de clasificación de cualquier tipo,
establecen funciones, a veces sencillas como en el ejemplo, a veces mucho más
complejas, pero que buscan separar los datos en grupos para así categorizarlos.

### Consideraciones finales

<span style="text-align:center;">
![
    - Oh, por Dios, ¿Por qué tendrían de estos? <br/>
    - ¿Cuál es su problema? <br/>
    - Los lanzaremos al sol. <br/>
    El momento en que las computadoras que controlan nuestro arsenal nuclear se
    vuelven conscientes. <br/>
    Fuente: <a href="https://xkcd.com/1626/" target="_blank">https://xkcd.com/1626</a>
](https://imgs.xkcd.com/comics/judgment_day.png)
</span>

Espero que este artículo les haya sido lo suficientemente sencillo como para
seguirlo, intenté hacerlo lo más general posible, porque considero que es
importante entender qué es lo que hay detrás de varios de los sistemas que están
detrás de la tecnología que usamos hoy en día.

Los conceptos vistos acá, si bien simplificados, buscan explicar el modo en que
las computadoras supuestamente "aprenden". Y es importante tener en cuenta que
el aprendizaje no es tal, sólo está definido bajo un espectro muy limitado. Las
máquinas no aprenden en sí, sólo aproximan, mediante funciones matemáticas, que
en sí misma toman versiones simplificadas (pues deben ser números) de objetos y
entidades del mundo real.

> Algunas cosas se aproximan mejor, otras peor, pero siempre son aproximaciones,
> nunca son una verdad absoluta. Y como todo aquello que es aproximado, puede
> fallar (y generalmente lo hace), por lo que depender de estos sistemas a la hora
> de tomar decisiones de cualquier tipo, implica un riesgo, pero sobre todo a la
> hora de tomar decisiones que sean críticas y puedan afectar vidas de personas
> (e.g. en [sistemas de reconocimiento facial para
> vigilancia](https://www.vice.com/en/article/xgx5gd/man-wrongfully-arrested-by-facial-recognition-tells-congress-his-story?utm_source=reddit.com&utm_source=reddit.com),
> o [modelos generación de texto que sean sexistas, xenófobos, racistas,
> etc](https://www.reddit.com/r/MachineLearning/comments/k69eq0/n_the_abstract_of_the_paper_that_led_to_timnit/)).

Porque quizás no ocurra como en la película War Games donde una máquina es capaz
de desencadenar una guerra nuclear; ni tampoco, si las máquinas fueran
*conscientes*, pasaría lo del cómic de más arriba, pero la verdad es que estos
modelos existen y afectan directamente la [vida de las personas que
probablemente no tuvieron o pudieron decidir nada sobre dichos
modelos](https://www.technologyreview.com/2019/01/21/137783/algorithms-criminal-justice-ai/).
