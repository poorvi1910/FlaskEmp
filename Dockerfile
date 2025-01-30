FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
