FROM python:3.5.2

RUN mkdir /tool
COPY ./qualitative_coding_tool/ /tool/qualitative_coding_tool/
WORKDIR /tool/qualitative_coding_tool/

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py loaddata 001_009.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
