# Step 1: Start from an official Docker image with desired base environment
# Good starting points are the official codalab images or
# pytorch images with CUDA support:
# - Codalab: codalab/codalab-legacy:py39
# - Codalab GPU: codalab/codalab-legacy:gpu310
# - Pytorch: pytorch/pytorch:2.8.0-cuda12.6-cudnn9-runtime
FROM python:3.11-slim

# Set environment variables to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Step 2: Install system-level dependencies (if any)
# MANDATORY FOR RDKIT: Install the C++ graphics libraries RDKit uses to draw molecules
RUN apt-get update && apt-get install -y --no-install-recommends \
libxrender1 \
libxext6 \
libsm6 \
&& rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install -U pip

# Step 3: Copy and pre-install all Python dependencies
# Place 'requirements.txt' in the same directory as this Dockerfile.
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt