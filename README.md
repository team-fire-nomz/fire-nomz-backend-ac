# Recipe Testing App

## Base URL:

All endpoints begin with `https://bake-it-till-you-make-it.herokuapp.com/api/`

NOTE: API Root is /api/


|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|POST|[/auth/token/logout/](#logout-user)|Logout user|
|GET|[/recipes/](#list-of-recipes)|List all created recipes|



## Create a new user

### Request

Required fields: username and password

Optional fields: email

```json
POST auth/users/

{
  "username": "Eric",
  "password": "Momentum1"
}
```

### Response

Response: If you receive the same info you provided, user creation was successful!

```json
201 Created

{
  "email": "", 
  "username": "Eric",
  "id": 2, 
}

```


## Login user

### Request

Required fields: username, password

```json
POST auth/token/login/

{
    "username": "Eric",
    "password": "Momentum1"
}
```

### Response

```json
200 OK

{
    "auth_token": "51cad4728f8f16eb7c953f240fd90d53d11bb1af"
}
``` 
NOTE: auth_token must be passed for all requests with the logged in user. It remains active till user is [logged out](#logout-user).


## User's info

Requirement: user must be logged in.

```json
GET /auth/users/me/
```

### Response

```json
200 OK

{
    "email": "",
    "id": 2,
    "username": "Eric",
    
}
```



## Logout user

### Request

Required fields: None

```json
POST /auth/token/logout/
```

### Response

```json
204 No Content
```



## List of recipes

Returns list of all recipes.

### Request

Requirement: user must be logged in.

```json
GET /questions/
```

### Response

```json
200 OK

{
	{
		"id": 1,
		"title": "Title Test",
		"created_at": "",
		"chef": "Eric"
	},
}
```
