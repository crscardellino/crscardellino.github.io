---
layout: post
title: "From Python to Scala (II): Types, Variables & Values"
date: 2014-07-30 20:23:00 +0200
comments: true
categories: [course, python, scala, tutorial]
---

#### Scala Types

Following my series of tutorial of Scala for Python programmers, I'll start to
talk about something most Python programmers don't usually pay attention to
because the language doesn't require it to do so.

I'm talking about data types. It's not that Python doesn't have types for its
variables, but as it is a dynamically typed programming language, you usually
don't care about the type of the variable. At least not unless you try to add a
number and a letter: you cannot add apple and oranges, naturally you cannot add
strings and numbers (not at least without conversion first):

In general terms, however, Python won't bother about the type you are giving to
your variables: actually, you won't be able to declare a type for them as Python
will infer it. So, this is perfectly normal for a Python program:

``` scala
string = "This is a string"
print string # Will output "This is a string"

string + 100 # Invalid. Will result in a TypeError exception.

string = 100 # Perfectly valid. `string` type will be int from now on.
print string # Will output 100

string + 100 # Valid. Will result in 200.
```

<!-- more -->

In Scala this is not the case. Once a variable is assigned a type, it will have
it until the end of that variable's scope. Of course, as in Python, some
operations between variables of different types are not permitted. However, in
this case, sum is not one of those cases. If you add a string to a number, Scala
will automatically transform the number into a String and result in a String
concatenation:

``` scala
var string = "This is a string"
println(string) // Will output "This is a string"

string + 100 // Valid. Will result in the string "This is a string100"

string = 100 // Invalid. Will result in a "type mismatch" error.
```

Scala, as well as Python, can infer the type of the variables you are using.
But, it add the possibility to declare the type of the variable (something that
many times comes in handy as we will see in future tutorials):

``` scala
var string: String = "This is a string with declared type"
var num: Int = 100 // This is a number with declared type
```

Scala has a variety of types (you should check on the [Scala Documentation](http://www.scala-lang.org/documentation/) for more information on
it), but the most common are Int (sometimes written as Integer), String, Long,
Float, Double and Boolean.

Although many Python fans can call this a disadvantage, I personally end up
having better experience with static data typing, as I feel I have more control
over the variables of my application. Then again, this is just a matter of
opinion.

#### Variables and Values

So, now you know that Scala is statically typed, which means once you give
variable a type (either inferred by the compiler or declared by the programmer)
you cannot set that variable to a value of another type.

Scala has also two kinds of "variables": mutable and immutable. Ok, maybe it has
only one type of variable, the ones that are mutable, since there is no much
variation in the immutable type. For making this simpler, let's say Scala has to
type of storage locations.

Mutable variables, or just variables, are the classic ones and the most near in
concept to the ones use by Python (with the static type exception). You can
create them with one value and the change them through the whole scope to
whatever value of the same type you want. They are declared with the reserved
word **var**.

Immutable variables, or values, are the ones that will have a constant value
during the whole scope of the variable. If you try to change the value for
another one (even of the same type), the compiler will throw an error. Values
are declared with the reserved word **val**.

``` scala
var variable: Int = 10 // This is a Scala variable.

variable = 20 // Valid. "variable" is now set to value 20.

val value: Int = 10 // This is a Scala value.

value = 20 // Invalid. Will result in a compiler error.
```

If you are coming from the Python environment (or, more in general from a
imperative paradigm environment) you would think values don't have any
usefulness beyond declaring a constant. Nevertheless, in Scala values are quite
fundamental. This is because Scala has been designed as an object-oriented
functional language. The word *functional* is a big deal here, because the
functional paradigm is quite different from the imperative paradigm which most
of Python programmers are used to.

If you ever tried something like LISP, Haskell or Earlang (also known as
*academic languages*), the concept of *stateless* is not a stranger to you. For
most of Python programmers, this is quite unusual though. In the most simple
terms stateless is defined by math functions: you apply a function to some
parameters and get a result. For the same parameters you get the same result
every time, and there will never be an inner state of the function that will
modify that returned value. Stateful (although you probably didn't hear it under
that name) is more common among imperative languages, and means you have a state
that can change the final computation.

This is not a tutorial for functional programming (not even on Scala) but to
understand the basics of Scala. Scala is a multi-paradigm language and can be
used for imperative programming. Still, if you are learning Scala I would
recommend you to learn something on functional programming. Otherwise you will
be wasting the full Scala potential. If you are interested in this matter there
should be lots of tutorials and resources on the internet, but my personal
recommendation is to take the [Functional Programming Principles](https://www.coursera.org/course/progfun) in Scala, in
[Coursera](https://www.coursera.org/), by Martin Odersky (the creator of the
Scala language).

I think is more than enough for this session. As always I appreciate any
feedback on comments (event to tell me I'm having some grammar or spelling
mistakes). Thank you for reading!
