---
layout: post
title: "From Python to Scala (V): Control Flow Tools"
date: 2014-08-20 20:58:00 +0200
comments: true
categories: [course, python, scala, tutorial]
---

Ok, after a short period of laziness, I come back for more. I warned you about
my activity, but, to be fair, it's been a busy couple of weeks at work.

However, before starting, I wanted you to know that there is an upcoming Course
for Functional Programming Principles in Scala in 25 days (starts on September
15th). You can find more information about it (or even enroll in it) at
[Coursera](https://www.coursera.org/course/progfun). The course is in charge of
Martin Odersky, the creator of Scala, so you are in good hands.

So, back to business. On this session let's talk about some more real
programming.

### Control Flow Tools

#### The if statement

The most basic and probably the most well known statement in programming, the
conditional control flow:

``` scala
val x: Int = 10

if (x < 0)
  println("x is Negative")
else if (x > 0)
  println("x is Positive")
else
  println("x is Zero")

// Will return: "x is Positive"
```

<!-- more -->

Very basic, right? So, what are the differences with Python's **if**?

For starter, the indentation is not actually necessary, it is used for better
reading, but you can put everything with the same indent. Actually, it's even
possible to make an if statement at the same line. But, it is important to
remark, as it dos not holds a colon to delimit the end of the boolean expression
to value, it does needs the parentheses to delimit it.

You can also see that there is no **elif** but you just start another **if**
after the **else**.

``` scala
val x = -1

if (x < 0) println("x is Negative") else if (x > 0) println("x is Positive") else println("x is Zero")

// Will return: "x is Negative"

if x < 0 println("x is Negative") // Invalid, will result in error.
```

The blocking delimiter in an if statement can be nothing as long as there is
only one instruction after the if or the else, or can be the curly braces: **{**
and **}**:

``` scala
val x = -2

if (x > 0) {
  println("x is Positive.")

  val y = x * 2

  println("The double of x is: " + y)
}
```

This programs obviously prints nothing. But if it doesn't have the curly braces
to delimit the if statement, the results would be:

``` plain
The double of x is: -4
```

This happens because when and if lacks curly braces it only takes the immediate
next statement as its body.

#### Loop statements

There are three types of loops in Scala: **while**, **do...while** and **for**.

The statements **while** and **do...while** are very similar. The two of them
execute a set of instructions multiple times until the condition they hold is
false. Much like Python's **while**.

Still, the same as with the **if** statement, the delimiter is either the
immediate next instruction or it is delimited by curly braces.

The main difference between **while** and **do...while**, is that the latter
executes what is inside the block of instructions at least once after checking
on the breaking instruction:

``` scala
var x = 10

while (x > 0) {
  println("The value of x is: " + x)
  x -= 1
}

// Will print successively the value of x until x equals 0

x = 10

do {
  println("The value of x is: " + x)
} while (x > 0)

// Exactly the same

x = 0

while (x > 0) {
  println("The value of x is: " + x)
  x -= 1
}

// Doesn't print anything. The value of x is 0 at the end of the loop.

x = 0

do {
  println("The value of x is: " + x)
  x -= 1
} while (x > 0)

// Prints: "The value of x is: 0" and finish. The value of x is -1 at the end of the loop.
```

The for statement, as much as in Python, is useful for traversing Lists or
Arrays. It's also useful for list comprehensions. These are a very powerful
tools in functional programming, that actually Python also supports (check on
them if you are not familiar with it).

``` scala
val xs: List[Int] = List(1, 2, 3, 4, 5)

for (x <- xs) println(x) // Prints the values of xs, from 1 to 5

val ys: List[Int] = for (x <- xs) yield x * x

// The list ys holds the squares of every value in xs: 1, 4, 9, 16, 25

val zs: List[Int] = for (x <- xs if x % 2 == 0) yield x / 2

// The list zs has the half-values of the pairs in xs: 1, 2
```

If you check on the **yield** instruction, this means that it will return the
result of the next operation as a value. Also, you can use the **if** statement
inside a **for** to set a filter for the values to go through.

The statement after yield can be anything that returns a value, so it can be a
function created before, or even a block (that is actually a function, but let's
not get into that for now) with a returning value at the end:

``` scala
val xs = List(1, 2, 3, 4, 5)

val ys = for (x <- xs) yield {
  // A lot of different operations over x, stored in a variable called "result"
  result
}
```

As an ending note on Scala loops, there is no direct control over the loop, I
mean, there is no **break**, **continue** or (may God have mercy on me for this
forbidden word) **goto**. When a loop starts there is no easy way to make it
break or jump on a cycle (you can set an if inside as well as other kinds of
workarounds).

The thing with Scala is, that if you need to mess with the natural flow of a
loop, maybe there is another and cleaner way to do it.

#### The range equivalent (to and until)

If you come from Python, you are surely familiar with the **range** function,
and maybe with the **xrange** function which is a lazy iterator.

In Scala there is a similar way to declare a range, the **to** operator:

``` scala
val xs = 0 to 10

// xs now holds a immutable Range object that goes from 0 to 10
```

The main difference with this an Python's **range**, is that with the **to**
operator you always need the lower boundary: this means there is not equivalent
to **range(10)** for example. And, the resulting range, holds both boundaries:
in our example 0 and 10 are part of the resulting Range object, whereas in
Python, the upper boundary is not in the resulting list. If you want a range
without taking in consideration the upper boundary, you can have it with the
**until** operator:

``` scala
val xs = 0 until 10

// xs holds a Range that goes from 0 to 9

for (x <- 0 until 10) println(x) // Will print all the numbers from 0 to 9
```

As you could see in the last examples, the **until** (as well as the **to**)
operator, can be used directly in a for loop to create a range to loop over it.

### The pass equivalent

For the last of today's post, I'll make a brief reference to Python's **pass**
Scala equivalent. There is none, as simple as that, in Scala if you don't want
to do something you just leave a blank space (as long as it is clear that there
is a blank statement):

``` scala
class EmptyClass // Is valid

for (x <- 0 until 10) {} // Will go through the for without doing anything

for (x <- 0 until 10) // Wrong, it's ambiguous where the the blank statement is
```

Ok. I think this is more than enough for today. We learned some of the most
common control flow structures on Scala. Go and experiment by yourselves now. As
always, don't hesitate to leave your comments.

Thank you for reading. See you soon!
