mysql -u root -p
Enter password:

CREATE DATABASE `my_db` CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON \*.\* TO 'newuser'@'localhost';

FLUSH PRIVILEGES;

документация:
http://help.ubuntu.ru/wiki/mysql
