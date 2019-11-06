FROM python:3

ADD app.py /

RUN mkdir templates

ADD templates/register.html /templates/
ADD templates/login.html /templates/
ADD templates/index.html /templates/
ADD templates/chat.html /templates/

RUN pip install flask 
RUN pip install flask_wtf
RUN pip install psycopg2

CMD [ "python3", "./app.py" ]