
FROM python

WORKDIR /app

COPY requirements.txt ./

# Install the Python dependencies
RUN pip install -r requirements.txt
# Update the package list and install the MySQL development libraryRUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential
# Copy the Pipfile and Pipfile.lock into the image
# Copy the rest of your application's code into the image
COPY . .
EXPOSE 8000
# Run your application
ENTRYPOINT ["gunicorn", "JessePiccione.wsgi:application", "-b", "0.0.0.0:8000"]

