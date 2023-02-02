# <TODO> documentation
exec { 'patch':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php && service apache2 restart"',
  path    => '/usr/sbin:/bin:/usr/bin'
}
