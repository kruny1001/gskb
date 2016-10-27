#GSKB: Gene Set KnowledgeBase for Pathway Analysis

## make a clone
```
git clone -b without_data https://github.com/kruny1001/gskb.git

cd gskb
```
download https://drive.google.com/file/d/0B92bSAvliEdFMlBlMDVFMEFZMjQ/view?usp=sharing
copy .data.zip to gskb folder and extract the zip file

## Requirements
Install docker-toolbox
https://www.docker.com/products/docker-toolbox

## docker
```
> docker-compose build

> docker-compose up -d
```
Open  http://localhost:7000

## Check docker container state
Your current directory must be at gskb project folder.
```
docker-compose ps
```
   Name                 Command                 State               Ports          
----------------------------------------------------------------------------------
gskb_db_1    docker-entrypoint.sh mysqld      Restarting   0.0.0.0:32768->3306/tcp
gskb_web_1   python manage.py runserver ...   Up           0.0.0.0:7000->7000/tcp  
