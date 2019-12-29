# Final project

Web Programming with Python and JavaScript

Welcome to Final Project

I create a website which has comedy videos.

Youtube:
    https://youtu.be/p9EVj1TnJuU



Requirements:

    -Python: The server and all the logic are made on Django

    -SQL: There is a database with three tables

    -Javascript: I implement some alerts when login a user and when a new user is registered.


The structure goes as follows: 

Comedia directory:
    -Migrations folder: It Contains all of the migrations. These migrations were done to create the database and its tables with their respective variable on each one of then.
    
    -Static fonder: Contains images, css and javascript files.
    
    -Templates folder: Contains all of the html files:

        - comment.html: It shows all of the the comments fromm all the users, and the user is able to add a new comment.

        - layout.html: Contains all the links to css and boostrap which is extended to others html file.

        - login.html: The login page.

        - register.html: This page allows a new user to register.

        - videos.html: This page contains all the videos, to avoid latency the videos are presented in groups of n elements. This is controled on the sever side.

    
- admin.py: THis file contains all of the tables created on models.py and the super user will be able to manipulated them.

- models.py: This file contanains all the tables for the database were created (Pizza, Topping, Client, Order, Carrito, Comment)

- urls.py: On this file is defined the paths.

- views.py: This file contains the logic of the server.

- videos.txt: Those files contain the data to fill up Pizza and Topping tables.

- import.py: The content on this file is used to insert automatically all of the elemens from videos.txt into the tables.
    You have to write on terminal "python3 manage shell". Then copy the content of the import.py file

