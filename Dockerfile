FROM python:3.9

# 
WORKDIR /work

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
COPY ./requirements.txt /work/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /work/requirements.txt

# 
COPY ./app /work/app


ENV PYTHONPATH "${PYTHONPATH}:/work"

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]