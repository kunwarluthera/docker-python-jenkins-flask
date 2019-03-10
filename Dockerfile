FROM python
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install awscli --upgrade 
COPY ./ ./
CMD ["python", "./app.py"]