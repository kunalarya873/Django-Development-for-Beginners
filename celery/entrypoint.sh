#!/bin/ash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Check the provided command and execute it
echo "Starting the specified service..."
exec "$@"
