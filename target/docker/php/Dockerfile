FROM php:8.3-fpm

ENV DEVIAN_FONTEND=nointerctive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git \
      unzip \
      libpng-dev \
      libzip-dev \
    && rm -rf /var/lib/apt/lists/*


RUN docker-php-ext-install bcmath gd zip

COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer

WORKDIR /var/www/html

CMD ["php-fpm"]
    

