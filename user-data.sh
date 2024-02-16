#!/bin/bash
sudo yum update -y
sudo yum install git -y
sudo yum install httpd
cd /var/www/
sudo git clone https://github.com/AWS-Re-Start-RDC-KINSHASA-1/tp-1-barakael-henock.git
sudo pip3 install Flask
cd tp-1-barakael-henock/
sudo chown -R ec2-user:ec2-user .
chmod u+w .
nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &