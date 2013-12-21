Getting the IP address of a specific interface in puppet using facter
#####################################################################
:date: 2013-10-06 22:13
:tags: facter, puppet
:slug: getting-the-ip-address-of-a-specific-interface-in-puppet-using-facter

One of the problems that I find annoying in puppet is that you can't easily obtain the IP address of a specific network interface.

Let's say that you want to define a class or type to which you wish to pass a interface name and use it's IP address as a variable.

.. code-block:: ruby

    class dns ($interface) {
        $address = [ insert magic here ]

        $message = "So you want to know the IP address for ${interface} huh?"
        $message += "Well, it's ${address}"
        notify {  "${message}": }
    }

    class { 'dns': interface => 'eth0' }

We could use facters ``$::ipaddress``, but what happens if the network interface is not our main network interface? What if we want to use more than one network interface? There's ``$::ipaddress_eth0``, but how do we construct or reference a variable in a dynamic way (construct a variable based on another variable) ?

Luckily there's a nifty trick involving inline templates and lookupvar:

.. code-block:: ruby

    class dns ($interface) {
        $address = inline_template("<%= scope.lookupvar('::ipaddress_${interface}') -%>")

        $message = "So you want to know the IP address for ${interface} huh?"
        $message += "Well, it's ${address}"
        notify {  "${message}": }
    }

    class { 'dns': interface => 'eth0' }

