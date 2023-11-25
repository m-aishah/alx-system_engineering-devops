# Define a class to install and configure Nginx
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    location / {
        alias /var/www/html;
    }
}
",
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
    require => Package['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => [File['/etc/nginx/sites-available/default'], File['/var/www/html/index.html']],
  }
}

# Include the nginx class to configure Nginx
include nginx
