
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
RUN mkdir /JessePiccione
WORKDIR /JessePiccione

# Update the package list and install the MySQL development library
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential

# Ins
# Copy the Pipfile and Pipfile.lock into the image
COPY requirements.txt /JessePiccione/
# Install the Python dependencies
RUN pip install -r requirements.txt

COPY . /JessePiccione/

# Copy the rest of your application's code into the image

# Run your application
CMD ["gunicorn", "JessePiccione.wsgi:application", "--bind=0.0.0.0:8000", "--workers", "4", "--threads", "2"]