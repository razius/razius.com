Generating password hashes for puppet
#####################################
:date: 2013-07-08 10:25
:tags: password, puppet, shadow
:slug: generating-password-hashes-for-puppet

Puppet expects the user’s password to be encrypted in the format the
local system expects, for most modern Unix-like systems (Linux, \*BSD,
Solaris, etc.) this format is a salted SHA1 password hash.

To generate a password hash to use with puppet manifest files you can
use the mkpasswd utility (it's available in the whois package):

.. code-block:: bash

    $ mkpasswd -m sha-512
    Password:
    $6$qfPDlAej83p$cj2nc1NjbKjhL42Mo/3Uia4NqD4dIB3ouVeI/tSG92UqH5cMKOA/ihjmxAuRtKHzGED0EHmdM0iNxa/662NW//

You can then use the password hash in a puppet manifest file:

.. code-block:: ruby

    user { 'root':
      ensure           => 'present',
      password         => '$6$qfPDlAej83p$cj2nc1NjbKjhL42Mo/3Uia4NqD4dIB3ouVeI/tSG92UqH5cMKOA/ihjmxAuRtKHzGED0EHmdM0iNxa/662NW//',
    }

Don't forget to put the password in quotes so that puppet does not
interpret it as a variable if it contains the dollar sign ($).

If you want the passwords to be stored in plain text in the puppet
manifest you can use puppet's sha1 function to generate the hashed
version of the password:

.. code-block:: ruby

    user { 'root':
      ensure           => 'present',
      password         => sha1('password'),
    }

References:
    - `Puppet type user`_
    - `Puppet sha1 function`_

.. _Puppet type user: http://docs.puppetlabs.com/references/latest/type.html#user
.. _Puppet sha1 function: http://docs.puppetlabs.com/references/latest/function.html#sha1
