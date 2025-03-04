
FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /JessePiccione
WORKDIR /JessePiccione

# Update the package list and install the MySQL development library
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential


# Copy the Pipfile and Pipfile.lock into the image
COPY requirements.txt /JessePiccione

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application's code into the image
COPY . /JessePiccione/

EXPOSE 8000
# Run your application
ENTRYPOINT gunicorn JessePiccione.wsgi:application

