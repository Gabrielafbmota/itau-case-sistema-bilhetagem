#!bin/bash

rm -rf ../event_ticketing.db

python3 create_sqlite.py

chmod +w ../event_ticketing.db
sudo chown $USER:$USER ../event_ticketing.db

