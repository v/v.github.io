---
layout: post
title: "Use PDSH to shell into multiple hosts via SSH"
date: 2014-01-26 13:40"
published: true
---

SSH is a powerful protocol that lets you access machines remotely and run commands on them. Rutgers has a [cluster of linux machines for CS students](http://ilab.rutgers.edu), and I often run programs on them. Sometimes, I leave a program running for a while, and forget which machine it was on. In this situation, PDSH comes in handy. It lets me run `ps aux | grep -i <username>` quickly across all the machines.

### PDSH - Run SSH in Parallel

PDSH lets you run a command in parallel across a bunch of machines. I start by creating a text file with a list of machines I want to shell into:

```
cd.cs.rutgers.edu
cp.cs.rutgers.edu
grep.cs.rutgers.edu
kill.cs.rutgers.edu
less.cs.rutgers.edu
ls.cs.rutgers.edu
man.cs.rutgers.edu
pwd.cs.rutgers.edu
rm.cs.rutgers.edu
top.cs.rutgers.edu
vi.cs.rutgers.edu
cpp.cs.rutgers.edu
java.cs.rutgers.edu
perl.cs.rutgers.edu
basic.cs.rutgers.edu
assembly.cs.rutgers.edu
pascal.cs.rutgers.edu
php.cs.rutgers.edu
lisp.cs.rutgers.edu
prolog.cs.rutgers.edu
adapter.cs.rutgers.edu
command.cs.rutgers.edu
decorator.cs.rutgers.edu
facade.cs.rutgers.edu
flyweight.cs.rutgers.edu
mediator.cs.rutgers.edu
patterns.cs.rutgers.edu
singleton.cs.rutgers.edu
state.cs.rutgers.edu
template.cs.rutgers.edu
visitor.cs.rutgers.edu
builder.cs.rutgers.edu
composite.cs.rutgers.edu
design.cs.rutgers.edu
factory.cs.rutgers.edu
interpreter.cs.rutgers.edu
null.cs.rutgers.edu
prototype.cs.rutgers.edu
specification.cs.rutgers.edu
strategy.cs.rutgers.edu
utility.cs.rutgers.edu
```

Let's say I save this file as `machines.txt`. I can then run a command in parallel across all these machines:

```bash
$ pdsh -R ssh -w ^machines "<command>"
```

Here are some things you can do with PDSH that you might find useful

Find all python processes running on these machines.
``` 
$ pdsh -R ssh -w ^machines "ps aux | grep -i python" ```

Kill any processes being run by my user. (Super useful if you forget to log out of a lab machine.)
``` 
$ pdsh -R ssh -w ^machines "killall -u `whoami`" ```

Check a specific log file for errors.
``` 
$ pdsh -R ssh -w ^machines "grep -i error /path/to/log" ```

It's a handy UNIX tool to have in your arsenal when working with lots of machines. Clearly, I am only showing the usage of `pdsh` in the most basic way. Check out [PDSH on Google Code](https://code.google.com/p/pdsh/) for a more detailed description of everything PDSH can do.
