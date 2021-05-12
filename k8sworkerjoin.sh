#!/usr/bin/env bash


sudo apt-get update && sudo apt-get install -y apt-transport-https
sudo apt-get install -y docker.io
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo touch /etc/apt/sources.list.d/kubernetes.list 
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update -y   

sudo apt-get update && apt-get install -y apt-transport-https curl
sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
sudo cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update -y

apt-get install -y kubelet kubeadm kubectl

export JOIN_TOKEN=$(cat /vagrant/token.txt)

#sudo kubeadm join --discovery-token-unsafe-skip-ca-verification --token $JOIN_TOKEN 10.168.80.11:6443

