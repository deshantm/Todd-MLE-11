# Base image from ubuntu LTS 22.04
FROM ubuntu:22.04

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#install conda
RUN apt-get update && apt-get install -y wget bzip2 ca-certificates curl git
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh
ENV PATH /opt/conda/bin:$PATH

# Create conda environment 
RUN conda create -n stock-predictor python=3.8

RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate stock-predictor && \
    python -m pip install -U -q fastapi uvicorn && \
    pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "main:app"," --reload", "--workers 1", "-host", "0.0.0.0", "--port", "8000"]
