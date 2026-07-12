---
title: Refactorizando mi web con ayuda de OpenCode
date: 2026-07-12 15:00:00 -0300
category: artificial intelligence
tags:
  - artificial intelligence
  - tools
---

### El contexto

Este año volví a dar una charla en la [FLISoL Córdoba
2026](https://librebase.org.ar/flisol-cordoba-2026/), la última había sido sobre
[Hugging Face para IA
Colaborativa]({filename}/posts/2023-11-20-hugging-face.markdown), es justo decir
que estos últimos 3 años el panorama en IA ha cambiado mucho. En esta nueva
charla, un poco más bajada a tierra que la anterior, me concentré en el [uso de
herramientas de Software Libre para armar un
Homelab]({filename}/posts/2026-04-25-armando-un-llm-homelab-con-software-libre.markdown). En particular,
expliqué un poco de [Ollama](https://ollama.com/) y
[Open-WebUI](https://openwebui.com/), y como podemos hacer uso de estas
herramientas de Software Libre para tener nuestro propio "ChatGPT" en casa.

Un tema que, por cuestión de tiempos, sólo pude explicar por encima en la
charla, fue el uso de [OpenCode](https://opencode.ai/). El mayor inconveniente
era el tiempo que toma "iniciar" OpenCode (i.e., que Ollama lea todo el prompt
del sistema que explica el uso de herramientas y agentes), por lo que sólo pude
probarlo con un modelo pequeño de Qwen. Pero me quedó la idea de probarlo en
casa en alguna tarea "útil".

<!-- more -->

Coincidentemente, en esos días también me topé con este
[comentario](https://www.reddit.com/r/LocalLLaMA/comments/1stjwg5/comment/ohtono6/?share_id=cfHF7cum305wjXlgducov&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=2)
en reddit, donde un usuario explicaba como podía correr un servidor de llama.cpp
con Qwen3.6 de 35b (es un MoE que sólo usa 3B en cada query), en una laptop de
8GB de VRAM y 32GB de RAM, bueno, yo tengo algo así, una Lenovo Thinkpad P14s
con un GPU AMD con 8GB de VRAM y 64GB de RAM, así que dije quizás podía darle
una oportunidad.

A su vez, en esa misma época, y por cuestiones de deadlines, me resigné en el
trabajo a usar Claude Code con resultados bastante positivos (en este caso,
logré llegar al deadline). Esto me ayudó a ablandar mi visión sobre el uso de
herramientas de IA para ayudar en el trabajo. Sigo teniendo mis reservas al
respecto, pero entendí que las herramientas de _agentic coding_ son muy útiles
para darles cierto _scope_ a los modelos, de manera que puedan ser más
utilizables en casos específicos.

### La tarea

La tarea en cuestión que encontré era algo que venía postergando hace tiempo, y
que creo es una de las mejores maneras de utilizar agentes de código como Claude
Code, o, en mi caso, OpenCode. En particular porque el contexto está
prácticamente dado, el desafío humano es nulo, la tarea es tediosa y suelen ser
largas y aburridas, y, más importante, el resultado contra el cuál comparar ya
existe. Estoy hablando de tareas de refactorización, y en mi caso en particular
estoy hablando de la refactorización de mi sitio web (si, este mismo que están
leyendo ahora).

Cuando empecé con este blog hace más de 10 años, fue a través de las [GitHub
Pages](https://docs.github.com/en/pages) y por supuesto la manera en que en ese
tiempo te recomendaban armar tu página era a través de
[Jekyll](https://jekyllrb.com/), un generador de sitios estático que todavía
sigue siendo bastante popular. Y si bien cambié varias veces el diseño, e
incluso el generador, siempre me mantuve en el ecosistema de Ruby, por dos
razones, en su momento Python no tenía buenas opciones de generación de
contenido estático (o al menos no recuerdo que me gustaran), y en segunda
instancia esto era una oportunidad para mi joven yo de usar Ruby que era otro de
los tantos lenguajes aprendidos por una versión mía más joven y con mayor
energía.

El problema fue que con el paso del tiempo, Ruby y Jekyll fueron evolucionando,
y a medida que sus versiones aumentaban, y saltaban problemas con
vulnerabilidades o dependencias que no se mantenían más, y yo cada vez con menos
tiempo (y ganas) de mantenerlo al día. Quería pasar a Python, aprovechando a
[Pelican](https://getpelican.com/) que es un generador que cumplía con los
requerimientos que yo buscaba (el principal, ser Python). Y no es que Python o
Pelican no vayan a tener las mismas evoluciones naturales que Ruby y Jekyll,
pero la diferencia es que con Python trabajo todos los días, y si algo se rompe
me da menos pereza de arreglar, porque entiendo como hacerlo sin tener que estar

El problema mayor, y la razón por la que estuve posponiendo esto, era lo tedioso
y agotador (y aburrido) de tener que organizar el refactor, revisar todo, y, más
aún, ver como mantener la estructura del sitio lo más parecido posible a la
original. El diseño de la web, basado en
[Minima](https://github.com/jekyll/minima), fue adaptado y cambiado por mi
durante muchos años de ajustes, y llevar todo eso a un nuevo generador estático
no era una tarea trivial, requería una revisión punto a punto de todo, un ensayo
y error bastante complejo y tedioso.

Alas, encontré en esta tarea el uso exacto para probar este nuevo modelo de Qwen
en un laboratorio puramente local, y los resultados me sorprendieron mucho.

### El setup

Siguiendo el consejo del usuario de reddit, y para tener un poco más de control,
decidí ir con [llama.cpp](https://llama.app/) en lugar de Ollama (que es lo que
expliqué como usar en la FLISoL). La razón principal es porque necesito
asegurarme que el modelo esté en memoria todo el tiempo, algo que Ollama por
defecto no hace (hay que configurarlo), pero además llama.cpp me da más opciones
de configuración personalizadas, y es ligeramente más eficiente que Ollama, algo
que con recursos limitados es crucial. Sigo creyendo que Ollama es mejor cuando
uno quiere probar distintos modelos, por su estructura de load/deload que es
mucho más pulida que lo que ofrece llama.cpp, pero para este caso creo que
llama.cpp ofrecía mejores resultados. Descargué el [modelo en
cuestión](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/resolve/main/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf?download=true),
en este caso el `Qwen 3.6 35B A3B Q4 XL`, que es el modelo más grande quantizado
en Q4, igual, hay varios modelos que se [pueden probar en la misma
familia](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF). La razón de usar
el de 35B es que, al ser un Mixture-of-Experts, sólo usa una fracción de
parámetros durante la inferencia, a diferencia del modelo denso de 27B que usa
la totalidad. Nuevamente, para hardware limitado es importante esto.

A partir de eso me armé un script de bash `load-llama.sh` que puse en el path
para cargarlo automáticamente:

```bash
#!/usr/bin/env bash

set -e

MODEL_NAME=${MODEL_NAME:-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf}
MODEL_ALIAS=${MODEL_ALIAS:-default}

docker run --rm -d --name llamacpp \
    --device /dev/kfd \  # Las `--device` flags son para GPUs de AMD
    --device /dev/dri \
    -v "$HOME/.local/llamacpp/models:/models" \
    -p 8000:8000 \
    ghcr.io/ggml-org/llama.cpp:server-vulkan \  # `server-vulkan` es para GPU de AMD
    --model /models/${MODEL_NAME} \
    --host 0.0.0.0 \
    --port 8000 \
    --alias ${MODEL_ALIAS} \
    -c 131072 \
    -n 32768 \
    --no-context-shift \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --repeat-penalty 1.00 \
    --presence-penalty 0.00 \
    --fit on \
    -fa on \
    -ctk q8_0 -ctv q8_0 \
    --chat-template-kwargs '{"preserve_thinking": true}'
```

Por otro lado, configuré mi instancia de OpenCode con los siguientes parámetros
(en particular el `provider` está configurado para encontrar la versión local
del modelo):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "lsp": true,
  "permission": {
    "*": "ask"
  },
  "provider": {
    "llamacpp": {
      "models": {
        "default": {
          "_launch": true,
          "name": "qwen3.6:35b"
        }
      },
      "name": "Llama.cpp",
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:8000/v1"
      }
    }
  }
}
```

### El trabajo

Una vez que tenía el setup completo y funcionando, comenzó la tarea de buscar
algo para guiar al LLM en el proceso de refactorización, y apareció un post de
2024 que trataba justo lo que estaba necesitando: ["From Jekyll to
Pelican"](https://natelandau.com/from-jekyll-to-pelican/).

Con esto, habilité algunas de las opciones experimentales de OpenCode, en
particular para que pueda hacer "WebFetch" y "WebSearch". Hay que tener cuidado
con estas opciones igualmente, pueden ser vectores de ataques de Prompt
Injection, por lo que hay que verificar que el agente no realice operaciones sin
nuestro permiso:

```bash
$ OPENCODE_EXPERIMENTAL=true OPENCODE_ENABLE_EXA=1 opencode
```

Le pasé a opencode la página web y le pedí que la leyera para tener contexto.
Con eso comenzó a armar un esquema de cosas que tenía por hacer. Y aquí es
quizás lo más importante a la hora de lidiar con LLMs y agentes, el espacio. Por
una cuestión de tener una ventana de contexto limitada, en este caso de ~128k
tokens, es importante ser consciente de que todo lo que se haga o se planee
hacer, quede documentado, ya sea en archivos como `AGENTS.md` o `CLAUDE.md`, o
directamente en `TODOs.md`. Es escencial explicarle y planificar de antemano,
porque todo lo que se pierde cuando se llena la ventana termina siendo difícil
de trabajar.

Una cosa que me sorprendió, en particular de modelos como los de Qwen 3.6 35B,
es la capacidad que tienen para interpretar código y tomar decisiones. No son de
la calidad de Claude Opus (o Sonnet si vamos al caso), y hay que saber
dirigirlos bien, pero pueden establecer ciertos parámetros de trabajo muy
útiles. Un ejemplo fue que, originalmente tenía parte de los estilos de mi blog
en SCSS/SASS, y eso venía siendo un problema porque las dependencias de eso eran
las que más se rompían, el LLM decidió hacer una transpilation y dejar
directamente el CSS, y si bien SCSS/SASS es más intuitivo para mi, y esa es la
razón por la cuál me resistía a cambiarlo, la verdad es que tener el LLM que se
encargue de ajustar los cambios que sean necesarios sin necesitar estar yo
buscando en documentación como hacer tal cosa en un lenguaje que utilizo poco
(CSS en este caso), es muy útil.

Algo que me pareció muy interesante es que el agente pudo resolver un tema
crucial entre Jekyll y Pelican, respecto al sistema de templates, y si bien
necesitó un poco de ayuda de mi parte para ajustar algunas cosas, en especial a
medida que la ventana de contexto se llenaba, pudo traducir de Liquid, el
lenguaje de templating de Jekyll, a Jinja, el de Pelican. En particular me
pareció muy interesante que se haya dado cuenta en su momento la naturaleza
distinta de cada sistema, mientras que Liquid tiene una aproximación donde las
templates más pequeñas se incluyen en las más grandes (algo estilo Top-Down), el
sistema de Jinja es más de herencia (i.e., un template no incluye otras más
chicas, sino que extiende un template de la que hereda).

Otro punto interesante es el sistema de subagentes que plataformas de agentic
coding utilizan, para realizar subtareas sin quemar la ventana de contexto al
hacerlo. Esto, en un homelab local sin embargo, es algo que debe saber
administrarse, muchas veces los modelos tienden a lanzar muchos agentes en
paralelo, y eso agota recursos muy rápido. Es mejor tratar de establecer cierto
límites en ese aspecto y sólo usarlo cuando es necesario, ya que por cada
subagente, se lanza un nuevo proceso en el LLM que borra el estado actual hasta
que dicho proceso termine con un valor, y después hay que volver a esperar para
que el proceso original ingiera su contexto original, que se perdió al lanzar el
subagente, además de los nuevos datos, esto puede llevar a mucho tiempo de
espera.

### Algunos aprendizajes y conclusiones

Algo que entiendo que tienen estos modelos, en particular junto a sistemas como
Opencode y Claude Code, es la capacidad de ayudarnos a no perder el hilo de lo
que venimos haciendo. Puedo iniciar una sesión o cambiar de contexto mucho más
fácil ya que no tengo que preocuparme de recordar lo que estaba haciendo, el
modelo lo hace por mi. Eso, sumado a la posibilidad de estos modelos de ingerir
mucho código en relativamente poco tiempo, los hacen muy útiles para entender
código en el que estuve trabajando hace mucho, o incluso código que no escribí
yo.

Por otro lado, creo que los LLMs han mejorado mucho estos años y por suerte
tenemos opciones como Qwen o Gemma que todavía nos dan cierto grado de control
sobre los sistemas que tenemos. Creo que de ahora en adelante las cosas van a
seguir mejorando y estoy seriamente pensando en invertir en tener una máquina
con buen hardware para soportar estos modelos de manera más utilizable.

Como dije, en especial para uso en base a un setup local, con hardware limitado,
los LLMs distan de ser la mejor herramienta para cualquier tarea. Sirven para
cosas que se puedan dejar en modo automático y no requieran supervisión
constante, como encargarles una refactorización o pedirles que resuman cómo
funciona un repositorio de código.

Usar y/o pagar subscripción a Claude, ChatGPT, o similares todavía no es mi
idea, al menos no pagarla yo, en el trabajo me la brindan. Aún así, trato de no
dejar la parte de "pensar" o "tomar decisiones" a los LLMs porque siento que eso
me puede traer problemas a largo plazo, en el sentido de que creo que si un
músculo no se usa, se atrofia, y el cerebro no es distinto (pero bueno, también
estoy intentando dejar videos cortos tipo YouTube Short o Reels de Instagram y
nunca tuve TikTok, así que entiendo que soy un poco peculiar en ese sentido).
También entiendo que los LLMs, en especial los servicios pagos, tienden a
generar mucho texto y por ende mucho código, lo que los hace difíciles de
auditar, creo que es necesario establecer ese límite y soy de poner en claro en
las instrucciones que lo que se genera debe ser "human readable" en el sentido
de que sea conciso y sin tanta verbosidad.
