Installing and adding an external Tomcat server in Netbeans
###########################################################
:date: 2012-01-28 05:18
:tags: linux, netbeans, tomcat
:slug: installing-and-adding-an-external-tomcat-server-in-netbeans

Netbeans no longer comes with Tomcat bundled so if you want to deploy
your application to an Tomcat server you need to manually register an
external server.

Pre-requisites:
~~~~~~~~~~~~~~~

I'm assuming you are using at least Ubuntu Linux 11.10 and you already
have installed the the latest Netbeans 7.1 with the Java Web
Applications plugin installed.

I also assume that you want to install and configure Tomcat from the
repository, if you don't care an easier method would be to just download
`apache-tomcat.zip`_ from the Tomcat website, extract the archive to a
folder under your home directory and just skip to step 4 of this
tutorial where Under Server Location you would browse to where you
extracted the archive and under Username and Password you would put the
username and password you would have put in tomcat-users.xml.

1. Install Tomcat
~~~~~~~~~~~~~~~~~

::

    $ sudo apt-get install tomcat7 tomcat7-common tomcat7-admin tomcat7-user

2. Add an administrative user to Tomcat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tomcat does have any users defined that could be used for administrative
purposes so we need to open tomcat-users.xml in a text editor and add a
user with the proper roles assigned to it.

::

    $ sudo gedit /etc/tomcat7/tomcat-users.xml

Replace its content with the following and make sure that you replace
USERNAME and PASSWORD with the values you want:

::







3. Some "fixes"
~~~~~~~~~~~~~~~

Unfortunately it seams that Netbeans doesn't correctly detect the the
Tomcat installation directory so we need to make some temporary changes
till we add the server otherwise will get an error saying *The specified
Server Location (Catalina Home) folder is not valid.*

::

    $ cd /usr/share/tomcat7/lib
    $ mv catalina.jar catalina.jar.bk
    $ wget http://www.razius.com/files/catalina.jar

We need to make sure that the configuration files can be read from the
installation directory otherwise will get an error saying
*The <CATALINA\_HOME>/conf/server.xml can't be read.*

::

    $ sudo ln -s /etc/tomcat7/ /usr/share/tomcat7/conf

We need to chown the Tomcat installation and configuration directory so
we don't have any permission problems. Replace USERNAME with your Ubuntu
username:

::

    $ sudo chown -R USERNAME:USERNAME /etc/tomcat7/
    $ sudo chown -R USERNAME:USERNAME /usr/share/tomcat7/

Disable the upstart Tomcat service (Netbeans start's it up for us
automatically):

::

    $ sudo update-rc.d tomcat7 disable 0123456

4. Adding the server in Netbeans
--------------------------------

|image0|
 Now that you have Tomcat installed and configured we can open up
Netbeans and under the Services tab right click on the Servers node and
click on Add server.

In the current list select Apache Tomcat and click Next.

`|image1|`_
 Under Server Location enter your Tomcat installation directory , by
default this should be /usr/share/tomcat7

Next under Username and Password put in the username and password that
we added in the tomcat-users.xml file.

Click Finish. You should now be able to see Tomcat as an added server
under the Servers Node.

5. Revert changes
~~~~~~~~~~~~~~~~~

If we are installing from the repository we need to revert some changes
done in step 3:

::

    $ cd /usr/share/tomcat7/lib
    $ rm catalina.jar
    $ mv catalina.jar.bk catalina.jar

.. _apache-tomcat.zip: http://ftp.download-by.net/apache/tomcat/tomcat-7/v7.0.47/bin/apache-tomcat-7.0.47.tar.gz
.. _|image2|: http://razius.com/wp-content/uploads/2012/01/netbeans-add-server-instance.png

.. |image0| image:: http://razius.com/wp-content/uploads/2012/01/netbeans-add-server.png
.. |image1| image:: http://razius.com/wp-content/uploads/2012/01/netbeans-add-server-instance-300x184.png
.. |image2| image:: http://razius.com/wp-content/uploads/2012/01/netbeans-add-server-instance-300x184.png
