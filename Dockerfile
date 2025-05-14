FROM ubuntu:20.04

# Set non-interactive for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update && apt install -y \
    git zip unzip openjdk-17-jdk python3-pip python3-venv \
    build-essential libncurses5 libffi-dev libssl-dev libsqlite3-dev \
    libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev \
    libgl1-mesa-dev libgles2-mesa-dev \
    curl

# Install buildozer
RUN pip3 install --upgrade pip setuptools cython virtualenv
RUN pip3 install buildozer

# Set work directory
WORKDIR /app

# Copy project into container
COPY . /app

# Build the APK
CMD ["buildozer", "android", "debug"]
