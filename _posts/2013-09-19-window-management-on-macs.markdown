---
layout: post
title: "Keyboard Focused Development Workflow on Macs"
date: 2013-09-19
published: false
---

Having used Linux almost exclusively for the last four years, I miss efficient window management on Macs. Coming from the [awesome window manager](http://awesome.naquadah.org/), I find that OS X does not have good support for a two monitor multiple workspace workflow out of the box. After tinkering with third party software, I believe I've found a good solution for most of my complaints, and have a workflow that I feel productive with. In my experience, this works best with multiple monitors, a standard keyboard (think Dell not Apple), and a three button mouse (I'm not a fan of touchpads or Apple mice).

### Setting up Multiple Desktops

I really like the use of multiple desktops in my workflow. I usually set up four desktops. I keep [Spotify](http://spotify.com) open on the very last one. The middle ones are my "work" desktops that I use for terminals, browsers, IDEs, and documentation. The first one is usually a "distraction workspace" that will have my email, and [Adium](http://adium.com) open. This helps me keep my windows organized, and keep focus when I need to.

In order to set this up, I add additional desktops (up to 4). The easiest way to do this is to open up `Mission Control` (usually Control-Up), hover over the Desktops, and click the Plus button on the top right.

Once this is done, I would recommend setting up easy keybindings to switch between desktops. To do this, you go to `System Preferences > Keyboard > Keyboard Shortcuts > Mission Control`. Then you can set up keybindings for `Move left a space`, `Move right a space`, ... `Switch to Desktop 1-4`. I use `Ctrl-Alt-Left/Right` to move between desktops, and use `Command-1/2/3/4` to jump to a desktop.

### Using Slate for Window Management

On OS X, it's sometimes pretty cumbersome to perform window management tasks like moving windows between monitors, and maximizing windows efficiently. This is where Slate comes in. [Slate](http://github.com/jigish/slate) is a configurable third-party window management application, that makes these window management tasks super easy. I will explain how I use Slate day-to-day. 

#### Setting it up

You can install Slate, pretty simply by downloading the [Slate dmg](). After installing and starting Slate, you will want to make sure it's properly configured.

Here is my `~/.slate` configuration file that describes the keybindings I use with it. Right click on the Slate icon in the topbar > `Reload Config`, to apply configuration changes. 

```python
# Save this in ~/.slate
# This configuration file came from http://vverma.net. 
# Credit to Gerard O'Neill, http://goneill.net for introducing me to Slate.


# Half Screens.


# Maximize Window


# Move windows between monitors.


### I don't use these frequently, but you can if you'd like to.

# Move windows.


# Resize windows.
```

I primarily use Slate to maximize windows easily with my keyboard, and move them across monitors. On occasion, I will use half screens to split two windows vertically.

Feel free to modify this slate configuration to suit your needs. You might find the [Slate documentation]() helpful.

### Miscellaneous

#### Adium

If you use [Adium](http://adium.im) as a chat client on your machine, I recommend setting up a [Global Keyboard Shortcut](). This allows you to switch the focus to Adium anytime on your machine by pressing the key sequence. It's super handy to instantly switch to Adium when you get an Adium notification.

I set my global keyboard shortcut to `Cmd-Shift-/`. To use this, you'll have to get rid of the keybinding for the `Help Center` first. Do this by removing the keybinding in `System Preferences > Keyboard > Keyboard Shortcuts > Help Center`.

To set the global keyboard shortcut in Adium, go to `Adium Preferences > General > Global Keyboard Shortcut `.

#### Spotlight/Alfred

You should already be using [Spotlight]() or [Alfred]() as your primary application launcher. They let you launch applications with your keyboard really easily, and do much more.

If you use multiple desktops, sometimes you'll want to create multiple windows of the same application. Spotlight will get in your way here, because if you try to launch an application that already has a window open, it will take you to the window instead of opening a new one. This happens to me all the time when I want to create a Chrome window, when you already have one open on another window. 

The easiest way to this is to go to an existing Chrome window, press `Cmd-N` to create another window, drag the newly created window, and *while dragging the window*, press `Cmd-1/2/3/4` to take the window to another desktop.
