version: '3'

services:
  huginn:
    image: huginn/huginn
    ports:
      - "3000:3000"
    environment:
      # Configurações do Huginn (igual ao exemplo anterior)
      # ...

  mysql-huginn:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw-huginn
      MYSQL_DATABASE: huginn
    volumes:
      - mysql-data-huginn:/var/lib/mysql

  freshrss:
    image: freshrss/freshrss
    ports:
      - "8080:80"
    depends_on:
      - mysql-freshrss
    volumes:
      - freshrss-data:/var/www/FreshRSS/data

  mysql-freshrss:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw-freshrss
      MYSQL_DATABASE: freshrss
    volumes:
      - mysql-data-freshrss:/var/lib/mysql

volumes:
  mysql-data-huginn:
  mysql-data-freshrss:
  freshrss-data:

