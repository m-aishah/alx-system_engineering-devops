# Define a class to install and configure Nginx
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://cuberule.com/;
    }
}
",
    require => Package['nginx'],
  }

file { '/etc/nginx/html':
    ensure  => directory,
    mode    => '0755',
  }

  file { '/etc/nginx/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
    require => Package['nginx'],
    mode => '0644'
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => [File['/etc/nginx/sites-available/default'], File['/etc/nginx/html/index.html']],
  }
}

# Include the nginx class to configure Nginx
include nginx
