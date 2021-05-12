#!/bin/bash 

sudo -i 
export HOME="/home/ubuntu/"

sudo mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config 
