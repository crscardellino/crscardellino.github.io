---
layout: post
title: "BASH: 10 (+1) comandos útiles"
date: 2023-04-04 11:00:00 -0300
tags: bash cli text console terminal
---

En este post haré un listado de los 10 (+1 mención especial) comandos más
útiles, a mi criterio, que BASH tiene para ofrecer. El orden es completamente
arbitrario y depende de mis preferencias, no tiene nada que ver con que tan
usado o no sea el comando (muchos de los comandos más comunes no están).
Empezamos:

<!-- more -->

**Mención especial**: `awk`, no lo uso tanto como antes (suelo directamente usar
combinaciones de `cut` y otros comandos más simples), pero `awk` es
extremadamente poderoso a la hora de manejar flujos de texto.

**10\.** `pkill`: Un comando muy útil (sobre todo con la opción `-f`) para matar
procesos que se colgaron sin tener que andar buscando el PID.

**9\.** `xclip`: Copy/Paste desde la línea de comandos. Inspirados de
`pbcopy`/`pbpaste` de OSX. De echo, tengo los alias: `pbcopy=xclip -selection
clipboard` y `pbpaste=xclip -out -selection clipboard`.

**8\.** `xargs`: Convertir inputs desde el STDIN en comandos. Muy útil junto con uno
comando que presentaré más adelante en la lista.

**7\.** `grep`: No creo que este necesite presentación. Quizás uno de los comandos
más útiles del entorno linux cuando se trabaja con texto.

**6\.** `sed`: Otro viejo conocido de linux, para edición de texto en flujo
("stream"). Herramienta excelente para todo tipo de ediciones en pipeline.

**5\.** `curl`: Si bien hay opciones mucho más modernas, como `http`
(https://httpie.io) hay algo en la simplicidad de `curl` de mandar directamente
al STDOUT cualquier response de HTTP que lo hace super versátil.

**4\.** `zcat`: Algo que empecé a utilizar, muy a mi pesar, hace relativamente poco.
La simplicidad de poder lanzar directamente al STDOUT sin tener que esperar que
se descomprima el archivo por completo es maravillosa.

**3\.** `jq` (https://stedolan.github.io/jq/): Un `sed` para `JSON`, muy poderoso y
versátil, en especial cuando se usa junto con `zcat` y `head` para inspeccionar
archivos de "JSONLines" o JSON APIs que provengan de `curl`/`http`.

**2\.** `rsync`: Una "Swiss Army Knife" a la hora de mantener sincronicidad entre
directorios (incluso remotos), probablemente mejor definida como una "Double
Edge Swiss Army Knife" porque si no aprendés a usarlo bien podés hacer desastre.

**1\.** `find`: Probablemente el mejor comando. Super versátil, hace de todo (y
tiene su learning curve también), pero a la hora de manejar archivos (no sólo
buscar sino también manipular) este comando mágico (sumado a `xargs`) tiene un
sinfin de usos.
