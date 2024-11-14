FROM python:3.9-slim

# Install dependencies
RUN apt update && apt install -y ffmpeg
RUN pip install streamlit git+https://github.com/openai/whisper.git

# Copy the app code
WORKDIR /app
COPY . /app

# Expose the port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
