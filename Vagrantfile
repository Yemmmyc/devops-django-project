# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.network "forwarded_port", guest: 8000, host: 8010

# Sync "myproject" folder to the VM
  config.vm.synced_folder "myproject", "/home/vagrant/myproject", type: "virtualbox"

  config.vm.provision "shell", path: "provision.sh"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
end
