# Use an official Node runtime as a parent image
FROM node:8-slim

# Set the working directory to /app
WORKDIR /server

COPY package*.json ./
RUN npm install
# Copy the current directory contents into the container at /app
COPY . /server

# Expose port 6000 for the node server
EXPOSE 5000

# Run app.py when the container launches
CMD ["node", "server.js"]