#Add a custom HTTP header with Puppet
exec { 'update':
  command => 'sudo apt-get -y update',
}

exec { 'install':
  command => 'sudo apt-get -y install nginx',
}

exec { 'index.html':
  command => 'echo "Holberton School" > sudo tee /var/www/html/index.html',
}

exec { 'sed':
  command => "sudo sed -i '/server_name _;/ a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' > /etc/nginx/sites-available/default",
}

exec { 'custom_404':
  command => 'echo "Ceci n'est pas une page" > sudo tee /var/ww/html/custom_404.html',
}

exec { 'sed':
  command => "sudo sed -i '/server_name _;/ a error_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\troot /var/www/html;\n\tinternal;\n\t}' > etc/nginx/sites-available/default",
}

exec { 'sed':
  command => "sudo sed -i '/server_name _;/ a add_header X-Served-By $HOSTNAME;' > /etc/nginx/sites-available/default",
}

exec { 'service':
  command => 'sudo service nginx restart',
}
