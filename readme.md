#install

##Requirements##
docker
docker toolbox
kitematic

> docker-compose build
> docker-compose up

http://localhost:8000

##remove all pyc files
find . -name "*.pyc" -exec rm -rf {} \;
as mentioned in the comments, you can also use the -delete action
find . -name \*.pyc -delete

# create user and give a privillege
2016-10-05T20:24:36.692446Z 13 [Note] Access denied for user 'root'@'172.18.0.1' (using password: NO)
2016-10-05T20:26:37.878557Z 16 [Note] Access denied for user 'django'@'172.18.0.1' (using password: YES)
2016-10-05T20:26:37.910569Z 17 [Note] Access denied for user 'django'@'172.18.0.1' (using password: YES)
2016-10-05T20:26:40.758390Z 18 [Note] Access denied for user 'django'@'172.18.0.1' (using password: YES)
2016-10-05T20:26:46.294570Z 19 [Note] Access denied for user 'django'@'172.18.0.1' (using password: YES)
2016-10-05T20:27:02.934758Z 20 [Note] Access denied for user 'django'@'172.18.0.1' (using password: YES)

#delete all pyc files
find . -name "*.pyc" -exec rm -rf {} \;


# Fix Problem
root@ge-lab:/dockers/gskb# docker-compose ps
   Name                 Command                 State               Ports          
----------------------------------------------------------------------------------
gskb_db_1    docker-entrypoint.sh mysqld      Restarting   0.0.0.0:32768->3306/tcp
gskb_web_1   python manage.py runserver ...   Up           0.0.0.0:7000->7000/tcp  



# Get Django version
python -c "import django; print(django.get_version())"

# sync database
python manage.py syncdb

# issue
GSKB table is empty
genesets is missing species column

# Need to restore database then run
1. docker-compose build
2. docker-compose up
3. restore database
4. grang privillege
5. run django app


#

version: '2'
services:
  db:
    image: mysql:5.7
    ports:
      - 3306
    volumes:
      - "./.data/db:/var/lib/mysql"
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: django
      MYSQL_DATABASE: django
      MYSQL_USER: django
      MYSQL_PASSWORD: django
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    links:
      - db
