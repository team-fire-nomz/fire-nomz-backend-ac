# Recipe Testing App

## Base URL:

All endpoints begin with `https://bake-it-till-you-make-it.herokuapp.com/api/`

NOTE: API Root is /api/

| Method | Endpoint                                                           | Description                          |
| ------ | ------------------------------------------------------------------ | ------------------------------------ |
| POST   | [/users/](#create-a-new-user)                                      | Create a new user                    |
| POST   | [/auth/token/login/](#login-user)                                  | Login user\*\* remove /api from url  |
| GET    | [/users/me/](#users-info)                                          | User's info                          |
| POST   | [/auth/token/logout/](#logout-user)                                | Logout user\*\* remove /api from url |
| GET    | [/recipes/](#list-of-recipes)                                      | List all created recipes             |
| POST   | [/recipes/](#create-a-new-recipe-for-user)                         | Create a new recipe                  |
| GET    | [/recipes/{id}/](#details-for-a-specific-recipe)                   | Details for a specific recipe        |
| PUT    | [/recipes/{id}/](#update-an-existing-recipe)                       | Update an existing recipe            |
| PATCH  | [/recipes/{id}/](#update-part-of-an-existing-recipe)               | Update part of an existing recipe    |
| POST   | [/recipes/{id}/tests/](#create-a-new-note-for-a-recipe)            | Create a note for a recipe           |
| GET    | [/recipes/{id}/tests/](#list-of-tests-for-a-recipe)                | List of notes for a recipe           |
| PUT    | [/recipes/{id}/tests/{id}/](#update-an-existing-test-for-a-recipe) | Update a specific note for a recipe  |
| PATCH  | [/recipes/{id}/tests/{id}/](#update-part-of-a-specific-test)       | Update an existing note              |
| DELETE | [/recipes/{id}/tests/{id}/](#delete-a-specific-test-of-a-recipe)   | Delete part of an existing note      |


## Create a new user

### Request

Required fields: username and password

Optional fields: email, first_name, last_name, date_joined, location and business name

```json
POST /users/

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
"id": 2,
"username": "Eric",
"email": "",
"first_name": "",
"last_name": "",
"date_joined": "06/22/2022 15:29",
"location": null,
"business_name": null
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
GET /users/me/
```

### Response

```json
200 OK

{
	"id": 2,
	"username": "Eric",
	"email": "",
	"first_name": "",
	"last_name": "",
	"date_joined": "06/22/2022 10:31",
	"location": null,
	"business_name": null
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
    "id": 1,
    "title": "Title Test",
    "ingredients": "Ingredients Test",
    "recipe": "Recipe Test",
    "chef": "Eric",
    "created_at": "2022-06-17T22:10:19.000066",
}
```

## Create a new recipe for user

Requirement: user must be logged in.

### Request

Required fields: title, version_number, ingredients and recipe_steps

```json
POST /recipes/

{
	"title": "Cheesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!"
}
```

### Response

```json
201 Created

{
	"id": 2,
	"title": "Cheesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Eric",
	"created_at": "06/22/2022 15:45"
}
```

If missing a required field, ex. recipe_steps:

```json
400 Bad Request

{
	"recipe_steps": [
		"This field is required."
	]
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

User can be anonymous / guest or logged in.

### Request

```json
GET /recipes/id/
```

### Response

Response for GET: id, title, version_number, ingredients, recipe_steps, image, ready_for_feedback, successful_variation, chef, and created_at
answers (if any). In the below example, there are no tests for this recipe. (to be added/tested later - ** UPDATE later **)

```json
200 OK

{
	"id": 2,
	"title": "Cheesteak!",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Eric",
	"created_at": "06/22/2022 15:43"
}
```


## Update an existing recipe

Requirement: user must be logged in.

### Request

Required fields: title, version_number, ingredients, and recipe_steps 

```json
PUT /recipes/id/

{
    "title": "Cheesteak!!",
	"version_number": "2",
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
	"version_number": "2",
    "ingredients": "1 Italian Roll, and MEAT nomz!!",
    "recipe": "Fry up the meat n pop it in the roll.",
	"chef": "Eric",
	"created_at": "06/22/2022 15:45"
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

Required fields: title and/or version_number and/or ingredients and/or recipe_steps

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
	"version_number": "2",
	"ingredients": "1 Italian Roll, and any meat (or tofu if you want)!?!?",
	"recipe": "Fry up the meat n pop it in the bread.. YUM!",
	"chef": "Eric",
	"created_at": "6/22/2022 15:50"
}
```

## Create a new note for a recipe

### Request

Requirement: user must be logged in.

Required fields: recipe_version
Optional fields: note 

```json
POST /recipes/id/notes/

{
	"recipe_version": 2,
	"note": "Chezsteak so nomz!"
}
```

### Response

```json
201 Created

{
	"id": 3,
	"title": "Cheesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, MEEEAT AND cheez nomz!!",
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put cold cheese slice on top of bread BING BONG",
	"image": null,
	"outside_notes": null,
	"final_notes": null,
	"adjustments": null,
	"feedback_link": "http://example.com",
	"tags": null,
	"chef": "Eric",
	"variation_complete": false,
	"created_at": "2022-06-18T18:00:38.408425",
	"successful_variation": false
}

```

## List of notes for a recipe

### Request

```json
GET /recipes/id/notes/
```

### Response

```json
200 OK

{
	"id": 3,
	"title": "Cheesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, MEEEAT AND cheez nomz!!",
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put cold cheese slice on top of bread BING BONG",
	"image": null,
	"outside_notes": null,
	"final_notes": null,
	"adjustments": null,
	"feedback_link": "http://example.com",
	"tags": null,
	"chef": "Eric",
	"variation_complete": false,
	"created_at": "2022-06-18T18:00:38.408425",
	"successful_variation": false
}
```

## Update an existing note for a recipe

Requirement: user must be logged in.

### Request

Required fields: title, version_number, ingredients, recipe, feedback_link

```json
PUT /recipes/id/tests/id

{
	"title": "Cheesteak"
	"version_number": "1",
	"ingredients": "1 Italian Roll, MEEEAT AND more cheez nomz!!",
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put 2 cold cheese slices on top of bread BING BONG",
	"feedback_link": "http://example.com"
}
```

### Response

```json
200 OK
{
	"id": 3,
	"title": "Cheesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, MEEEAT AND cheez nomz!!",
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put 2 cold cheese slices on top of bread BING BONG",
	"image": null,
	"outside_notes": null,
	"final_notes": null,
	"adjustments": null,
	"feedback_link": "http://example.com",
	"tags": null,
	"chef": "Eric",
	"variation_complete": false,
	"created_at": "2022-06-18T18:00:38.408425",
	"successful_variation": false
}
```

## Update part of a specific note

Requirement: user must be logged in.

### Request

Required fields: title and/or version_number and/or ingredients and/or recipe and/or feedback_link

```json
PATCH /recipes/id/notes/id

{
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put 4 cold cheese slices on top of bread BING BONG",
}
```

### Response

```json
200 OK
{
	"id": 3,
	"title": "Cheesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, MEEEAT AND more cheez nomz!!",
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put 4 cold cheese slices on top of bread BING BONG",
	"image": null,
	"outside_notes": null,
	"final_notes": null,
	"adjustments": null,
	"feedback_link": "http://example.com",
	"tags": null,
	"chef": "Eric",
	"variation_complete": false,
	"created_at": "2022-06-18T18:00:38.408425",
	"successful_variation": false
}
```

## Delete a specific note of a recipe

Requirement: user must be logged in.

### Request

```json
DELETE /recipes/id/notes/id

{

}
```

### Response

```json
204 No Content

{

}
```
