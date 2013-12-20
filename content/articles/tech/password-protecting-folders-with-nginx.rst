Password protecting folders with nginx
#######################################
:date: 2012-02-13 12:20
:tags: nginx
:slug: password-protecting-folders-with-nginx

If you need to password protect a folder using nginx here's how.
 In this example we're gonna password protect the /admin folder.
Accessing the admin directory will prompt the user with a basic
authentication dialog, and will be challenged against the created
password file.

Edit your site's configuration file and add the following lines inside
the server-block configuration:

::

    location /admin {
       auth_basic            "Restricted";
       auth_basic_user_file  /etc/nginx/htpasswd;
    }

Next we need to create a password file , the safest place to store a
password file is outside of the web-accessible location so we're gonna
place it in /etc/nginx.

::

    # cd /etc/nginx/
    # wget http://trac.edgewall.org/export/10975/trunk/contrib/htpasswd.py
    # chmod 755 htpasswd.py
    # ./htpasswd.py -c -b htpasswd USERNAME PASSWORD

Don't forget to reload nginx so that the configuration changes take
effect:

::

    # /etc/init.d/nginx reload

