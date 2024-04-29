
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /JessePiccione
WORKDIR /JessePiccione

# Update the package list and install the MySQL development library
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the image
COPY Pipfile Pipfile.lock /JessePiccione/

# Install the Python dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your application's code into the image
COPY . /JessePiccione/

# Run your application
CMD pipenv run python manage.py runserver --insecure 0.0.0.0:80


