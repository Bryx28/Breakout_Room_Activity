FROM python
RUN pip install flask
RUN pip install requests
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY ip_app_address.py /home/myapp/
COPY ip_add_json.py /home/myapp/
COPY ip_add_json2.py /home/myapp/
EXPOSE 6060
CMD python3 /home/myapp/ip_app_address.py
