# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run the app
CMD ["python", "main.py"]
