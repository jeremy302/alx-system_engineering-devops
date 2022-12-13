# installs flask
exec { 'apt-get update':
  path => ['/bin', '/usr/bin'],
}

package { 'nginx':
  provider        => apt,
  install_options => ['-y'],
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
  content => "Hello World!\n",
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


tidy { '/etc/nginx/sites-enabled/default' }

file { '/etc/nginx/sites-available/alx-1.com':
  ensure => 'link',
  target => '/etc/nginx/sites-enabled/alx-1.com'
}
# exec { 'ln /etc/nginx/sites-available/alx-1.com /etc/nginx/sites-enabled/alx-1.com':
#   path => ['/bin', '/usr/bin'],
# }

exec { 'nginx':
  path    => '/usr/bin:/usr/sbin:/bin',
}
