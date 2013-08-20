---
layout: post
title: "Using git hooks to deploy your web application"
date: 2013-08-09 19:12
published: true
---

Often times when building web applications, I used to spend time deploying my web applications via `ssh` and `scp`. Then I used [Heroku](http://heroku.com) for a few projects, and I really liked that deploying to heroku was as easy as it could be.
{% highlight bash %}
    git push heroku master
{% endhighlight %}

I wanted to have a similar deployment scheme on my own projects that aren't deployed on Heroku.

### Setting it up

Before you start, your codebase needs to be in a git repository. This could be a Github repository that you use for version control. I will assume that your codebase lives in one directory called `project` on your development machine, which I will refer to as `develop`.

This codebase will be deployed to your server. I will refer to your server as `deploy`.

Now, you are going to create a bare git repository on `deploy`, and you will be able to push to it from `develop`.

```bash
username@deploy:~$ mkdir repos # this is the dir where all your repos will be stored.
username@deploy:~$ cd repos
username@deploy:~/repos$ mkdir project.git 
username@deploy:~/repos$ cd project.git # You can replace this with the name of your project.
username@deploy:~/repos/project.git$ git init --bare
# Initialized empty Git repository in /home/username/repos/project.git
```

You will now set up your codebase on `develop` to push to the repos/project.git directory on `deploy`.

```bash
username@develop:~$ cd /path/to/my/project
username@develop:~/code/project$ git status 
# This must be a git repo.
username@develop:~/code/project$ git remote add deploy username@deploy:~/repos/project.git # This is the path to your bare repo.
username@develop:~/code/project$ git push deploy master 
```

This will push your codebase, to the bare repository you just created on `deploy`. You can verify this by cloning the bare repository if you'd like.

```bash
username@develop:~$ cd /tmp
username@develop:/tmp$ git clone username@deploy:~/repos/project.git
# Cloning into 'project'...
# remote: Counting objects: 666, done.
# remote: Compressing objects: 100% (417/417), done.
# remote: Total 666 (delta 255), reused 632 (delta 221)
# Receiving objects: 100% (666/666), 621.96 KiB | 462 KiB/s, done.
# Resolving deltas: 100% (255/255), done.
username@develop:/tmp$ cd project
username@develop:/tmp$ ls
# make sure your files are here.
```

Now that we are pushing to the repos/project.git directory on `deploy`. Let's set up our repository to actually deploy its code. I'll assume that your application gets deployed to `/var/www/myproject.com` . 

```bash
username@deploy:~$ cd repos/project.git
username@deploy:~$ ls
# HEAD  branches  config  description  hooks  info  objects  refs
username@deploy:~$ cd hooks
username@deploy:~$ [editor] post-receive
```

The post-receive hook gets called by git right after code gets pushed to a repository (right after git push deploy master). We will make this hook deploy your application to `/var/www/myproject.com` . Using an editor of your choice, place the following in the post-receive file.

```bash
#!/bin/bash

### This file gets run when code is pushed to the project.git directory.

GIT_WORK_TREE=/var/www/myproject.com git checkout -f
```

Make the hook executable.

```bash
username@deploy:~/repos/project.git/hooks$ chmod +x post-receive
```

Make sure that your user has permissions to write to `/var/www/myproject.com`. This is it! You can now deploy your code anytime you want by running:

```bash
username@develop:~/code/project$ git push deploy master
```

Verify that your code is deployed when you push, and you should never need to use `scp` to deploy ever again.
