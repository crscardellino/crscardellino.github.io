---
layout: post
title: "From Python to Scala (VI): Functions"
date: 2014-08-23 20:30:00 +0200
tags: scala-course python scala tutorial
---

Welcome to another post on my series of tutorials. As you can see (if you were
following my tutorials since I started them), I change the environment of my
blog, using Octopress to facilitate the blog writing (it has very nice features
such as the automatic categories and blog archive).

This time we will exploring one of the most powerful things Scala offers as a
functional programming language. That is, of course, the functions, the core
concept in this paradigm.

This concept is quite important, and I'm sure I won't be able to explain the
full potential of Scala functions as I'm not a master in functional programming
paradigm. Yet, I'll do my best. However, it is important that you take a
tutorial or course on Scala's functional programming (I deeply recommend Martin
Odersky's [Functional Programming Principles in Scala](https://www.coursera.org/course/progfun)).

## Functions Basics

Scala functions are declared using the same reserved word that Python uses:
**def**. Like all Scala's control flow instructions, the scope of the function
is defined either by the immediate next instruction or by a block closed between
curly braces: **{** and **}**.

> I won't be able to explain the full potential of Scala functions as I'm not a
> master in functional programming paradigm. Yet, I'll do my best.

Functions in Scala are actually values assigned to a symbol (just like a **val**
or a **var**), so naturally they have a type. The type of a function is defined
as a list of parameters of some type returning a parameter of some type (can be
the same, can be different). In basic terms, this means that every parameter of
a function should have an explicit type (the system cannot infer the type on its
own and will throw an error if you don't declare it). But, they can have an
implicit returning type that the system can infer:

{% highlight scala %}
def add(x: Int, y: Int): Int = x + y // All good!

def pow2(x: Int) = x * x // Correct again. The system infer the returning type as Int

def substract(x, y) = x - y // Wrong. The system doesn't know the type of x and y
{% endhighlight %}

<!-- more -->

Pay attention in my last code. Every function define is followed by an equality
sign (**=**) and neither of them needed the **return** reserved word.

The equality sign is particularly important, it's the one that states the
function returns a value. If you forget it, then there are two options: You get
an error if the block is not marked with braces or the function doesn't have a
returning value. You'll also get an error if you impose it with a return
directive or give the function a return type:

{% highlight scala %}
def add(x: Int, y: Int): Int { x + y } // Wrong

def add(x: Int, y:Int) { return x + y } // Wrong

def add(x: Int, y: Int) x + y // Wrong

def add(x: Int, y: Int) { x + y } // It's not an error. But the function doesn't return a value when you apply it.
{% endhighlight %}

Functions that doesn't return a value have a special returning type called Unit,
but of course, you can just skip it.

Another important thing is that the reserved word **return**, that exists in
Scala and does the same thing as in Python is not necessary for functions in
order to return a value. In Scala the evaluation of the last expression or
instruction is the returned value of the function. Return is only necessary if
you want to force a return value in the middle of the function (which is not
very functional programming, but it can be done). Also, return requires to
explicit the returning value of the function.

## A Little on Recursion

This is a major area in functional programming. There are papers, articles and
books on this subject and I won't be able to do enough justice to it in just one
blog post. Basically, in real functional programming, all loops are written as
recursive functions (instead of using imperative instructions like **while** or
**for**).

A recursive function is a function that in order to give a result, solves a
simpler version of the same function (it calls itself recursively). Taking in
consideration the example given in the [Python Tutorial](https://docs.python.org/2/tutorial) in section 4.6, the Fibonacci
function example that takes a integer n and returns a list containing the
Fibonacci series up to _n_ (the one called fib2):

{% highlight python %}
>>> def fib2(n): # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
{% endhighlight %}

In Scala you can basically copy-paste the algorithm they show and twitch it a
little bit to get the same function:

{% highlight scala %}
import scala.collection.mutable.ListBuffer // The equivalent to Python's list

def fib(n: Int): List[Int] = {
  val result: ListBuffer[Int] = ListBuffer()
  var a = 0
  var b = 1
  var aux = 0 // Needed. Scala doesn't accept multiple variable assignment
  while (a < n) {
    result += a
    aux = a
    a = b
    b = b + aux
  }

  result.toList
}

fib(100) // Will return List(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
{% endhighlight %}

Now, as you could see there, there are a couple of difference between this and
the Python version. The main one resides in the use of a third auxiliary
variable, _aux_, as Scala doesn't support multiple assign over existing
variables, like the instruction: _a, b = b, a+b_. But on other ways is quite
similar to the Python algorithm.

However, if we want to make this a recursive function, a first approach to do
the same (although not an elegant one) can be represented by:

{% highlight scala %}
def fib(a: Int, b: Int, n: Int): List[Int] = { // The returning value is mandatory for recursive functions
  if (a > n) Nil
  else a :: fib(b, a+b, n)
}

fib(0, 1, 100) // Will return List(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
{% endhighlight %}

I guess the extra parameters are not really ideal, but you can see that in this
version we didn't need state, we didn't need to import the ListBuffer, we didn't
need the auxiliary variable and we even reduce the written code a lot. The only
sacrifice was to add two extra parameters.

The good thing about Scala (and I think you can also do this in Python as well,
but I'm not sure about it), is that you can define a function inside another
function, so, we can rewrite the last function taking advantage of this:

{% highlight scala %}
def fib(n: Int) = {
  def fibaux(a: Int, b: Int, n: Int): List[Int] = {
    if (a > n) Nil
    else a :: fibaux(b, a+b, n)
  }

  fibaux(0, 1, n)
}

fib(100) // Will return List(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
{% endhighlight %}

Nice, huh? In this new version we use a locally defined a _fibaux_ which
result's value we return as the value of the main _fib_ function. Then, we only
need to call fib with only one parameter just like in the imperative version
before and we still manage to save code writing (and avoid state). We can even
declare _fibaux_ without the _n_ parameter as it will take the _n_ parameter
from the fib function scope. But I think getting into that is way more than I'm
capable of explain: you should read something on
[scope](https://en.wikipedia.org/wiki/Scope_%28computer_science%29).

Recursion is a powerful resource. And is not easy to master. As everything in
programming, if it is correctly used, it will have lots of advantages, if it's
misused, well, you can guess the results: extreme resource consumption is most
probably what you'll be dealing with.

> Remember, recursion is a big deal in functional programming. There are
> papers, articles and books on this subject and I won't be able to do enough
> justice to it in just one blog post.

Well. I think that this is already enough for you to process before moving on
with a new post. Functions are the way to go in Scala. Don't take them for
granted, they are a core concept in the Scala world and can easily define how
good or bad as a Scala programmer you will be. We have some more topics to
discuss on functions before moving on some other subject, but I think this is
enough for today. I'm trying to keep this tutorials simple and concise.

As always, thank you for reading. All your feedback and comments are welcome.
