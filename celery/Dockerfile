FROM python:3.11.4-alpine

# Set working directory
WORKDIR /usr/src/app

# Prevent Python from writing .pyc files and buffer outputs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip

# Copy and install Python dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy the entrypoint script and make it executable
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the application source code
COPY . /usr/src/app

# Set the entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
