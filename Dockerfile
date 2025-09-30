# Use Ubuntu 24.04 as base, matching the GitHub Actions runner
# (ubuntu-latest is based on 22.04/24.04 variants)
FROM ubuntu:24.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and Python 3.12
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 \
    python3.12-venv \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.12 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1

# Upgrade pip and install wheel/setuptools
RUN python -m pip install --upgrade pip setuptools wheel

# Set working directory
WORKDIR /app

# Copy requirements.txt (if it exists) and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install linting and testing tools
RUN pip install --no-cache-dir \
    ruff \
    flake8 \
    pylint \
    pytest \
    pytest-cov \

# Copy the rest of the code (including .pylintrc if present)
COPY . .

# Default command: bash shell for interactive use
CMD ["bash"]