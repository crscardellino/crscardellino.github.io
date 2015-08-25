---
layout: post
title: "From Python to Scala (III): Lists"
date: 2014-08-05 20:34:00 +0200
comments: true
categories: [course, python, scala, tutorial]
---

Following with the series in this crash course from Python to Scala, today I'll
introduce one of the most useful Scala's data structures and make the comparison
to Python.

#### Scala Lists

Starting off with one of the most used data structures in Scala (and in
functional languages in general) and also the most common data structure in
Python as well: the lists.

A list in Scala is a data structure to represent a collection of values of the
same type. Lists are very used in Python, and the concept is quite similar in
Scala, with a couple of exceptions. First, in Python are written as a list of
comma-separated values between square brackets. The empty list, is represented
as a pair of empty square brackets:

``` scala
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> empty = []
>>> empty
[]
```

In Scala, a list is build with the use of a constructor of name *List* and the
values passed by parameter to the constructor. The empty list is represented by
the empty constructor:

``` scala
scala> val squares = List(1, 4, 9, 16, 25)
squares: List[Int] = List(1, 4, 9, 16, 25)

scala> val empty = List()
empty: List[Nothing] = List()
```

<!-- more -->

One major difference between Python and Scala lists, is in the type. Python
support lists of different types, however in general (and is a good practice to
stick to it) lists in Python only contain elements of the same type. In Scala
this is not optional, lists may only contain elements of the same type in them.

If you take a good look at the previous examples, you'll notice that Scala uses
its type infer engine to determine the type of the lists. In the case of the
"squares" list, it's inferred that is a list of Int, while in the case of the
"empty" list, it is inferred that is a list of Nothing since there's no
information to determine the type of the list (it has no value).

Of course, as Scala lets you declare the type of a value or a variable, it's
possible to force the empty list to be of a certain type. This is very useful in
the needing of making some kind of manipulation between lists and operations
that requires the same type of list.


``` scala
var empty = List()
empty = List(1, 2, 3) // Incorrect. Results in a type error.

var emptyIntList: List[Int] = List()
emptyIntList = List(1, 2, 3) // Correct. New value of the variable is List(1, 2, 3)

emptyIntList = List("a", "b", "c") // Incorrect. Results in type error.
```

Scala lists have a another constructor operator, named **cons** and represented
by two colons **::**. Along with another constructor for the empty list:
**Nil**. If you've never heard about functional programming, this concept is
maybe new to you. For people with Lisp or Haskell background it comes quite
natural. In simple terms, a list in Scala can be constructed like so:

``` scala
val square = 1 :: (4 :: (9 :: Nil)) // Equivalent to List(1, 4, 9)

val empty = Nil // Equivalent to List() with type List[Nothing]

val emptyIntList: List[Int] = Nil // Equivalent to List() with type List[Int]
```

Although this format may seem unnatural for a Python programmer (and most
unnatural for someone who only knows imperative paradigm), this notation is
quite common and is very useful, as a matter of fact is essential, in pattern
matching, something we'll talk about later and that you must know if you plan to
use Scala at its full potential.

#### Operations over Lists

The three most common operations over a list are: isEmpty, head and tail. The
isEmpty operation, as its name says, check wether a list is empty or not. The
head operation over a list will return the first element of the list, much like
Python's **pop(0)**, but with the difference that it won't alter the original
list. Finally, the _tail_ operation has no direct map to a Python's list
function (as far as I know of) and will return a new list with all the elements
of the original list but the first:

``` scala
val empty = Nil
empty.isEmpty // Will return true

val squares = List(1, 4, 9)
squares.isEmpty // Will return false

squares.head // Will return 1
squares.tail // Will return List(4, 9)
squares      // Will return List(1, 4, 9). The original list never changes.

empty.head   // Invalid. Result in an exception. The same happens to empty.tail
```

As lists in Python, lists in Scala also have an indexing function, and as well
as in Python, indexing starts from 0. The difference is that negative indexing
is not possible in Scala:

``` scala
squares(0) // Returns 1. Note that the indexing is with "()" instead of "[]".
squares(2) // Returns 9.
squares(3) // Raises an exception.
squares(-1) // Raises an exception. This is valid in Python, not in Scala.
```

Another common operation over a list is the slice. In Python this is done with a
colon in the indexing. In Scala you'll have to make use of the function
slice(from, until). Although you can use negative values, this won't work as in
Python:

``` scala
squares.slice(0, 2) // Returns List(1, 4)
squares.slice(0, 0) // Returns List()
squares.slice(-1, 5) // Returns List(1, 4, 9)
```

There is a whole set of other methods and operations you can perform on a list,
and we won't discuss it here, check on the [Scala Documentation](http://www.scala-lang.org/api/current/index.html) for more
information on immutable lists.

This is all wonderful, but the structure that I've shown you is not exactly the
list structure a Python programmer is used to. Scala's primitive lists are
immutable, which means you are not allowed to change the values they hold once
they are set. Nonetheless, there is another Scala structure that's more similar
to Python lists. We will discuss it in the next part of the tutorial.

Thank you again for reading this tutorial. I hope it's becoming more helpful
with each new post. Please comment if you have anything to add!
