Vagrant and SSH agent forwarding
#################################
:date: 2013-09-13 08:29
:tags: provisioning, ssh, vagrant
:slug: vagrant-and-ssh-agent-forwarding

I haven't even started yet and I can already hear you muttering over there, "What the hell is this Vagrant thing and why should I care?". Well, `Vagrant`_ is a wrapper around `VirtualBox`_, the virtualization
software, that can create homogeneous development environments automatically without any effort from the developer. This means that we have a consistent development environment across out team with the same OS version, same package versions, same database, same settings. No more *But it worked on MY machine* excuses.

Lets say that inside this virtual machine you need to use your SSH key, maybe the key for your `Github`_ account to access your private or public git repositories or maybe the key to connect to a remote server.
That can be a problem, you don't want to distribute your SSH keys with the Vagrant box. Each SSH key should be tied to an individual developer
account so to prevent SSH key sharing you would need to either distribute each SSH key with a new Vagrant box or copy it during provisioning. That's not really homogeneous, you will end up with a Vagrant box for each developer or an inconvenient way of providing the SSH key depending on the developer's OS.

Enter `SSH agent forwarding`_. With SSH agent forwarding we can use the SSH key from our local machine inside the Vagrant box.

To enable agent forwarding for all ssh connections inside your Vagrant box you need to set the following in your Vagrant file inside the config section (Vagrant.configure(VAGRANTFILE\_API\_VERSION) do \|config\|):

.. code-block:: bash

    [...]
        config.ssh.private_key_path = "~/.ssh/id_rsa"
        config.ssh.forward_agent = true
    [...]

Due to a Vagrant bug SSH Agent Forwarding not available during provisioning (`see issue`_), to work around that we need to create a file in ``/etc/sudoers.d/`` with the following contents:

.. code-block:: bash

    Defaults env_keep += "SSH_AUTH_SOCK"

To create it automatically during provisioning we can add the following to our Vagrant file:

.. code-block:: ruby

    config.vm.provision :shell do |shell|
        shell.inline = "touch $1 && chmod 0440 $1 && echo $2 > $1"
        shell.args = %q{/etc/sudoers.d/root_ssh_agent "Defaults env_keep += \"SSH_AUTH_SOCK\""}
    end

or in the shell script that you're using for provisioning:

.. code-block:: bash

    SSH_FIX_FILE="/etc/sudoers.d/root_ssh_agent"
    if [ ! -f  $SSH_FIX_FILE ]
        then
        echo "Defaults env_keep += \"SSH_AUTH_SOCK\"" > $SSH_FIX_FILE
        chmod 0440 $SSH_FIX_FILE
    fi

.. _Vagrant: http://www.vagrantup.com/
.. _VirtualBox: https://www.virtualbox.org/
.. _Github: https://github.com/
.. _SSH agent forwarding: https://help.github.com/articles/using-ssh-agent-forwarding
.. _see issue: https://github.com/mitchellh/vagrant/issues/1303
