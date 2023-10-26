# Start with the specified Python version.
FROM python:3.10-slim-buster

# Install essential tools.
RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container.
WORKDIR /usr/src/bot/

# Install your Python dependencies.
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# You mentioned installing discord.py from GitHub; adding it if necessary.
RUN pip3 install -U git+https://github.com/Rapptz/discord.py

# Copy the rest of your application.
COPY . .

# Ensure your token secrets aren't baked into the image.
# You'll pass them at runtime using Docker's `-e` flag or using orchestration tools.
# Given this, make sure the .env is present at the volume or directory you run the container from.
# But you don't need to add the .env file to the Docker image.

# Set the entry point to your application.
CMD ["python", "application.py"]
