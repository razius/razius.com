# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "raring64"
    config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/raring/current/raring-server-cloudimg-amd64-vagrant-disk1.box"
    config.vm.network :forwarded_port, guest: 8000, host: 8000
    config.ssh.forward_agent = true
    config.vm.hostname = "pelican"
    # config.vbguest.installer = CloudUbuntuVagrant
    config.vm.provision :shell do |shell|
        shell.inline = "cd /vagrant && su -c 'bootstrap_vagrant.sh' vagrant"
        shell.args = ""
    end
end
