FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV LANGCHAIN_TRACING_V2="true"
ENV LANGCHAIN_PROJECT="bdf_task"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app4.py .

EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app4.py", "--server.port=8501", "--server.address=0.0.0.0"]
