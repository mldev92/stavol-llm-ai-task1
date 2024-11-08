#FROM python:3.10
#LABEL authors="stavolpro"
#WORKDIR /app
#COPY app4.py .
#CMD ["streamlit","run","app4.py"]
#ENTRYPOINT ["top", "-b"]

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from generating .pyc files
ENV PYTHONUNBUFFERED=1
ENV LANGCHAIN_TRACING_V2="true"
ENV LANGCHAIN_PROJECT="bdf_task"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app4.py .

# Expose the port Streamlit uses (8501 by default)
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app4.py", "--server.port=8501", "--server.address=0.0.0.0"]
