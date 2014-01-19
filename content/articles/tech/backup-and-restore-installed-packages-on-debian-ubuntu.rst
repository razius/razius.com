Backup and restore installed packages on Debian/Ubuntu
######################################################
:date: 2012-03-05 10:24
:tags: debian, dpkg, linux
:slug: backup-and-restore-installed-packages-on-debian-ubuntu
:description: Backup your list of installed packages on Debian/Ubuntu for easy restoration after an OS reinstall.

If you want to reinstall a server or a desktop and want to install the same packages after reinstalling the operating system you can easily do that with dpkg.

First we need to backup the list of packages to a file and after reinstalling the operating system, in this example will also backup the ``/etc/apt/sources.list`` file and the ``/etc/apt/sources.list.d`` directory as they contain the list of repositories from which you installed packages.

Backuping up the list of installed package and the repository list into a tar archive
-------------------------------------------------------------------------------------

.. code-block:: console

    # mkdir ~/packages; cp -R /etc/apt/sources.list /etc/apt/sources.list.d/ ~/packages/; dpkg --get-selections > ~/packages/package.list; tar cPvzf ~/packages-`date +%Y-%m-%d`.tar.gz ~/packages/; rm -rf ~/packages/

Now you should have a ``packages-DATE.tar.gz`` archive under your root user's home folder (/root/) containing the list of packages and repositories.

Restore the list of installed package and the repository list from the tar archive:
-----------------------------------------------------------------------------------

After reinstalling upload the packages-DATE.tar.gz archive to the root's user's home directory (``/root/``) and run the following command:

.. code-block:: console

    # mkdir ~/packages; tar xPvzf ~/packages-*.tar.gz; cp ~/packages/sources.list /etc/apt/sources.list; cp ~/packages/sources.list.d/* /etc/apt/sources.list.d/;apt-get update; dpkg --set-selections < ~/packages/package.list; apt-get install --yes dselect; dselect update; apt-get dselect-upgrade

This will install all of the packages which you had at the time of the backup.
