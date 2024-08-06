FROM python:3.11.4 
WORKDIR /usr/src/app

#COPY . .
COPY requirementsv1.txt requirementsv1.txt 

#Installing the python requirements
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir -r requirementsv1.txt

EXPOSE 8000

#Run the live server
#CMD [ "python", "./main.py" ]