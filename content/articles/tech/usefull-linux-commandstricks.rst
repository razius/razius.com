Usefull linux commands/tricks
#############################
:date: 2012-05-14 23:00
:slug: usefull-linux-commandstricks

These are some sort of notes to myself, this list will be constantly
updated.

Sort directories by size (human readable size):

::

    # du --max-depth=1 -h |sort -hr

Set tabsize to 4 in vim:

::

    :set tabstop=4

Show failed login attempts on your machine:

::

    # lastb -F

Print the most recent login of all users and of a given user:

::

    # lastlog
    lastlog -u USERNAME

::

    $ curl -d "param1=value1&param2=value2" http://example.com/
    $ curl -X POST -d @filename http://example.com/

Return current SSID

::

    iwconfig wlan0 | awk -F':' '/ ESSID/ {print $2}' | tr -d '"'

Force reboot:

::

    # echo 1 > /proc/sys/kernel/sysrq
    # echo b > /proc/sysrq-trigger

Force shutdown:

::

    # echo 1 > /proc/sys/kernel/sysrq
    # echo o > /proc/sysrq-trigger

