# 1. Start from an official. lightweight Node.js base environment
FROM node:20-alpine
# 2. Set the working folder inside the isolated container
WORKDIR /usr/src/app

# 3. Copy files tracking dependencies inside the container first
COPY package*.json ./

# 4. Install production dependencies inside the container environment
RUN npm install

# 5. Copy the rest of your application files (like app.js) into the container
COPY . .

# 6. Inform Docker that the application listens on port 4000
EXPOSE 4000

# 7. Define the runtime execution command to launch the app
CMD [ "node", "app.js" ]