---
layout: post
title: "Succeeding in Rutgers Computer Science"
date: 2015-06-12
published: true
---

I spent 5 years in the Computer Science BS-MS program. I was a peer mentor for CS111 for 3 years.

I've met a wide range of students in the CS department. I've helped students with assignments, and explained concepts to them over and over again. This blog post explains the patterns for success and failure that I have noticed.

### Your performance in intro courses is incredibly important. Develop a good mental model of programming early in your coursework.

A good performance in the intro courses builds the foundation for your CS knowledge. Without it, you are as useful as a mathematician that cannot add fractions, or solve linear equations.

By the time you get through CS111, you should have a clear mental model of how problem solving is accomplished through code. It's easy to get distracted as a 111 student by the complexities of Java, Eclipse, jEdit, your weekly assignments, and course project. This is especially true if you come to 111 with no programming experience. It might feel like all you're doing is staying afloat week after week, assignment after assignment, milestone after milestone. Someone tells you that using Eclipse is good/bad. Someone tells you that you should put curly braces on the same line as a function, as opposed to putting it on its own line. It can be very overwhelming.

If at the end of 111, you are able to take a problem given to you, think about how it's solved, write code to solve it, and debug your code until it works, you have done well. This seems like a hard thing to measure, so I'm going to give you a couple of litmus tests to gauge your performance.

Consider the problem below:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Lemon` instead of the number and for the multiples of five print `Juice`. For numbers which are multiples of both three and five print `LemonJuice`.

Here is what the output of the program looks like from 1 to 20.

```
1
2
Lemon
4
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

This problem should be a breeze for you after 111. If you cannot write code to solve this in 30 minutes, without someone's help, you are in trouble.

Here is another litmus test. If you can solve the first 5 problems on [Project Euler](http://projecteuler.net) without any help, you have learned problem solving. You can start worrying about other things. If you can't do these problems, you need to spend more time learning to problem solve, writing code, and debugging code. You will not get very far in a CS degree before you do this.

You can write code to solve a Project Euler problem, and submit the solution by creating an account. This is also a great way to learn a new programming language (This is how I learned the basics of Python).

### Data Structures is incredibly important.

Data Structures develops on your understanding of problem solving from 111 and teaches you about clever ways in which programmers manipulate data, and algorithms.

1. You need to know Data Structures to write C code (CS211 - Computer Architecture, and CS214 - Systems Programming).
2. You need to know Data Structures to do well in Algorithms (CS344).
3. You need to know Data Structures to get through a tech interview.

You can ask any upperclassman what they think the most important CS course is, and Data Structures will almost certainly be one of their top 3.

#### The Story of 50% of the students in CS112

Now, let me tell you the story of Alice. Alice is a metaphorical student that represents 50% of the CS112 roster.

Alice took CS111, did fairly well in it (got better than a B). In 111, Alice often found it hard to listen to the professor in lecture. Every once in a while, she zoned out, and couldn't figure out what Tjang or Sesh was saying. She went home, looked at the weekly assignment, and finished it (perhaps with some help from a friend, TA, or someone at the iLabs). Since every concept in lecture was reinforced in a weekly assignment, she understood most of the material that was covered in 111.

When Alice took 112, she followed a similar path. Tjang/Sesh was lecturing about Heaps, Linked Lists, Graphs, Tail Recursion, Efficiency Analysis of Insertion Sort etc. She went on Facebook on her laptop/got a text from a roommate, subequently zoned out in class, and quickly lost track of what the professor was saying. Alice went home, there was a project due in two weeks. Alice worked very hard on the project. She definitely had some issues along the way, but she was able to ask Sesh/TAs/peers/people at the iLabs for help and get it done. She got an 85+ on all the 5 projects in CS112. Alice got around a 50 on both Data Structures exams, ended Data Structures with a C/C+, and moved on.

Alice is the canonical example of a student that does poorly in the Rutgers CS degree, and here's why.

In 111, Alice had projects every week that forced her to learn material. The only thing in 112 that forces you to learn material is the exam, and that happens twice a semester. Sometimes, the first 112 exam is so early in the semester that there's very little material covered on it. This means that the final covers a ton of material, and because Alice has been zoning out of 112 lecture on a regular basis, she does not know why Heapify is O(n), or why you would want to use a min heap as a frontier when implmenting Dijkstra's shortest path algorithm.

In order to avoid Alice's pitfalls, you need to *make sure that you understand every concept in Data Structures*. Practically every sentence that Sesh or Tjang says in 112 is important. I understand that you are human, and cannot keep perfect concentration in an 80 minute lecture. But you need to be proactive about understanding all the concepts that are covered. This means that if you zoned out in the lecture about AVL Trees, you still need to make sure you learn it. You can go read the textbook after class. You can look up the material online. There's some very good online courses that cover data structures. I strongly recommend the [lectures from Stanford's Programming Abstractions course](https://www.youtube.com/watch?v=kMzH3tfP6f8&list=PLFE6E58F856038C69). You can ask upperclassmen to explain the concept to you.

You need to do this before the day of your data structures exam, because the course covers *a lot of important material*, and you cannot learn all of it in a day.

### Pick classes carefully, especially after the intro sequence.

1. Pay close attention to the professor that's teaching the class.
    - Don't take a class just because the professor is easy. By doing this, you are learning nothing, and wasting both time and tuition dollars.
    - Understand that a lot of the professors teaching you haven't written a line of code in 15+ years. They cannot and will not teach you web or mobile app development. If they attempt to teach you this stuff, their material will likely be outdated and poorly researched. 
    - The theoretical classes are challenging and will require mental discipline. I highly recommend everything being taught by [Martin Farach-Colton](http://www.cs.rutgers.edu/~farach), [William Steiger](http://www.cs.rutgers.edu/~farach), or [Eric Allender](http://www.cs.rutgers.edu/~allender). These were my favorite professors. Their classes were engaging, memorable, and had challenging material.
2. Prerequisites don't matter. 
    - If you've done well in 111, 112, 211 and 205, you can take **any** other class in the department - *even a graduate class*.
    - Do you see [Uli Kremer](http://www.cs.rutgers.edu/~uli) (an excellent compilers professor) teaching next semester? Take his class even though you haven't taken 314.
    - But V! I'm not smart. Everyone in this class is going to have an edge on me. I'm going to get a bad grade, lose my scholarship, and end up on the streets. Here's what I have to say to this - 50% of the people taking a class don't learn a thing. At the end of CS112, I want you to ask 10 of your classmates if they can implement a hash table. At the beginning of 211 and 214, I want you to look around you as they struggle to implement one in C. They're not learning in 112, and they're not learning in the prerequisite courses that you want to skip. They will have no edge over you.
    - You will feel more challenged in a course if you take it without a prerequisite, but as long as you're proactive about brushing up on material you don't know, you'll do just fine.
    - Logistics - you can't register for a course on webreg if you haven't taken the prereqs. Send the prof an email to get a prereq override - tell them you're interested in the material, and you'll put extra time and learn stuff you don't know.

3. Stop focusing on grades. Focus on concepts you're learning
    - The classes I loved the most were the ones in which I was engaged by the professor's lectures and assignments. 
    - I took Operating Systems with a smart but boring professor. I was not engaged in lecture, but his assignments, exams were easy so I got an A. I regret wasting my time, because my grade did not reflect my knowledge of OS.
    - I have friends that took OS with [Ricardo Bianchinni](http://www.cs.rutgers.edu/~ricardo). Their assignments and exams were much harder, and they spent much more time on coursework. Most of them did not get As - but they learned far more about OS than I did.
    - If your goal is to learn OS, don't waste your time in a course that doesn't teach you OS.
    - If your goal is to get a piece of paper with your name on it, and "Bachelors in Computer Science" under it, this advice isn't for you. I loved learning about the hard problems in computer science from incredibly smart people that were experts in these fields.

### If you are not branching out from the material you learn in class, you will have a hard time getting hired as a developer.

Your professors haven't written code in 15+ years. They're not going to teach you how to develop software - don't waste your time taking CS431.

Start writing code in your free time to solve **any problem** that you have. I wrote [RUBUS](http://oss.rutgers.edu/rubus/) when I was in 112. I used to maintain [static web pages](http://eden.rutgers.edu/~vverna/) for a board game my roommate played with his high school friends. Everyone that's good at programming has put in lots of time into it, and you will need to do the same.

Talk to upperclassmen about ideas you have, and the things that they've built. Hang out in the CAVE, attend USACS events, and go to hackathons. All of this experience will add up, and help you land your first paid programming gig.

### Get paid to write code as early as possible.

When I started taking CS classes, I didn't understand why people got paid to sit at a computer and write for-loops. I thought the mysterious, legendary developers getting internships and part time jobs must **know so much more** about the web/mobile apps/algorithms. This is a classic case of impostor syndrome, and it creates a mental roadblock until you get paid to write code.

Use your summers for internships or part time work ([not for folding clothes](http://www.joelonsoftware.com/articles/CollegeAdvice.html)). For your first development job, I recommend [Student System Administration at OSS](http://oss.rutgers.edu), [System Administration at LCSR (under Doug Motto)](http://lcsr.rutgers.edu), [an internship at Too Much Media](http://toomuchmedia.com/), or [HackNY if you are lucky](http://hackny.org/). You'll want to do a more traditional tech internship at companies like Microsoft, Google or Etsy, but you'll have an easier time getting these once you have some experience. If you hang around CS folks, you'll hear about such opportunities frequently. Apply early and often - you'll have an easier time in October than in April.

### Participate in the community

The Rutgers CS community, while not perfect, [has grown a great deal over the last few years](https://medium.com/@maltzj/from-0-350-in-three-years-991501eba5c7). You've got access to events like HackRU, HackNY, PennApps, and HackTCNJ. You've got access to the CAVE and the Hackerspace. USACS, RuMAD and the Rutgers Hackathon Club are active, and full of smart people. People taking the same classes as you have gone on to [amazing jobs](https://docs.google.com/spreadsheets/d/1LQDJuN2G8JKGIeqiQPtRVQochu9uyGcCt_SrTHEtGnc/edit#gid=0), [start companies](https://comminfo.rutgers.edu/news/iti-alum-transforms-from-self-taught-hacker-to-co-founder-of-the-hacker-league.html), and [sell companies](http://techcrunch.com/2013/12/03/hacker-league-mashery-intel/). Start reading [hacker news](http://news.ycombinator.com/), and [/r/programming](http://reddit.com/r/programming).


Don't forget to give back to the community. Teach CS111 recitation. Join the USACS board, and help plan events. Hang out at the CAVE and help underclassmen understand difficult concepts. Help the noobs out at hackathons.

Make friends out of your peers. [Impossible looking homework assignments](http://vverma.net/static/cs509_hw.pdf) will become easier. You'll spend a silly amount of time [working on a CTF challenge](https://github.com/stripe-ctf/stripe-ctf-2.0), or [writing a game](http://sia.github.io/game/). You'll get [one letter](http://github.com/v) [Github](http://github.com/x) [usernames](http://github.com/k) together. After college, they'll help you find jobs and offer you their couches.

Rutgers is a great place to study Computer Science, and I hope your time there will be as memorable as mine was.
