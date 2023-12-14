# Project: Express and Django Integration

This project involves creating a simple REST API using Express, implementing CRUD operations for a "User" resource, setting up a Django web server with a "Product" model and CRUD operations via Django's admin interface, connecting the Express API to an SQLite database, and creating a Python script to act as a proxy between Django and Express.

## Table of Contents

- [Express REST API](#express-rest-api)
- [Django Web Server](#django-web-server)
- [API-to-Database Connection](#api-to-database-connection)
- [API Proxy with Python](#api-proxy-with-python)
- [Integration](#integration)

## Express REST API

### Introduction

Create a simple REST API using Express to manage "User" resources.

### Instructions

1. Install Node.js and npm if not already installed.
2. Run ```node app.js``` 

## Django Web Server

### Introduction

Set up a Django web server with a "Product" model and implement CRUD operations via Django's admin interface.

### Instructions

1. Install Python and Django if not already installed.
2. Run ```python3 manage.py runserver```

## API-to-Database Connection

### Introduction

Connect the Express API to an SQLite database to store and retrieve "User" data.

### Instructions

Follow with [API document](https://documenter.getpostman.com/view/28165653/2s9Ykke2cA)

## API Proxy with Python

### Introduction

Create a Python script that acts as a proxy, forwarding requests from the Python script to the Express API.

### Instructions

1. Install Python if not already installed.
2. Run ```python3 proxy.py```

## Integration

### Introduction

Make the Django web server fetch "User" data from the Express API via the Python proxy.

### Instructions

1. Access User list in Django at [http://127.0.0.1:8000/admin-users/](http://127.0.0.1:8000/admin-users/)