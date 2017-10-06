#!/bin/sh
echo "Installing PyQT, pandas, numpy, scikit-learn and other dependencies!"
read -p "Press [Enter] key to start..."
sudo apt-get -y update
sudo apt-get -y install python-pip python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential
sudo apt-get -y install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
sudo apt-get -y install build-essential python-dev python-setuptools \
                     python-numpy python-scipy \
                     libatlas-dev libatlas3gf-base
pip install -r pip_req.txt
echo "\n\nDONE!!!"

