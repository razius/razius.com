Usefull linux commands/tricks
#############################
:date: 2012-05-14 23:00
:slug: usefull-linux-commandstricks

These are some sort of notes to myself, this list will be constantly updated.

Sort directories by size (human readable size):

.. code-block:: console

    # du --max-depth=1 -h |sort -hr

Set tabsize to 4 in vim:

.. code-block:: vim

    :set tabstop=4

Show failed login attempts on your machine:

.. code-block:: console

    # lastb -F

Print the most recent login of all users and of a given user:

.. code-block:: console

    # lastlog
    lastlog -u USERNAME

.. code-block:: console

    $ curl -d "param1=value1&param2=value2" http://example.com/
    $ curl -X POST -d @filename http://example.com/

Return current SSID

.. code-block:: console

    iwconfig wlan0 | awk -F':' '/ ESSID/ {print $2}' | tr -d '"'

Force a reboot:

.. code-block:: console

    # echo 1 > /proc/sys/kernel/sysrq
    # echo b > /proc/sysrq-trigger

Force a shutdown:

.. code-block:: console

    # echo 1 > /proc/sys/kernel/sysrq
    # echo o > /proc/sysrq-trigger

