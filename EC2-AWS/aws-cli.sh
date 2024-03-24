sudo apt update
sudo apt install awscli apache2 -y
aws s3 cp s3://voutuk/site/sign-in/ /var/www/html/ --recursive
