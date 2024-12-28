FROM nginx:1.25-alpine

COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    ln -sf /dev/stderr /var/log/nginx/error.log


