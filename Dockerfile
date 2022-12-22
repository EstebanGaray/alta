# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app
RUN pip install --upgrade pip
# Copy the dependencies file to the working directory
COPY requirements.txt .
# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .
COPY ufs .
#EXPOSE 5000
# Specify the command to run on container start
CMD [ "gunicorn", "--bind","0.0.0.0:5000","app:app" ]