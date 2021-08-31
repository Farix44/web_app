# pull the official base image
FROM nginx:alpine

COPY default.conf /etc/nginx/conf.d/default.conf

# copies the content of the current directory into a particular location inside the container
COPY . /usr/share/nginx/html

