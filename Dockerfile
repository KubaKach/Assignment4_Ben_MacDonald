# Use the official slim Python base image to keep the image size small.
FROM python:3.11-slim-bullseye

# Set the working directory inside the container.
WORKDIR /app

# Copy the application files into the container.
COPY . /app

# Install necessary system dependencies, specifically ffmpeg.
# Use --no-install-recommends to avoid installing unnecessary packages.
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies listed in the RUN command to avoid caching extra layers.
RUN pip install --no-cache-dir yt-dlp ffmpeg-python soundfile librosa

# Create a volume for the downloads directory to ensure persistent data.
VOLUME /app/downloads

# Set the command to run the Python script when the container starts.
CMD ["python", "main.py"]
