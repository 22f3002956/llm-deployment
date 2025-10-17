# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port Hugging Face uses
EXPOSE 7860

# Start the Flask app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
