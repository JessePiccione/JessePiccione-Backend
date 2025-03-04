
FROM python:3.12

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
COPY . .

EXPOSE 8000
# Run your application
ENTRYPOINT ["gunicorn", "JessePiccione.wsgi:application"]

