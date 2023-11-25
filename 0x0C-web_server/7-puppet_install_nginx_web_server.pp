# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create a new Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => '
    server {
        listen 80;
        listen [::]:80 default_server;
        root   /etc/nginx/html;
        index  index.html index.htm;

        location /redirect_me {
            return 301 http://cuberule.com/;
        }
    }
  ',
  require => Package['nginx'], # Ensure the Nginx package is installed before creating the configuration file
}

# Create the "Hello World" index.html
file { '/etc/nginx/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx'], # Ensure the Nginx package is installed before creating the index.html file
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [
    File['/etc/nginx/sites-available/default'], # Ensure the configuration file is in place before starting the service
    File['/etc/nginx/html/index.html'],         # Ensure the index.html file is in place before starting the service
  ],
}
