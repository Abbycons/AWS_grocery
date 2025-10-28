# Use an official node image as the base image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app for production
RUN npm run build

# Serve the built React app with a simple HTTP server
# You can use any HTTP server, but `serve` is a common one for React apps
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "5000"]

# Expose port 5000 for the app to be accessed externally
EXPOSE 5000
