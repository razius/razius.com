Auto-refreshing Google Chrome on file changes
#############################################
:date: 2014-01-19 10:58
:tags: automation, chrome, bash
:slug: auto-refreshing-google-chrome-on-file-changes
:description: Automatically refreshing Google Chrome when a file changes with a simple bash script (or poor man's LiveReload).

I am known for being an lazy ass, one of the ways of coping with this horrible disease is automating any repetitive task that takes more that 5 minutes of work. So, in my free time, when I'm not dreaming of eating cake on a magical dessert island, I have the habit of bashing away at my keyboard to write shell scripts that ease my life.

During the process of writing a HTML presentation for my school and while trying to find ways to procrastinate and avoid it, I head this little voice in my head: "Hey, psstt, you, wouldn't it be neat if you didn't have to spend those 5 seconds refreshing the browser window each time you save that file?".

After consulting my trusty "Is it work the time chart?" and seeing that I have lots of free time, with the weekend ahead of me, I've decided to listen to my little procrastination demon and dive in to see how I can shave those 5 seconds off.

.. figure:: http://imgs.xkcd.com/comics/is_it_worth_the_time.png
    :align: center
    :target: http://xkcd.com/1205/

It turns out it's pretty easy to do, there are two nice system utilities on Linux that you can easily glue together by writing a bash script.


inotifywait
-----------

inotifywait is a command-line utility that uses the `inotify <http://linux.die.net/man/7/inotify>`_ Linux kernel API which provides a mechanism for monitoring filesystem events. The API can be used to monitor individual files, or to monitor directories.

When a directory is monitored, inotify  will  return  events  for  the  directory itself, and for files inside the directory. Events are fired, for example, for file and directory creation, deletion, access, modification, etc (for a full list, read the manual).

inotifywait, as the name suggests, will listen and wait for an event returning a code if the events for which we are listening to are triggered.


xdotool
-------

xdotool is a command-line utility that lets you automate keyboard input and mouse activity, move and resize windows, etc. It basically lets you control your GUI application.

TuxRadar has a really nice `tutorial <http://tuxradar.com/content/xdotool-script-your-mouse>`_ about it if you want to find out more.

Tying it all together
---------------------

Ubuntu doesn't come with inotifywait and xdotool installed by default, but you can install them using apt:

..  code-block:: console

    apt-get install -y inotify-tools xdotool

Now for the bash script.

.. code-block:: bash

    #!/bin/bash
    #
    # Watches the folder or files passed as arguments to the script and when it
    # detects a change it automatically refreshes the current selected Chrome tab or
    # window.
    #
    # Usage:
    # ./chrome-refresh.sh /folder/to/watch /some/folder/file_to_watch.html

    TIME_FORMAT='%F %H:%M'
    OUTPUT_FORMAT='%T Event(s): %e fired for file: %w. Refreshing.'

    while inotifywait -q -r --timefmt "${TIME_FORMAT}" --format "${OUTPUT_FORMAT}" "$@"; do
        CHROME_WINDOW_ID=$(xdotool search --onlyvisible --class google-chrome | head -1)
        xdotool key --window $CHROME_WINDOW_ID 'CTRL+r'
    done

It waits for an event, when detected it will search for the current Google Chrome window or tab and send the refresh key shortcut (CTRL+r) to it then loop again in the listening state.

I've also made a `gist <https://gist.github.com/razius/8503625>`_ for easy reference. I'll probably update that more when I'll want to add new features.

**Note**: Yes, I know about LiveReload but I find it way to complicated for my needs and it's also not available on Linux (my OS of choice). Plus, in the process I learned something new and I will definitely be using that knowledge in the future.


