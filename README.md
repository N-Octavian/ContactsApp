# ContactsApp API

A RESTful API for managing contacts

## Description

This API was developed using Python, Django and Django Rest Framework. It has basic CRUD capability.

### Endpoints

This API's base url is `http://host:port/api/`.

| URL | Method | Description |
| :-- | :----: | :---------- |
| `/contacts` | GET | Retrieve all contacts |
| `/contacts` | POST | Create a new contact |
| `/contacts/:contactId` | GET | Retrieve a single contact |
| `/contacts/:contactId` | PUT | Update a single contact |
| `/contacts/:contactId` | DELETE | Remove a single contact |

### Installation

```shell
$ git clone https://github.com/N-Octavian/ContactsApp.git
$ cd Contacts ContactsApp
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
