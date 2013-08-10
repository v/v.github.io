---
layout: post
title: "Using git hooks to deploy your web application"
date: 2013-08-09 19:12
published: false
---

Often times when building web applications, I used to spend time deploying my web applications via ssh and scp. Then I used [Heroku](http://heroku.com) for a few projects, and I really liked that deploying to heroku was as easy as it could be.
{% highlight bash %}
    git push heroku master
{% endhighlight %}

I wanted to have a similar deployment scheme on my own projects that aren't deployed on Heroku.

### Setting it up

Before you start, your codebase needs to be in a git repository. This could be a Github repository that you use for version control. I will assume that your codebase lives your development machine, which I will refer to as **develop**. 

This codebase will be deployed to your server. I will refer to this as **deploy**.

Now, we are going to create a bare git repository on **deploy**, and you will be able to push to it from **develop**.
