#!bin/bash

sudo yum update

sudo yum install postgresql15 postgresql15-server -y

sudo postgresql-setup --initdb

sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql


sudo passwd postgres

su - postgres

# Now, change the admin database password:
psql -c "ALTER USER postgres WITH PASSWORD 'GciT3DJ68wraYjnH0NuxSx1fo31OHZfA';"
exit

