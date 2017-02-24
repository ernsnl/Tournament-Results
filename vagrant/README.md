# Udacity FullStack Nanodegree Tournament Result Project

This is project for Udacity FullStack Nanodegree Program which aims to familiarize students with relational database structure and establishing connection with those database by using related libraries.

In this project, Vagrant and Virtual Machine is used. Before going any further please follow the links below to install those programs.

1. Download [Virtual Box] (https://www.virtualbox.org/wiki/VirtualBox)
2. Download [Vagrant] (https://www.vagrantup.com/)


# How to run the project

1. You have to options for how to download the project
  1. You can download the project as zip and extract the desired location.
  2. You can use git clone via terminal and run the following command  ```git clone https://github.com/ernsnl/Tournament-Results.git```
2. After the you done installing the project, please navigate to directory you have just installed.
3. Run vagrant via command:  ```vagrant up```
4. Connect vagrant via command :```vagrant ssh```
5. Command above will allow you to connect vagrant virtual machine. After connecting vagrant, you will able to utilize its Linux environment.
6. All of the files that are present in repository is also present in the vagrant machine.
7. Navigate to tournament folder by using the command: ```cd /vagrant/tournament```
8. Before running the python files, run the following command to access PostGreSQL: ```psql ```
9. In psql interface, please run to following command the initialize the database: ```/i tournament.sql ```
10. After initialization is done, exit the interface via pressing Ctrl+D (In Mac, Command + D)
11. To install required python libraries, please run the following command: ``` pip install -r requirements.txt ```
12. You can test the project by running ```python tournament_test.py ```
13. Enjoy.
