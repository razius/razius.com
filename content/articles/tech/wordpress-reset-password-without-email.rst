Wordpress reset password without email
######################################
:date: 2011-09-13 14:45
:slug: wordpress-reset-password-without-email

If you're like me and you forgot your wordpress password and don't have email setup on your system there are alternative ways to set a new password rather then sending and email.

Pick a particular method depending on what type of access you have to your website/hosting.

Through MySQL:
--------------

The easiest ways is through the MySQL command line but you need ssh access to your server.

1. Connect to MySQL:

.. code-block:: console

    # mysql -u root -p

2. Select the wordpress database (replace DATABASE with the wordpress database, if you don't know it you can find it in ``wp-config.php`` under ``DB_NAME``):

.. code-block:: mysql

    mysql> use DATABASE;

3. Update the password running the folowing query (replace NEWPASSWORD with your new password and USERNAME with the username you wish to change the password for):

.. code-block:: mysql

    mysql> UPDATE wp_users SET user_pass = MD5('NEWPASSWORD') WHERE user_login = 'USERNAME';

Through ftp/file edit
---------------------

If you don't have MySQL access you can also reset it by editing your theme's functions.php file. Edit the file and insert after the first <?php the folowing(replace NEWPASSWORD with your new password):

.. code-block:: php

    wp_set_password('NEWPASSWORD',1);

After you changed your password make sure you delete the line from functions.php otherwise it will reset your password on every page load.
