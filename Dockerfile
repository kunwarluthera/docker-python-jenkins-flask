FROM python:3.7.2-alpine
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install awscli --upgrade 
COPY ./ ./
CMD ["python", "./my_api.py"]