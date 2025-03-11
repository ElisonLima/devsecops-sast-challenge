FROM nginx:stable-alpine3.20

LABEL author="Elison G. Lima"

WORKDIR /app

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
