# installs flask
exec { 'apt-get update':
  path => ['/bin', '/usr/bin'],
}

package { 'nginx':
  provider        => apt,
  install_options => ['-y'],
}

file { '/etc/nginx/sites-available/alx-1.com':
  mode    => '0755',
  owner   => 'www-data',
  group   => 'www-data',
  content =>"
server {
        listen 80;
        listen [::]:80;

        root /var/www/alx-1/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;
		rewrite ^/redirect_me / permanent;

        location / {
                try_files \$uri \$uri/ =404;
        }
}
",
}

file { '/var/www/alx-1':
    ensure => 'directory',
}
file { '/var/www/alx-1/html':
    ensure => 'directory',
}

file { '/var/www/alx-1/html/index.html':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-enabled/default':
  ensure => deleted,
}

exec { 'ln /etc/nginx/sites-available/alx-1.com /etc/nginx/sites-enabled/alx-1.com':
  path => ['/bin', '/usr/bin'],
}

exec { 'Start the server':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
