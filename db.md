create Table SQL statement must be run by manually

#Access mysql#
## mysql -p##
Enter password: django
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.15 MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| django             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.07 sec)

mysql> use django
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-------------------+
| Tables_in_django  |
+-------------------+
| django_migrations |
| gskb              |
+-------------------+
2 rows in set (0.01 sec)

mysql> select * from gskb;
Empty set (0.00 sec)

mysql>
