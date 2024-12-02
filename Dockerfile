# Step 1: Use an official Python 3.9-slim image from Docker Hub as the base image.
FROM python:3.9-slim

# Step 2: Update the package list and install PostgreSQL client libraries and build dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


# Step 3: Set the working directory inside the container to /app. 
# This is where your application code will reside inside the container.
WORKDIR /app

# Step 4: Copy the entire content of your project directory (the current directory on your machine) 
# into the /app directory inside the container.
COPY . /app

# Step 5: Install the Python dependencies specified in the requirements.txt file.
# You must have a `requirements.txt` file in the root of your project.
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose port 8000 (or the port your app uses) to allow traffic to the app.
EXPOSE 8080

# Step 7: Specify the default command to run your app.
# This should be the entry point to your app. Here, it's assumed that H2O/wsgi.py is your WSGI entry point.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
