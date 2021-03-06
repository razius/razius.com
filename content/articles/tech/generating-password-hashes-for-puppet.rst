Generating password hashes with puppet
######################################
:date: 2013-07-08 10:25
:tags: password, puppet, shadow
:slug: generating-password-hashes-for-puppet
:description: Generate a password hash to use when creating users with puppet.

Puppet expects the user’s password to be encrypted in the format the local system expects, for most modern Unix-like systems (Linux, \*BSD, Solaris, etc.) this format is a salted SHA1 password hash.

To generate a password hash to use with puppet manifest files you can use the mkpasswd utility (it's available in the whois package):

.. code-block:: console

    $ mkpasswd -m sha-512
    Password:
    $6$qfPDlAej83p$cj2nc1NjbKjhL42Mo/3Uia4NqD4dIB3ouVeI/tSG92UqH5cMKOA/ihjmxAuRtKHzGED0EHmdM0iNxa/662NW//

You can then use the password hash in a puppet manifest file:

.. code-block:: ruby

    user { 'root':
        ensure   => 'present',
        password => '$6$qfPDlAej83p$cj2nc1NjbKjhL42Mo/3Uia4NqD4dIB3ouVeI/tSG92UqH5cMKOA/ihjmxAuRtKHzGED0EHmdM0iNxa/662NW//',
    }

Don't forget to put the password in quotes so that puppet does not interpret it as a variable if it contains the dollar sign ($).

If you want the passwords to be stored in plain text in the puppet manifest you can use puppet's `generate <http://docs.puppetlabs.com/references/latest/function.html#generate>`_ function to call mkpassword and return the generated the hash version of the password:

.. code-block:: ruby

    $password = 'your_plain_text_password'
    user { 'root':
        ensure   => 'present',
        password => generate('/bin/sh', '-c', "mkpasswd -m sha-512 ${password} | tr -d '\n'"),
    }

References:
    - `Puppet type user`_
    - `Puppet sha1 function`_

.. _Puppet type user: http://docs.puppetlabs.com/references/latest/type.html#user
.. _Puppet sha1 function: http://docs.puppetlabs.com/references/latest/function.html#sha1
