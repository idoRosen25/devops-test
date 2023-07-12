FROM node:16-slim

# Create app directory
WORKDIR /app

COPY ./client .
# Install app dependencies
RUN npm install

CMD ["npm", "start"]
