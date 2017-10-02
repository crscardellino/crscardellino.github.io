---
layout: post
title: "From Python to Scala (I): The Basics"
date: 2014-07-28 20:15:00 +0200
tags: course python scala tutorial
---

This is the first post in a series in which I'll try to give a nice insight for
the Scala Language to a programmer with background in Python. I chose to do
these posts since, at least when I started this series, the "Scala for people
coming from Python" tutorial was a work in progress.

First of all I'll state some of my background (in case you didn't check my
[about]({{ root_url }}/about) page), in a kind of a disclaimer. There
are people out there who are experts in Python. I'm not one of them. I only have
a background of 4 years in this language, and only work with the 2.X version
(started with 2.5 until 2.7). Never even try to learn Python 3. Also, there are
experts on Scala as well, I'm not one of those either. In fact, my Scala
knowledge is far from deep, I learned Scala at the end of last year and been
using it since then (along with Python).

> There are people out there who are experts in Python. I'm not one of them. [...]
> Also, there are experts on Scala as well, I'm not one of those either.

Once you know this, I'll just say I have enough knowledge of both Scala and
Python to get by. I've done some projects in Django and some projects in Play
Framework, but nothing really impressive. The reason I'm doing this set of
tutorials is because when I started to learn Scala I didn't have one and many
times I end up in Stackoverflow looking for how to do in Scala things I did in
Python.

<!-- more -->

For this task, I'll make use of the examples and general structure of the
[Python Tutorial](https://docs.python.org/2/tutorial/index.html), and
demonstrate how to do the same examples in Scala. Trough this tutorial I'll
assume you have a decent knowledge of Python (at least you read the Python
Tutorial). I'll also assume you've already installed Scala on your machine and
get running your first "Hello, world!" app (if not, please refer to the [Scala Getting Started](http://www.scala-lang.org/documentation/getting-started.html)
section).

#### The Scala REPL (The Python Interpreter)

As Python, Scala also has an interpreter: the Scala REPL (from Read–eval–print
loop). In this mode, just as in Python's interpreter, you can test different
commands of Scala. Just type "scala" in your shell and voilà, you have your own
Scala shell:

    $ scala
    Welcome to Scala version X.Y.Z (Java HotSpot(TM) 64-Bit Server VM, Java X.Y.Z).
    Type in expressions to have them evaluated.
    Type :help for more information.

    scala>

You can use it, for example, as a calculator, as shown with Python interpreter
in [An Informal Introduction to Python](https://docs.python.org/2/tutorial/introduction.html). The main
difference being in that Scala REPL will create a value (not the same that a
variable) with the name "res" plus a number depending on the number of
operations not assigned to any value or variable you have done so far. This
value will have an inferred type and won't be changeable for the rest of the
session.

    scala> 2 + 2
    res0: Int = 4

    scala> 4 + 4
    res1: Int = 8

    scala> res0
    res2: Int = 4

    scala> res0 = 5
    <console>:8: error: reassignment to val
           res0 = 4
                ^

As you could notice in the last example, even if you try to get the value of a
res you'll end up creating another res (look what happens when "res2" is
created).

#### Scala Strings & Chars

One important different when working on Scala, is the strings declaration. In
Python you can declare a String with single quotes or double quotes, for
example:

    >>> 'spam eggs'  # single quotes
    'spam eggs'
    >>> 'doesn\'t'  # use \' to escape the single quote...
    "doesn't"
    >>> "doesn't"  # ...or use double quotes instead
    "doesn't"
    >>> '"Yes," he said.'
    '"Yes," he said.'
    >>> "\"Yes,\" he said."
    '"Yes," he said.'
    >>> '"Isn\'t," she said.'
    '"Isn\'t," she said.'

In Scala, double quotes are for strings and single quotes are for characters.
The values of type Char are actually numbers, but representative of the
characters in some codification. However, you should not use them for operations
that should go for integers, although these operations are permitted.

    scala> "This is a string" // Ok
    res3: String = This is a string

    scala> 'c' // This is a character
    res4: Char = c

    scala> "c" // This is also a string
    res5: String = c

    scala> 'This is error' // Wrong
    <console>:1: error: unclosed character literal
           'This is error'
                         ^

    scala> "This is a " + "concatenation of strings"
    res6: String = "This is a concatenation of strings"

    scala> 'A' + 'B' // This will produce a sum of integers of 131 ('A' = 65, 'B' = 66)
    res7: Int = 131

Finally, the last for this session, to print, there are two built-in functions:
print() and println(). The first prints a string passed by parameter and the
second prints a string and adds an ending "\n" character (new line). Both of
these functions take their parameters inside parentheses:

    scala> print("Hello, world!")
    Hello, world!
    scala> println("Hello, world!")
    Hello, world!

    scala> println "Hello, world!" // Wrong! This is not Python
    <console>:1: error: ';' expected but string literal found.
           println "Hello, world!"
                   ^

Ok, so, this is all for this session, very basic, nothing too complicated. I'll
be posting more on this crash course during the next weeks. I hope this is
useful for you and I'll thank all comments for feedback.
