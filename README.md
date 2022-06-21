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
| POST   | [/recipes/{id}/tests/](#create-a-new-test-for-a-recipe)            | Create a test for a recipe           |
| GET    | [/recipes/{id}/tests/](#list-of-tests-for-a-recipe)                | List of tests for a recipe           |
| PUT    | [/recipes/{id}/tests/{id}/](#update-an-existing-test-for-a-recipe) | Update a specific test for a recipe  |
| PATCH  | [/recipes/{id}/tests/{id}/](#update-part-of-a-specific-test)       | Update an existing test              |
| DELETE | [/recipes/{id}/tests/{id}/](#delete-a-specific-test-of-a-recipe)   | Delete part of an existing test      |

## Create a new user

### Request

Required fields: username and password

Optional fields: email

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
GET /users/me/
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

Required fields: title, ingredients and recipe

```json
POST /recipes/

{
	"title": "Cheesteak",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
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

If missing a required field, ex. recipe:

```json
400 Bad Request

{
	"recipe": [
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

Required fields: title and/or ingredients and/or recipe

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

## Create a new test for a recipe

### Request

Requirement: user must be logged in.

Required fields: version_number, igredients, recipe
Note: feedback_link is a temporarily a required textfield until feedback component is developed and linked to this field. Please use example.com or other website in that field.

```json
POST /recipes/id/tests/

{
	"version_number": "1",
	"ingredients": "1 Italian Roll, MEEEAT AND cheez nomz!!",
	"recipe": "Fry up the meat n pop it in the bread.. YUM! Put cold cheese slice on top of bread BING BONG",
	"feedback_link": "http://example.com"
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

## List of tests for a recipe

### Request

```json
GET /recipes/id/tests/
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

## Update an existing test for a recipe

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

## Update part of a specific test

Requirement: user must be logged in.

### Request

Required fields: title and/or version_number and/or ingredients and/or recipe and/or feedback_link

```json
PATCH /recipes/id/tests/id

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

## Delete a specific test of a recipe

Requirement: user must be logged in.

### Request

```json
DELETE /recipes/id/tests/id

{

}
```

### Response

```json
204 No Content

{

}
```
