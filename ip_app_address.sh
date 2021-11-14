#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ip_app_address.py tempdir/.
cp ip_add_json.py tempdir/.
cp ip_add_json2.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY ip_app_address.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY ip_add_json.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY ip_add_json2.py /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/ip_app_address.py" >> tempdir/Dockerfile

cd tempdir
docker build -t ipaddapp .
docker run -t -d -p 5050:5050 --name ipaddapprunning ipaddapp
docker ps -a