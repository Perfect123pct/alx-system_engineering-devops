#!/usr/bin/env bash
#  Add a custom HTTP header with Puppet

# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Define a custom fact to get the hostname
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Configure Nginx with custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By $custom_hostname;
        # ... (other configurations)
    }

    # ... (other server blocks)
}
",
  notify  => Service['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}
