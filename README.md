# flask-practices
Flask practices 

# Check Python Refresher 

https://github.com/tecladocode/python-refresher

# VirtualEnv

python -m venv tutorial-env

tutorial-env\Scripts\activate.bat

# Test

# Queries

```
users = [{"id": 1, "username": "bob", "password": "asdf"}]
users = [User(1, "bob", "asdf")]

username_mapping = {"bob": {"id": 1, "username": "bob", "password": "asdf"}}
username_mapping = {u.username: u for u in users}

userid_mapping = {1: {"id": 1, "username": "bob", "password": "asdf"}}
userid_mapping = {u.id: u for u in users}

```

# Table

```
CREATE TABLE IF NOT EXISTS users(
	id INT 
	username VARCHAR(50) UNIQUE NOT NULL, 
	password VARCHAR(50) NOT NULL
);
```

## Info

```
sudo -i -u <name>
psql
\conninfo
exit
exit
adduser <name>
visudo
sudo su
sudo -i -u <name>
createuser <name> -P
createdb <name>
exit
exit
psql
```

## Links

https://arac.tecladocode.com/

## Process
- Installing psql
	- apt-get update
	- apt-get install postgresql postgresql-contrib
	- sudo -i -u postgres
	- psql
	- \conninfo
	- \q
	- exit
- login root
- create new user
	- adduser name
	- visudo
	- vi /etc/ssh/sshd_config
	- service sshd reload
	- ssh user@adress
	- sudo su
	- exit
- postgres config 
	- sudo su
	- sudo -i -u postgres
	- createuser user -P 
	- createdb user
	- exit
	- exit
	- psql 
	- \conninfo
	- \q
	- sudo vi /etc/postgresql/12/main/pg_hba.conf
	- change peer for md5
- nginx
	- sudo apt-get update
	- sudo apt-get install nginx
	- sudo ufw status
	- sudo ufw enable
	- sudo ufw allow 'Nginx HTTP'
	- systemctl status nginx
	- systemctl stop nginx
	- systemctl restart nginx
	- sudo vi /etc/nginx/sites-available/store-rest.conf
	```
server{
listen 80;
real_ip_header X-Forwarded-For;
set_real_ip_from 127.0.0.1;
server_name localhost;

location / {
include uwsgi_params;
uwsgi_pass unix:/var/www/html/store-rest/socket.sock;
uwsgi_modifier1 30;
}

error_page 404 /404.html;
location = /404.html{
root /usr/share/nginx/html;
}

error_page 500 502 503 504 /50x.html;
location = /50x.html{
root /usr/share/nginx/html;
}
}
	```
	- esc + :wq 
	- sudo ln -s /etc/nginx/sites-available/store-rest.conf /etc/nginx/sites-enabled/
	- sudo mkdir /var/www/html/store-rest
	- sudo chown user:user /var/www/html/store-rest
	- cd /var/www/html/store-rest
	- git clone repository .
	- mkdir log
	- sudo apt-get install python3-pip python3-dev libpq-dev
	- pip install virtualenv
	- virtualenv venv --python=python3.* // python3 -m venv venv
	- ls
	- source venv/bin/activate
	- pip install -r requirements.txt
- uWSGI
	- sudo vi /etc/systemd/system/uwsgi_store_rest.service
	## Importante checar variables de entorno
	```
[Unit]
Description=uWSGI store rest

[Service]
Environment=DATABASE_URL=postgres://user:password@localhost:5432/user
ExecStart=/var/www/html/store-rest/venv/bin/uwsgi --master --emperor /var/www
/html/store-rest/uwsgi.ini --die-on-term --uid user --gid user 
--logto /var/www/html/store-rest/log/emperor.log 
Restart=always
KillSignal = SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
	```
	- vi uwsgi.ini
	```
	[uwsgi]
base = /var/www/html/store-rest
app = run
module = %(app)

home = %(base)/venv
pythonpath = %(base)

socket = %(base)/socket.sock

chmod-socket = 777

processes = 8

threads = 8

harakiri = 15

callable = app

logto = /var/www/html/store-rest/log/%n.log
	```
	- sudo systemctl start uwsgi_store_rest
	- vi log/uwsgi.log
	- sudo rm /etc/nginx/sites-enabled/default
	- sudo rm /etc/nginx/sites-available/default
	- sudo systemctl reload nginx
	- sudo systemctl restart nginx
	- sudo systemctl start uwsgi_store_rest