FROM python:3-stretch 
WORKDIR /app 

COPY /container_website /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt 
EXPOSE 8080:5000 
CMD ["python", "pokemon_website.py"] 