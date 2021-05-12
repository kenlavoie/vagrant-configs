# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing. 

$script = <<SCRIPT
  chmod +x /vagrant/k8smgrinst.sh 
  chmod +x /vagrant/cfgchange.sh 
  source /vagrant/k8smgrinst.sh 
  sleep 480
  source /vagrant/cfgchange.sh
  
SCRIPT


Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.

      config.vm.define "kube11" do |kube11|
        config.vm.provider :virtualbox do |vb|
                vb.customize ["modifyvm", :id, "--memory", "2048"]
                vb.customize ["modifyvm", :id, "--cpus", "1"]
                vb.name = "kube11"
        end
        kube11.vm.box = "ubuntu/xenial64"
        kube11.vm.hostname = "kube11"
        kube11.vm.network "private_network", ip: "10.168.80.11"
        kube11.vm.provision :shell, path: "k8smgrinst.sh"
        kube11.vm.provision :shell, path: "cfgchange.sh"
      end
      config.vm.define "kube22" do |kube22|
        config.vm.provider :virtualbox do |vb|
                vb.customize ["modifyvm", :id, "--memory", "2048"]
                vb.customize ["modifyvm", :id, "--cpus", "1"]
                vb.name = "kube22"
        end
        kube22.vm.box = "ubuntu/xenial64"
        kube22.vm.hostname = "kube22"
        kube22.vm.network "private_network", ip: "10.168.80.12"
        kube22.vm.provision :shell, path: "k8sworkerjoin.sh"
      end
      config.vm.define "kube33" do |kube33|
        config.vm.provider :virtualbox do |vb|
                vb.customize ["modifyvm", :id, "--memory", "2048"]
                vb.customize ["modifyvm", :id, "--cpus", "1"]
                vb.name = "kube33"
        end
        kube33.vm.box = "ubuntu/xenial64"
        kube33.vm.hostname = "kube33"
        kube33.vm.network "private_network", ip: "10.168.80.13"
        kube33.vm.provision :shell, path: "k8sworkerjoin.sh"
      end
        config.vm.define "kube44" do |kube44|
        config.vm.provider :virtualbox do |vb|
                vb.customize ["modifyvm", :id, "--memory", "2048"]
                vb.customize ["modifyvm", :id, "--cpus", "1"]
                vb.name = "kube44"
        end
        kube44.vm.box = "ubuntu/xenial64"
        kube44.vm.hostname = "kube44"
        kube44.vm.network "private_network", ip: "10.168.80.14"
        kube44.vm.provision :shell, path: "k8sworkerjoin.sh"
      end



  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "10.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
