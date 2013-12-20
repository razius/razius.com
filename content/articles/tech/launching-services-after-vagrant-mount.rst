Launching services after Vagrant mount
######################################
:date: 2013-11-10 14:40
:tags: init, upstart, vagrant, virtualbox
:slug: launching-services-after-vagrant-mount

I recently had to set up a Vagrant project where all the configuration
files for services like nginx, supervisor, mysql where symlinks pointing
to files residing on the `Vagrant synced folder`_. This turned out to be
a bit of a problem, when the Vagrant box boots, one of the last things
it does is mount the synced folder, so those services would fail to
start because of missing configuration files.

To fix the problem you need to ensure that all services are started
after Vagrant had the chance to mount the synced /vagrant/ folder and to
do this there are a couple of ways depending on the type of init script
that the service has.

Upstart
~~~~~~~

There is an `upstart event`_ that Vagrant emits each time it mounts a
synced folder that is called *vagrant-mounted* so we can modify the
upstart configuration file for services that depend on the Vagrant
synced folder to listen and start after the *vagrant-mounted* `event is
emitted`_.

.. code-block:: bash

    # nginx
    description "nginx http daemon"
    author "Silviu Tantos "

    # Listen and start after the vagrant-mounted event
    start on vagrant-mounted
    stop on runlevel [!2345]

    env DAEMON=/usr/sbin/nginx
    env PID=/var/run/nginx.pid

    expect fork
    respawn
    respawn limit 10 5

    pre-start script
            $DAEMON -t
            if [ $? -ne 0 ]
                    then exit $?
            fi
    end script

    exec $DAEMON

System-V
~~~~~~~~

If you are not running Ubuntu as the guest OS or you don't want to
convert your init script to upstart, there's still hope, albeit a bit
more complicated. Underneath Vagrant uses VirtualBox's shared folder for
it's synced folder so we can hook-up to udev events and trigger a script
execution after the VirtualBox mount event has fired, this of course
will also works for VirtualBox's shared folder not just for Vagrant's
synced folders.

Finding out the udev event
^^^^^^^^^^^^^^^^^^^^^^^^^^

This step is not needed as I already wrote the udev rule, it's just to
show how I came up with it. If you're not interested in it just skip to
writing the udev rule.

Fire up a terminal and listen to udev events:

.. code-block:: bash

    root@vagrant:~# udevadm monitor --property --kernel
    monitor will print the received events for:
    KERNEL - the kernel uevent

Fire up another terminal and trigger a mount:

.. code-block:: bash

    root@vagrant:~# mount -t vboxsf -o uid=`id -u vagrant`,gid=`id -g vagrant` /vagrant /vagrant

Now we should see the event in the first terminal window:

.. code-block:: bash

    root@vagrant:~# udevadm monitor --property --kernel
    monitor will print the received events for:
    KERNEL - the kernel uevent

    KERNEL[4234.545610] add      /devices/virtual/bdi/vboxsf-13 (bdi)
    ACTION=add
    DEVPATH=/devices/virtual/bdi/vboxsf-13
    SEQNUM=1407
    SUBSYSTEM=bdi
    UDEV_LOG=3

Writing the udev rule
^^^^^^^^^^^^^^^^^^^^^

We can see that the subsystem is *bdi* and the action is *add* so we can
write a `udev rule`_ for the event. I use
``/etc/udev/rules.d/50-vagrant-mount.rules`` as the file name and path.

.. code-block:: bash

    # Start on mount
    SUBSYSTEM=="bdi",ACTION=="add",RUN+="/usr/bin/screen -m -d bash -c 'sleep 5; /etc/init.d/nginx start'"
    # Stop on unmount
    SUBSYSTEM=="bdi",ACTION=="remove",RUN+="/usr/bin/screen -m -d bash -c 'sleep 5; /etc/init.d/nginx stop'"

This will run each time a VirtualBox shared folder is mounted. It spawns
a screen session (of course you need to have the `screen`_ package
installed) to prevent the command from being killed by systemd when
parent udev exits, sleeps for 5 seconds to make sure Vagrant had the
chance to mount the synced folder and exits successfully and finally
start the service.

Don't forget to type in the full paths otherwise udev won't be able to
find the command. For more information see the `udev manual`_.

.. _Vagrant synced folder: http://docs.vagrantup.com/v2/synced-folders/index.html
.. _upstart event: http://upstart.ubuntu.com/cookbook/#event
.. _event is emitted: https://github.com/mitchellh/vagrant/blob/7897de3fbdc4c61a281954ec2df1c23bfe22f4d4/plugins/guests/ubuntu/cap/mount_nfs.rb#L13
.. _udev rule: http://hackaday.com/2009/09/18/how-to-write-udev-rules/
.. _screen: https://wiki.archlinux.org/index.php/GNU_Screen
.. _udev manual: http://www.freedesktop.org/software/systemd/man/udev.html#RUN%7Btype%7D
