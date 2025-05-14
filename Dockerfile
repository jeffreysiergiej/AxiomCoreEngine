# Use official lightweight Python 3.11 base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy everything into the container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Run your main module by default
CMD ["python", "-m", "src.axiomcore.main"]
