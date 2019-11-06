FROM python:3

RUN pip install psycopg2

ADD preinst.py /

CMD [ "python3", "./preinst.py" ]