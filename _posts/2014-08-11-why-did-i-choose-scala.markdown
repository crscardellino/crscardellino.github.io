---
layout: post
title: "Why Did I Choose Scala?"
date: 2014-08-11 20:53:00 +0200
tags: course python scala tutorial
---

So, on this entry I'll put a halt on the series of tutorials I've been writing.
Instead I think it's time to give a personal opinion in why did I choose
[Scala](http://scala-lang.org/) as my new main language.

Before keep going on this, I'll just state that this is a complete personal
opinion on Scala, is completely subjective. The reason why I chose it is mine
and doesn't have to be your reason to choose it, but maybe you'll find some
useful insights on what advantages I think the language has.

So, a couple of friends and co-workers asked me "Why Scala over Python? (or any
other language for that matter)", I guess I've never answered with a full
justification on why did I do it. Actually, I don't think I have a real or valid
justification more than "because I liked it", but I do want to state some stuff
that end up with me switching from a Python programmer to a Scala programmer.

<!-- more -->

#### I got bored

I don't think this counts as a real "advantage", but it's definitely one of the
main reasons. Before Scala I was a Python programmer for 4 years, and I just got
bored. Programming in Python wasn't fun anymore, wasn't challenging enough.
Don't take this the wrong way, it's not that I've learnt everything I could in
Python, that's completely ridiculous, I'm as far as learning or using all that
Python has to offer as I can get. But, somehow, I wasn't interested in learning
new things in Python.

Maybe was the fact that in the Zen of Python "There should be one– and
preferably only one –obvious way to do it", which is a great way but not fun
enough for me. But probably was the mere fact that 4 years with the same
language was far more than what I wanted.

Nonetheless, I don't regret knowing Python, is still a wonderful language to
learn, specially for a starter programmer. Simple and plain, easy to read even
if you coded it years ago.

And of course, with these I'm not saying Scala is better than Python, nor is
that my intention. Scala and Python are just different, they offer different
things and provide different ways for programming.

#### Functional Programming

Scala is a multi-paradigm language. It can be used with an imperative language
orientation (much like Java, C++ or Python), but it's designed with the idea of
functional programming in it's core.

Functional programming is something very different from imperative programming,
and probably is not as natural as the latter. Is a paradigm harder to learn and
even harder to master (at least from my point of view). And in general term has
always been associated with the academia (with LISP or Haskell as references).
However, when you start to use this paradigm, is extremely good in dealing with
many issues, specially nowadays. For example, functional programming languages
can handle concurrency like no other languages as they are stateless. Other nice
features include the always useful pattern matching and the extremely powerful
high-order functions.

There is a good article called [Functional Programming For The Rest Of
Us](http://www.defmacro.org/ramblings/fp.html). Take a look at it, it's an
interesting read.

I learned the functional programming paradigm in the university, in my first
courses of algorithms and data structures. Back then I used Haskell and to be
honest I hated it. It wasn't clear for me, it made me have headaches. But, I
guess that with time I became mature enough to know the advantages of this
paradigm.

You can tell me, if I like functional programming, why not LISP or Haskell then?
Real purely functional programming languages. And it's as simple as saying, it's
still not natural for me to use a purely functional language, it would take me
too much time to code some functionalities. That's why I prefer Scala, because,
if I don't know how to do something in the functional way I still can do it in
the imperative way. It's not the cleanest solution, I know, but when
experimenting, it's a solution. Then I can try to arrange it so it's either all
functional or all imperative.

Besides, after years of imperative programming in Python, it's smoother to jump
to a language that allows me to do things the way I used to do them instead of a
language that makes me learn new ways for everything. Once I've mastered Scala I
can jump to something more pure in the functional paradigm (that is, if Scala
cannot accomplish it, which I doubt).

Finally, Scala, as a functional language, has been given the tools necessary to
go [reactive](http://www.reactivemanifesto.org/), making concurrency and
distribution easier and giving a nice and elegant way to asynchronous
programming.

#### Static Types

If there is a thing that Python lacks of are static types. Of course, this is a
matter of pure perspective, since for some people this is an advantage of
Python. You don't have to deal with variable types so it's a weight you take off
your back.

This, however, is not the case for me. At the beginning I thought dynamic typing
was a great feature, you could make reuse of variables without having to deal
with them being already used. But, as I experienced in some codes I did across
my time as Python coder, I realized most of the time is good to have a registry
on what are the variables you are using and the type they have on them.
Specially when I dealt with experimentations in Natural Language.

Still, the great thing that Scala has over static typed languages (think Java
for example), is the fact that it packs a type inferrer. This makes the coding
much easier and far less verbose than a Java application. Like it's presented in
the [Scala Website](http://scala-lang.org/): Don't work for the type system. Let
the type system work for you.

After years of dynamic typing, I come back once again to the good old static
typing, and I'm happy with it.

#### Compilation to JVM

Scala compiles over the JVM, that's why it's called a JVM language (just like
Jython, Clojure, Groovy or JRuby).

This compilation to Java bytecode gives Scala a couple of nice features. The
very first is speed, as it compiles to something nearer to object code (and
thus near to machine code), a typical Scala application is only [2 or 3
times](http://benchmarksgame.alioth.debian.org/u32/which-programs-are-fastest.php)
slower than a C application, whereas a Python application can be up to [50
times
slower](http://benchmarksgame.alioth.debian.org/u32/which-programs-are-fastest.php)
than a C application.

The second great feature resides in its seamless interoperation with Java. As it
is stated in the [Scala Website](http://scala-lang.org/): "Scala classes are
ultimately JVM classes. You can create Java objects, call their methods and
inherit from Java classes transparently from Scala. Similarly, Java code can
reference Scala classes and objects.

In general terms, this is a very big deal. Why? It's simple, because Java has
been an industrial standard for years now, and that translated in hundred if not
thousands of useful libraries written for Java that are completely useful for
building Scala applications.

A programming language is as powerful as the libraries it has to back it up
(that's precicely why Java and C++ are top choices in the market). The more
libraries, the less code you have to rewrite (an important principle in
programming is to never reinvent the wheel). Scala is growing in libraries
everyday, but the collection probably is not as large as Python's. However, Java
libraries' collection is as large (and probably even larger) as Python's
collection, and the fact that this are useful for Scala programs as well give a
Scala a great advantage over many other new languages.

If you are asking, ok but, why not use Java then? Simple, I've never been a Java
enthusiast, and although I respect the contribution it has given to the
programming environment, I still prefer the less verbose code of Scala, and then
again, Java is not a functional programming language.

#### A Cool Kid

Finally, the last reason I choose Scala as new toy to play with. In the last
years, Scala community has grown a lot, and it's in part because is a new
technology or, a more slang way to say it: "it's what cool kids are doing".

Ok, maybe "cool kid" is way too arrogant to state it. Still, what I mean is that
a big generation of early adopters in programming languages has been turning
into one of these two new technologies these last couple of years: JavaScript,
commonly a client-side language to give web applications a little more
"dynamic", has been increasing in usability since the launch of NodeJS (another
new tool I'm interested in), using the JavaScript V8 engine to build side-server
JavaScript applications; And the other one is Scala, with the reactive
programming manifesto and the easiness in coding asynchronous applications.

Personally, I've never been an early adopter, I've always preferred a good old
fashion stable Debian OS over a fancy latest model Ubuntu. But, as I stated
before, I got bored, and as a result of that, I wanted to learn something new,
something different, and Scala has been so far a smooth ride.

That's all I had to say about this. I hope you liked my insight on this
beautiful language and my post leads you to learn it. If you really put yourself
into it you'll find out the potential of this language is excellent and you
won't be regretted in adopting Scala.

Thank you for reading.
