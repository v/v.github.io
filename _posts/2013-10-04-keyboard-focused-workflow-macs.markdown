---
layout: post
title: "Keyboard Focused Development Workflow on Macs"
date: 2013-10-04
published: true
---

Having used Linux almost exclusively for the last four years, I miss efficient window management on Macs. Coming from the [awesome window manager](http://awesome.naquadah.org/), I find that OS X does not have good support for a two monitor multiple workspace workflow out of the box. After tinkering with third party software, I believe I've found a good solution for most of my complaints, and have a workflow that I feel productive with. In my experience, this works best with multiple monitors, a standard keyboard (think Dell not Apple), and a three button mouse (I'm not a fan of touchpads or Apple mice).

### Setting up Multiple Desktops

I really like the use of multiple desktops in my workflow. I usually set up four desktops. I keep [Spotify](http://spotify.com) open on the very last one. The middle ones are my "work" desktops that I use for terminals, browsers, IDEs, and documentation. The first one is usually a "distraction workspace" that will have my email, and [Adium](http://adium.com) open. This helps me keep my windows organized, and keep focus when I need to.

In order to set this up, I add additional desktops (up to 4). The easiest way to do this is to open up `Mission Control` (usually Control-Up), hover over the Desktops, and click the Plus button on the top right.

Once this is done, I would recommend setting up easy keybindings to switch between desktops. To do this, you go to `System Preferences > Keyboard > Keyboard Shortcuts > Mission Control`. Then you can set up keybindings for `Move left a space`, `Move right a space`, ... `Switch to Desktop 1-4`. I use `Ctrl-Alt-Left/Right` to move between desktops, and use `Command-1/2/3/4` to jump to a desktop.

### Using Slate for Window Management

On OS X, it's sometimes pretty cumbersome to perform window management tasks like moving windows between monitors, and maximizing windows efficiently. This is where Slate comes in. [Slate](http://github.com/jigish/slate) is a configurable third-party window management application, that makes these window management tasks super easy. I will explain how I use Slate day-to-day. 

#### Setting it up

You can install Slate, pretty simply by downloading the [Slate dmg](http://slate.ninjamonkeysoftware.com/Slate.dmg). After installing and starting Slate, you will want to make sure it's properly configured.

Here is my `~/.slate.js` configuration file that describes the keybindings I use with it. Right click on the Slate icon in the topbar > `Relaunch and Load Config`, to apply configuration changes. 

```javascript
//Save this in ~/.slate.js
//This configuration file came from http://vverma.net. 
//Credit to Gerard O'Neill, http://goneill.net for introducing me to Slate.

var left = {
    'x': 'screenOriginX',
    'y': 'screenOriginY',
    'width': 'screenSizeX/2',
    'height': 'screenSizeY',
};

var right = {
    'x': 'screenOriginX + screenSizeX/2',
    'y': 'screenOriginY',
    'width': 'screenSizeX/2',
    'height': 'screenSizeY',
};


//half screen.
slate.bind('right:ctrl,cmd', function(win) {
    var screen = slate.screen().rect();
    var win_rect = win.rect();

    // if we are at the edge of a screen on the right.
    if(Math.abs(screen.x + screen.width - win_rect.x - win_rect.width) < 5) {
        var curr_screen = slate.screen().id();
        slate.log(curr_screen);
        if(curr_screen < slate.screenCount() - 1) {
            var shift_screen = _.clone(left);
            shift_screen['screen'] = curr_screen + 1;

            win.doOperation(slate.operation('move', shift_screen));
        }
    } else {
        win.doOperation(slate.operation('move', right));
    }
});


//half screen.
slate.bind('left:ctrl,cmd', function(win) {
    var screen = slate.screen().rect();
    var win_rect = win.rect();

    // if we are at the edge of a screen on the left.
    if(screen.x == win_rect.x) {
        var curr_screen = slate.screen().id();
        if(curr_screen > 0) {
            var shift_screen = _.clone(right);
            shift_screen['screen'] = curr_screen - 1;

            win.doOperation(slate.operation('move', shift_screen));
        }
    } else {
        win.doOperation(slate.operation('move', left));
    }
});


//maximize
slate.bind('up:ctrl,cmd', function(win) {
    win.doOperation(slate.operation('move', {
        'x': 'screenOriginX',
        'y': 'screenOriginY',
        'width': 'screenSizeX',
        'height': 'screenSizeY',
    }));
});

//center
slate.bind('down:ctrl,cmd', function(win) {
    win.doOperation(slate.operation('move', {
        'x': 'screenOriginX + screenSizeX/4',
        'y': 'screenOriginY + screenSizeY/4',
        'width': 'screenSizeX/2',
        'height': 'screenSizeY/2',
    }));
});

```

Here is the mapping of keybindings

```
Cmd-Ctrl-Left - Split window in half vertically and move to the left. (Moves to the next screen if you are at the edge.)
Cmd-Ctrl-Right - Split window in half vertically and move to the right. (Moves to the next screen if you are at the edge.)

Cmd-Ctrl-Up - Maximize window.
Cmd-Ctrl-Down - Center window in its current screen.
```

Feel free to modify this slate configuration to suit your needs. You might find the [Slate documentation](https://github.com/jigish/slate/wiki/JavaScript-Configs) helpful.

### Miscellaneous

#### Adium

If you use [Adium](http://adium.im) as a chat client on your machine, I recommend setting up a [Global Keyboard Shortcut](). This allows you to switch the focus to Adium anytime on your machine by pressing the key sequence. It's super handy to instantly switch to Adium when you get an Adium notification.

I set my global keyboard shortcut to `Cmd-Shift-/`. To use this, you'll have to get rid of the keybinding for the `Help Center` first. Do this by removing the keybinding in `System Preferences > Keyboard > Keyboard Shortcuts > Help Center`.

To set the global keyboard shortcut in Adium, go to `Preferences > General > Global Shortcut `.

Now, you can press `Cmd-Shift-/` to switch to Adium, and press `Cmd-/` to show/hide your buddy list.

#### Spotlight/Alfred

You should already be using [Alfred](http://www.alfredapp.com) as your primary application launcher. It lets you launch applications with your keyboard really easily, and do much more. It's also way faster than Spotlight.

If you use multiple desktops, sometimes you'll want to create multiple windows of the same application. Alfred will get in your way here, because if you try to launch an application that already has a window open, it will take you to the window instead of opening a new one. This happens to me all the time when I want to create a Chrome window, when you already have one open on another window. 

The easiest way to do this is to go to an existing Chrome window, press `Cmd-N` to create another window, drag the newly created window, and *while dragging the window*, press `Cmd-1/2/3/4` to take the window to another desktop.

#### Spaces

Like I mentioned before, I use Spaces in my development workflow. One thing that I really dislike about Spaces is that when you move between Spaces using `Ctrl-Alt-Left/Right`, it takes a second to animate the movement. I don't like this because it feels clunky.

You can run this in a terminal to make this animation a lot faster.

```
defaults write com.apple.dock expose-animation-duration -int 0; killall Dock
```

Credit to [Gerard O'Neill](http://goneill.net) for showing me a lot of this workflow.
