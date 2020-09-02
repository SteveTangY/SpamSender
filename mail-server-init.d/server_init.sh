#! /bin/env bash

echo "installing postfix...\n"
sudo apt-get install postfix > /dev/null << EOF
y
EOF
echo "installing mailutils...\n"
sudo apt-get install mailutils > /dev/null << EOF
y
EOF
