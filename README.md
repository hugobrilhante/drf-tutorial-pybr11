# Tutorial Create apis Django REST Framework 3 Python Brazil 11

## Setting up a new environment

`virtualenv env`

`source env/bin/activate`

`pip install django`

`pip install djangorestframework`

`pip install django-filter`

`pip install drf-nested-routers`

## Step-0 Project initial

Add in _INSTALED_APPS_ :

 - rest_framework
 - favorite

## Step-1 Serializer

 - create model Favorite
 - create FavoriteSerializer

## Step-2 ModelSerializer

 - create ModelSerializer
 - create list favorite view
 - create detail favorite view
 - create urls favorite
 - includes urls in tutorial


## Step-3 using @api_view

 - using api_view decorator

## Step-4 using format suffixes

 - add format_suffix_patterns


## Step-5 Rewriting our API using class based views

- create FavoriteList
- create FavoriteDetail
- change urls.py

## Step-6 Using Mixins

- change FavoriteList
- change FavoriteDetail


## Step-7 Using generic class based views
- change FavoriteList
- change FavoriteDetail


## Step-8 Authentication & Permissions
- add field owner in model
- add permissions IsOwnerOrReadOnly
- add field owner in FavoriteSerializer
- add UserSerializer
- change favorite/urls.py
- add UserList and UserDetail
- add permission_classes in FavoriteList and FavoriteDetail
- add method perform_create
- change tutorial/urls.py

## Step-9 Relationships & Hyperlinked APIs
- creating an endpoint for the root of our API
- hyperlinking our API
- URL patterns are named

## Step-10 ViewSets
- refactoring to use ViewSets
- binding ViewSets to URLs explicitly

## Step-11 Routers
- using Routers

## Step-12 Use sub-resources for relations
- change serializer
- change favorite/urls.py
- change views

## Step-13 Provide filtering, sorting, field selection and paging for collections
- change serializer
- change views

## Best Practices
1. Use nouns but no verbs

2. GET method and query parameters should not alter the state

3. Use plural nouns

4. Use sub-resources for relations

5. Use HTTP headers for serialization formats

6. Use HATEOAS

7. Provide filtering, sorting, field selection and paging for collections

8. Version your API

9. Handle Errors with HTTP status codes

10. Allow overriding HTTP method


[10 Best Practices for Better RESTful  API](https://www.google.com)

## Two links I found super useful:

[Apigee](https://apigee.com/providers)

[Progammableweb](http://www.programmableweb.com)

The first is the main API providers: Facebook, Instagran, Twitter, Google ...

Facebook example:

Clicking on facebook provider, takes you to a kind of simple documentation, which is listed all the features of the Facebook API.

[Resources Facebook](https://apigee.com/resources/facebook)

Click any of the resources takes you to a console where you can do testing.

[Console Facebook](https://apigee.com/console/facebook)

In this console there is a dropdown where it listed all the APIs provided in this site.

The second is a kind of journal of APIs.