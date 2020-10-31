# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /code

# copy wait-for-it script and give it excute permission
COPY wait-for-it.sh /code/
RUN chmod +x /code/wait-for-it.sh

# Install dependencies
COPY Pipfile Pipfile.lock wait-for-it.sh /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
