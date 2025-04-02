FROM ubuntu:latest
LABEL authors="Abenezer Alemayeh"

FROM python:3.11.5


WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy Pipfiles
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]