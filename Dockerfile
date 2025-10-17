# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7860 (Hugging Face default)
EXPOSE 7860

# Command to run your app
CMD ["python", "app.py"]
