---
layout: post
title: "From Python to Scala (IV): Arrays &amp; ListBuffers"
date: 2014-08-07 20:48:00 +0200
tags: course python scala tutorial
---

So, now you've learnt about Scala lists. As you could see in the previous
examples, Scala has a very _functional_ kind of lists, as these are immutable.

If you are ever to use Scala as a functional programming language this is the
way to go. I really recommend you to, at least, try to learn this paradigm, as
it is design purpose and has many advantages. But, then again, even now I
sometimes go back to imperative programming in Scala myself because is more
natural to me. Scala as imperative language is pretty similar to Java, so as a
side effect I ended up learning how to read Java code (I knew some Java but only
the basics, learning Scala my Java understanding improved a lot).

But, lets say that functional programming is way too much to deal with now and
you want to know a type more similar to Python lists, the oldie but goodie
mutable lists. You have a couple of options of data structures available in
Scala, I'll present two of the most commons.

#### Scala Arrays

Ok, if my university's data structure teacher sees me presenting Scala arrays as
an option for a "mutable" list he probably would take away my degree and force
me to redo the Computer Sciences career all over again.

An array **is not** a list and will never be one. But, for someone who comes
from a Python environment, it's probably an easy option to replace a immutable
list for a mutable version.

Arrays are the simplest and one of the oldest (if not _the_ oldest) data
structure you'll ever face with. In fact, most high-level programming languages
lists are internally implemented as arrays. If you've ever deal with a real old
imperative programming language (I'm looking at you C developer), you are
familiar to the concept of array. The thing is that Python doesn't really have
them (at least not internally, you'll have to import a module for dealing with
arrays).

Arrays have some pros and cons in programming, as every data structure. Among
the most common pros of an array you'll find the efficiency they carry in
comparison to lists. As arrays are represented as collection of elements (of the
same type) stored in a continuous space of memory. They differ from lists in
that you'll have an index for all the elements (which makes the access time of a
constant order) and in general are faster to make operations than in lists which
can have chunks of elements sparse in many places.

<!-- more -->

Arrays in Scala are a built-in type (you don't have to import them), and they
are completely compatible with Java arrays (in fact, are implemented as a
wrapper of Java arrays). And, as most arrays, they are naturally mutable as they
are stateful data structure (which makes them perfect for imperative paradigms
that relies on state), in contrast to stateless data structures like lists (more
associated to functional paradigm):

{% highlight scala %}
scala> val array: Array[Int] = Array(1, 2, 3)
array: Array[Int] = Array(1, 2, 3)

scala> array(0)
res0: Int = 1

scala> array(0) = 5 // This, not valid in lists, is valid in arrays.

scala> array(0)  // Arrays are mutable!
res1: Int = 5
{% endhighlight %}

In general terms, you'll be able to do many of the lists' operations in an array
(like concatenation, traverse, length). However, as I state before, arrays are
not lists, and cannot replace them in all the occasions. The thing is that
arrays do not have a functionality to add (append or prepend) elements to them
(and if they do, usually are very time and resource consuming which is not a
good idea). You can emulate it with the concatenation, but it's not the same
thing, and this workaround creates a new structure instead of modifying the
existing one:

{% highlight scala %}
var array = Array(1, 2) // Pay attention to the "var" instead of "val"
array(2) // Will throw an exception.

array = array ++ Array(3) // I'm reassigning the array value as "++" creates a new structure.
array(2) // The new array now has three elements. This will return 3.
{% endhighlight %}

Ok, so far so good, we now have a workaround and it works. Not the simplest and
definitely not the prettiest one, but it works. All set? Are we happy? Of course
we are not happy. It can't be that Scala won't consider a real mutable list in
its library.

Then again, you are right, the Scala team of course made this consideration. But
it's not a built-in data structure, but one you'll have to import from the Scala
collection library.

#### Scala ListBuffer

So we finally meet a real equivalent to the Python list. Or at least the closest
one I can think of. Scala ListBuffer is a mutable data structure which can mimic
a Python list's operations.

For this you'll have to import it as it is not in the built-in types of Scala
(but is included in the Scala library). First, let see a little about module
imports:

{% highlight scala %}
import scala.collection.mutable.ListBuffer // Self explanatory

import scala.collection.mutable._  // Equivalent to Python: from library.sublibrary import *

import scala.collection.mutable.{ListBuffer => MutableList} // Rename of the import
{% endhighlight %}

Very basics, don't think you need too much to be explained. Now lets get to the
real deal. Listbuffers, as well as arrays, are mutable in its values, which
means they can be changed. But also, a listbuffer has the classic append and
prepend operations without the need of creating a new structure out of it:

{% highlight scala %}
scala> val list = ListBuffer(1, 2, 3) // ListBuffer can only store one type values as well as a List. Is a "val".
list: ListBuffer[Int] = ListBuffer(1, 2, 3)

scala> list(0)
res0: Int = 1

scala> list(0) = 2  // This is valid in ListBuffer

scala> list(0)
res1: Int = 2

scala> list.append(4)

scala> list
res2: ListBuffer[Int] = ListBuffer(2, 2, 3, 4)

scala> list.prepend(1) = ListBuffer(1, 2, 2, 3, 4)
{% endhighlight %}

Listbuffers also offer an operator to deal with appending elements at the end.
And finally, they can be easily converted to a Scala list for further working
(if by any chance you needed the listbuffer for an initial construction but then
all the operations are regular list operations):

{% highlight scala %}
val list = ListBuffer(1, 2)
list += 3 // The new value of the list is: ListBuffer(1, 2, 3).

list + 3 // Beware! this make no sense. And in many cases will throw a type mismatch.

list = list + 3 // Wrong. Even if the operation is permitted (not this case) this is a val reassign.

list.toList // Returns a Scala List
list.result // Same as before
{% endhighlight %}

There's also a Scala structure that you can import from the same library of the
ListBuffer, called ArrayBuffer. It provides functionality to append elements
similar to the one of the ListBuffer, but it returns an Array, which is a better
structure (more efficient) when you have to deal with large collections and more
imperative programming. Don't use it if you'll have to prepend many values or
you need the final result to be a list.

Other common data structures implemented in the Scala library include queues and
stacks (with internal array and list representations according to what you
need). I leave it to you to find out and look at the best option for you. The
Scala documentation is pretty well [written regarding the collections](http://docs.scala-lang.org/overviews/collections/introduction.html), specially the part where it explains the [performance characteristics](http://docs.scala-lang.org/overviews/collections/performance-characteristics.html).

I hope you enjoyed the new chapter on my Python to Scala tutorial. As always,
thank you for your time and all comments are welcome. Until next time, happy
coding!
