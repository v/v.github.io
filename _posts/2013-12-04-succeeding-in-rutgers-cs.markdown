---
layout: post
title: "Succeeding in Rutgers Computer Science"
date: 2013-12-04
published: false
---

### Introduction

I'm a fifth year masters student in the Rutgers CS department, and I've interacted with students in introductory CS courses for over 3 years. I was a peer mentor for CS111 for 3 years (Fall 2011 to Spring 2013), and I've helped students with their assignments, and explained concepts to them a countless number of times.

I have met a wide range of students in the CS department that have succeeded and failed for various reasons. This blog post tries to explain these patterns for success and failure that I have noticed.

A good performance in the intro courses builds the foundation for your CS knowledge. Without it, you are as useful as a mathematician that cannot add fractions, or solve linear equations.

### Your performance in intro courses is incredibly important.

### Develop a good mental model of programming early in your coursework.

By the time you get through CS111, you should have a clear mental model of how problem solving is accomplished through code. It's easy to get distracted as a 111 student by the complexities of Java, Eclipse, jEdit, your weekly assignments, and course project. This is especially true if you come to 111 with no programming experience. It might feel like all you're doing is staying afloat week after week, assignment after assignment, milestone after milestone. Someone tells you that using Eclipse is good/bad. Someone tells you that you should put curly braces on the same line as a function, as opposed to putting it on its own line. It can be very overwhelming.

If at the end of 111, you are able to take a problem given to you, think about how it's solved, write code to solve it, and debug your code until it works, you have done well. This seems like a hard thing to measure, so I'm going to give you a couple of litmus tests to gauge your performance.

Consider the problem below:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Lemon` instead of the number and for the multiples of five print `Juice`. For numbers which are multiples of both three and five print `LemonJuice`.

Here is what the output of the program looks like from 1 to 20.

```
1
2
Lemon
3
Juice
Lemon
7
8
Lemon
Juice
11
Lemon
13
14
LemonJuice
16
17
Lemon
19
Juice
```

This problem should be a breeze for you after 111. If you cannot write code to solve this in 30 minutes, without someone's help, you are in serious trouble. You have a very poor chance of succeeding in further CS courses.

Here is another litmus test. If you can solve the first 5 problems on [Project Euler](http://projectuler.net) without any help, you have learned problem solving. You can start worrying about other things. If you can't do these problems, you need to spend more time learning to problem solve, writing code, and debugging code. You will not get very far in a CS degree before you do this.

You can write code to solve a Project Euler problem, and submit the solution by creating an account. This is also a great way to learn a new programming language (This is how I learned the basics of Python).

### Data Structures is incredibly important.

Data Structures develops on your understanding of problem solving from 111 and teaches you about clever ways in which programmers manipulate data, and algorithms.

1. You need to know Data Structures to write C code [CS211 - Computer Architecture, and CS214 - Systems Programming].
2. You need to know Data Structures to do well in Algorithms [CS344].
3. You need to know Data Structures to get through a tech interview.

You can ask any upperclassman what they think the most important CS course is, and Data Structures will unanimously be their top 3.

#### The Story of 50% of the students in CS112

Now, let me tell you the story of Alice. Alice is a metaphorical student that represents 50% of the CS112 roster.

Alice took CS111, did fairly well in it (got better than a B). In 111, Alice often found it hard to listen to the professor in lecture. Every once in a while, she zoned out, and couldn't figure out what Tjang or Sesh was saying. She went home, looked at the weekly assignment, and finished it (perhaps with some help from a friend, TA, or someone at the iLabs). Since every concept in lecture was reinforced in a weekly assignment, she understood most of the material that was covered in 111.

When Alice took 112, she followed a similar path. Tjang/Sesh was lecturing about Heaps, Linked Lists, Graphs, Tail Recursion, Efficiency Analysis of Insertion Sort etc. She went on Facebook on her laptop/got a text from a roommate, subequently zoned out in class, and quickly lost track of what the professor was saying. Alice went home, there was a project due in two weeks. Alice worked very hard on the project. She definitely had some issues along the way, but she was able to ask Sesh/TAs/peers/people at the iLabs for help and get it done. She got an 85+ on all the 5 projects in CS112. Alice got around a 50 on both Data Structures exams, ended Data Structures with a C/C+, and moved on.

Alice is the canonical example of a student that does poorly in the Rutgers CS degree, and here's why.

In 111, Alice had projects every week that forced her to learn material. The only thing in 112 that forces you to learn material in the exam, and that happens twice a semester. Sometimes, the first 112 exam is so early in the semester that there's very little material covered on it. This means that the final covers a ton of material, and because Alice has been zoning out of 112 lecture on a regular basis, she does not know why Heapify is O(n), or why you would want to use a min heap as a frontier when implmenting Dijkstra's shortest path algorithm.

In order to avoid Alice's pitfalls, you need to *make sure that you understand every concept in Data Structures*. Practically every sentence that Sesh or Tjang says in 112 is important. I understand that you are human, and cannot keep perfect concentration in an 80 minute lecture. But you need to be proactive about understanding all the concepts that are covered. This means that if zoned out in the lecture about AVL Trees, you still need to make sure you learn it. You can go read the textbook after class. You can look up the material online. There's some [very good online courses that cover data structures](http://see.stanford.edu/see/courseinfo.aspx?coll=11f4f422-5670-4b4c-889c-008262e09e4e). You can ask me or another upperclassman to explain the concept to you.

You need to do this before the day of your data structures exam, because the course covers *a lot of important material*, and you cannot learn all of it in a day.

### When picking classes, the only thing that matters is the quality of the professor teaching the course.

### When learning concepts in a class, you should very clearly understand why the concept is important.

### If you are not branching out from the material you learn in class, you will have a hard time getting hired as a developer.

### Always have an idea of what your learning progression 
