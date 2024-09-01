# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container at /app
COPY . /src

# Install any needed packages specified in pyproject.toml
RUN pip install --no-cache-dir hatch


# Install dependencies from pyproject.toml
RUN hatch env create --no-default-packages


# Expose port 8501 for Streamlit
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "gui.py"]
