---
layout: post
title: "Adding Rutgers Ubuntu Mirrors"
date: 2013-09-26 12:37
published: true
---

Rutgers Open Systems Solutions [mirrors a bunch of Linux distributions](http://mirrors.rutgers.edu/), and you can use these to download packages quickly when you're on campus. When downloading on the Rutgers campus, your bandwidth will also not be throttled which significantly improves your download speeds.

### Adding a Mirror to Ubuntu

To add a mirror, open up your `/etc/apt/sources.list` file. 

```bash
sudo [editor] /etc/apt/sources.list
```

It should look something like this:

```
# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://us.archive.ubuntu.com/ubuntu/ [distrib] main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib] main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://us.archive.ubuntu.com/ubuntu/ [distrib]-updates main restricted
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib]-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://us.archive.ubuntu.com/ubuntu/ [distrib] universe
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib] universe
deb http://us.archive.ubuntu.com/ubuntu/ [distrib]-updates universe
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib]-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu 
## team, and may not be under a free licence. Please satisfy yourself as to 
## your rights to use the software. Also, please note that software in 
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://us.archive.ubuntu.com/ubuntu/ [distrib] multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib] multiverse
deb http://us.archive.ubuntu.com/ubuntu/ [distrib]-updates multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib]-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://us.archive.ubuntu.com/ubuntu/ [distrib]-backports main restricted universe multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ [distrib]-backports main restricted universe multiverse
...
```

`[distrib]` here is the name of your distribution. This is one of `natty`, `oneiric`, `precise`, `quantal`,  or `raring`. You can find a full list on the [Ubuntu Wikipedia Page](http://en.wikipedia.org/wiki/Ubuntu_(operating_system))

You are going to add the following lines at the *top of the file*.

```
deb http://mirrors.rutgers.edu/ubuntu [distrib] main restricted universe multiverse
deb http://mirrors.rutgers.edu/ubuntu [distrib]-updates main restricted universe multiverse
deb http://mirrors.rutgers.edu/ubuntu [distrib]-backports main restricted universe multiverse
deb http://mirrors.rutgers.edu/ubuntu [distrib]-security main restricted universe multiverse
```

Be sure to replace `[distrib]` with the name of your distribution. Now, save the file and quit, and run

```bash
sudo apt-get update
```

You should now be downloading packages from the Rutgers mirror. Try to install a package, and make sure that you're making requests to `http://mirrors.rutgers.edu`.
