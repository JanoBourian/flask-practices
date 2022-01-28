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