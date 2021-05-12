#!/bin/bash

sudo apt-get update && sudo apt-get install -y docker.io

sudo apt-get update && sudo apt-get install -y apt-transport-https curl ssh
sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF

chmod +x /vagrant/cfgchange.sh

sudo apt-get update -y 

sudo -i 

sudo apt-get install -y kubelet kubeadm kubectl

kubeadm init --apiserver-advertise-address 10.168.80.11

kubeadm token create --print-join-command  > /vagrant/token.txt

