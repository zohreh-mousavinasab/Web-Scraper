
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Run Streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
