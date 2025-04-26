FROM nginx:1.25-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ./staticfiles /app/staticfiles

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]