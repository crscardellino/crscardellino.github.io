---
layout: post
title: "From Python to Scala (VII): Functions (II)"
date: 2014-08-26 20:05:00 +0200
tags: scala-course python scala tutorial
---

Hello again! Nice to see you decided to come back. If you check my [previous
post]({{ root_url }}/blog/2014/08/23/from-python-to-scala-vi-functions) you
know that functions are quite an important matter in the Scala language.

Last time, talking about recursion, I wasn't able to cover all the topics about
functions. So I decided to dedicate yet another post to it. You can call it
"advanced functions", but I don't think is so "advance" what I'm going to show
here.

You are welcome to read some more on functions in this new blog post.

## Arguments

#### Default Values

Following the [Python Tutorial](https://docs.python.org/2/tutorial/), I'll talk
a little about this.

Default argument values in Scala are very similar to Python's. With the
difference being in the static types, that is, you'll have to explicit declare
the type of the argument:

{% highlight scala %}
def foo(x: Int, y: Int = 0, z: Int = 1): Int = (x + y) * z

foo(10) // Returns 10

foo(10, 10) // Returns 20

foo(10, 10, 2) // Returns 40

foo(10, z = 2) // Returns 20

foo(10, z = 2, y = 10) // Returns 40

foo(10, 10, y = 10) // Error! The parameter `y` has already been specified
{% endhighlight %}

As you can see, there is no problem in how to send the arguments, but if you
don't explicitly tell what parameter you are passing, it will use the order to
define the assignments.

<!-- more -->

In Scala you don't even have to declare all the parameters with default
arguments at the end (like in Python), but it's a good practice as otherwise
you'll face with problems:

{% highlight scala %}
def foo(x: Int, y: Int = 0, z: Int): Int = (x + y) * z // Valid!

foo(10) // Wrong, `z` has no value

foo(10, 15) // Wrong, 15 is assigned to `y` not `z`. `z` still has no value

foo(10, z = 2) // Returns 20
{% endhighlight %}

You see? In this version of foo, you have to explicit declare z as a passed
parameter, otherwise you get an error. That's why it's good practice to keep all
arguments with default values in the end.

Of course, as parameters have a type, you have to give the a default value of
that type (or with an implicit conversion to that type), otherwise is an error:

{% highlight scala %}
def foo(x: Int, y: Int = 0, z: Double = 0) = { (x + y) * z} // Valid. `0` is an Int with implicit conversion to Double

def bar(x: Int, y: Int = 0, z: Double = null) = { (x + y) * z} // Invalid. `null` has no implicit conversion to Double
{% endhighlight %}

Now, on the last code I introduce a new value I don't think I talked about it
before: **null**. The value **null** is similar to the value **None** in Python.
It's specially useful to use it on a variable of a particular class when you
don't want to instantiate that class just yet (for example a class defined by
you). You can use on some variables of Scala types such as String or List, but
not in a primitive type (Int, Double, Char, etc.). We'll talk more about it when
we start working on classes. For now I just wanted to make a quick warning: do
not use the (also) reserved word in Scala of **None** as the value **null**.
It's not the same, None is a value of a special Scala type called **Option**,
that we'll discuss in further posts.

> Do not use the (also) reserved word in Scala of `None` as the value `null`.

#### Arbitrary List

In Scala, as in Python, you can pass an argument representing an arbitrary list
of arguments. This argument always has to be defined as the last one and is
treated as a list of elements of the defined type (you cannot have a list of
types of mixed values):

{% highlight scala %}
def sum(args: Int*) = {
  var x = 0
  for(arg <- args) x += arg
  x
} // Return the sum of all the parameters

sum(1) // returns 1

sum(1, 2) // return 3

sum(1, 10, 100, 1000) // returns 1111
{% endhighlight %}

Now, Scala does not have an equivalent to Python's \*\*_kwargs_. There are some
workarounds you can do, but I don't think it's useful for me to get deep into
that.

## Lambda expressions (a.k.a. anonymous functions)

Well, anonymous functions, such a powerful and useful tool in Scala (when you
start with them, you end up using them everywhere). Anonymous functions are _the
tool_ that makes a functional programming language. These are core concept in
the paradigm, so obviously I won't be able to explain it well enough. Instead,
I'll take the example in the Python tutorial, and show how it is done in Scala.
Then again, you'll have to learn more on anonymous functions on your own, as
it's not the idea of my tutorial to teach more than the basics that helps a
Python programmer enter in the Scala world.

> Anonymous functions are the tool that makes a functional programming language.

Let's show you the Python example of use of a lambda expression, they create a
function which returns a function:

{% highlight python %}
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
{% endhighlight %}

Now, in this example, you create a *lambda* expression using the lambda reserved
word. In Scala the code is quite similar, but you don't need an extra
expression:

{% highlight scala %}
def make_incrementor(n: Int) = (x: Int) => x + n

val f = make_incrementor(42)

f(0) // Returns 42

f(1) // Returns 43
{% endhighlight %}

Pay attention to the returned value by the function `make_incrementor: (x:Int)
=> x + n`. This is the definition of an anonymous function, basically a function
with it's parameters, no name and a => operator instead of a = operator.

This functions can have as many parameters as you want and you can directly
apply them without making necessary to assign them to a value or variable:

{% highlight scala %}
(x: Int, y: Int) => x + y

() => println("Hello, world") // Anonymous function with zero parameter

((x: Int) => x * 2)(20) // Applies the anonymous function and returns 40
{% endhighlight %}

Now, of course, as everything in Scala, functions have types, and sometimes you
may need to explicit declare a function type. This can happen, for example, if
you are declaring a recursive function with a return value of an anonymous
function; however, the function type declaration is fundamental when having a
function's parameter taking a function. This is called [higher-order
programming](http://en.wikipedia.org/wiki/Higher-order_programming) and is a
topic for another post (a whole post in fact), it's another of the core
features of functional programming.

For now, you only need to now that the type of a function is defined by the type
of its parameters and the returning type:

{% highlight scala %}
val foo: Int => Int = (x: Int) => x + 50 // Equivalent to: def foo(x: Int): Int = x + 50

foo(5) // Returns 50

val bar: () => Int = () => 20 // Equivalent to def b(): Int = 20

bar() // Returns 20

val baz: (Int, Int) => Int = (x: Int, y: Int) => x + y // Equivalent to def baz(x: Int, y: Int): Int = x + y

baz(2, 3) // Returns 5
{% endhighlight %}

As you see, sometimes the parentheses are not mandatory when the function only
takes one parameter but it is obligatory in any other case.

Of course, this examples are very simple and don't really show the power of
anonymous functions nor even why sometimes is necessary to explicit the type.
This, hopefully, will come later and you'll understand the importance of it in a
functional programming language like Scala.

So, I think is now time to finish this post. As always, I'll be thankful on your
comments. Best regards and until the next part!
