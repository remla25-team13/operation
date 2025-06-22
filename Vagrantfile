# -*- mode: ruby -*-
# vi: set ft=ruby :

#Variables
NODES = 2
CORE_CPUS = 2
CORE_MEM = 4096
WORKER_CPUS = 2
WORKER_MEM = 6144

def get_node_ip(node)
  return "192.168.56.#{100 + node}"
end

def provision_ansible_general(defined_node)
  defined_node.vm.provision :ansible do |ansible|
    ansible.compatibility_mode = '2.0'
    ansible.playbook = 'ansible/playbooks/general.yml'
    ansible.extra_vars = {
      nodes: [
        { hostname: 'ctrl', ip: get_node_ip(0) },
        *(1..NODES).map { |i| { hostname: "node-#{i}", ip: get_node_ip(i) } }
      ]
    }
  end
end

ansible_groups = {
  :control => ['ctrl'],
  :workers => (1..NODES).map { |i| "node-#{i}" }
}

#Vagrant configuration 
Vagrant.configure("2") do |config|

  #Configure control node
  config.vm.define "ctrl" do |ctrl|
    ctrl.vm.hostname = "ctrl"

    #Provide bento image
    ctrl.vm.box = "bento/ubuntu-24.04"

    #Set network settings
    ctrl.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    ctrl.vm.network "private_network", ip: get_node_ip(0)
    ctrl.vm.network "forwarded_port", guest: 22, host: 22
    #Set virtualbox settings
    ctrl.vm.provider "virtualbox" do |v|
      v.memory = CORE_MEM
      v.cpus = CORE_CPUS
    end

    #Run general ansible
    provision_ansible_general(ctrl)

    #Run ansible for control node
    ctrl.vm.provision :ansible do |acore|
      acore.compatibility_mode = "2.0"
      acore.playbook = "ansible/playbooks/ctrl.yml"
      acore.groups = ansible_groups
    end

    # ctrl.vm.provision "finalization", type: :ansible do |final|
    #   final.compatibility_mode = "2.0"
    #   final.playbook = "ansible/playbooks/finalization.yml"
    #   final.groups = ansible_groups
    # end
  end
  
  #Configure NODES amount of workers
  (1..NODES).each do |i|
    #create node i
    config.vm.define "node-#{i}" do |node|
      node.vm.hostname = "node-#{i}"

      #Bento
      node.vm.box = "bento/ubuntu-24.04"

      #Network
      node.vm.network "forwarded_port", guest: "8#{i}", host: "808#{i}" , host_ip: "127.0.0.1"
      node.vm.network "private_network", ip: get_node_ip(i)

      #Set virtualbox settings
      node.vm.provider "virtualbox" do |v|
        v.memory = WORKER_MEM
        v.cpus = WORKER_CPUS
      end

      #Run general ansible
      provision_ansible_general(node)

      #Run node ansible
      node.vm.provision :ansible do |anode|
        anode.compatibility_mode = "2.0"
        anode.playbook = "ansible/playbooks/node.yml"
        anode.groups = ansible_groups
      end
    end
  end
end
