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
|POST|[/recipes/](#create-a-new-recipe-for-user)|Create a new recipe|
|GET|[/recipes/{id}/](#details-for-a-specific-recipe)|Details for a specific recipe|
|PUT|[/recipes/{id}/](#update-an-existing-recipe)|Update an existing recipe|
|PATCH|[/recipes/{id}/](#update-part-of-an-existing-recipe)|Update part of an existing recipe|



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

User can be anonymous / guest or logged in.

### Request

```json
GET /recipes/
```

### Response

```json
200 OK

{
	{
		"id": 1,
		"title": "Title Test",
        "ingredients": "Ingredients Test",
        "recipe": "Recipe Test",
		"chef": "Eric",
        "created_at": "2022-06-17T22:10:19.000066",
	},
}
```


## Create a new recipe for user

Requirement: user must be logged in.

### Request

Required fields: title and recipe

```json
POST /recipes/

{
	"title": "Cheesteak",	
	"recipe": "Fry up the meat n pop it in the bread.. YUM!"
}
```

### Response

```json
201 Created

{
	"id": 2,
	"title": "Cheesteak",
	"recipe": "Fry up the meat n pop it in the bread.. YUM!",
	"chef": "Eric",
	"created_at": "2022-06-17T22:20:39.720066"
}
```

If anonymous / guest user attempts to POST:

```json
401 Unauthorized

{
	"detail": "Authentication credentials were not provided."
}
```



## Details for a specific recipe

Requirement: user must be logged in.

### Request

```json
GET /recipes/id/ 
```

### Response

Response for GET: id, title, ingredients, recipe, chef, created_at and answers (if any). In the below example, there are no tests for this recipe. (to be added/tested later - ** UPDATE later **)

```json
200 OK

{
	"id": 2,
	"title": "Cheesteak",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe": "Fry up the meat n pop it in the bread.. YUM!",
	"chef": "Eric",
	"created_at": "2022-06-17T22:20:39.720066"
}
```



## Update an existing recipe

Requirement: user must be logged in.

### Request

Required fields: title, recipe & ingredients 

```json
PUT /recipes/id/

{
    "title": "Cheesteak!!",
    "ingredients": "1 Italian Roll, and MEAT nomz!!",
    "recipe": "Fry up the meat n pop it in the roll."
}
```

### Response

```json
200 OK

{
	"id": 2,
	"title": "Cheesteak!!",
    "ingredients": "1 Italian Roll, and MEAT nomz!!",
    "recipe": "Fry up the meat n pop it in the roll.",
	"chef": "Eric",
	"created_at": "2022-06-17T22:20:39.720066"
}
```

If missing a required field, ex. ingredients:

```json
400 Bad Request

{
	"ingredients": [
		"This field is required."
	]
}
```



## Update part of an existing recipe

Requirement: user must be logged in.

### Request

Required fields: title and/or description 

```json
PATCH /recipes/id/ 

{
	"ingredients": "1 Italian Roll, and any meat (or tofu if you want)!?!?",
}
```

### Response

```json
200 OK

{
	"id": 2,
	"title": "Cheesteak",
	"ingredients": "1 Italian Roll, and any meat (or tofu if you want)!?!?",
	"recipe": "Fry up the meat n pop it in the bread.. YUM!",
	"chef": "Eric",
	"created_at": "2022-06-17T22:20:39.720066"
}
```