version: '3'

services:
  huginn:
    image: huginn/huginn
    ports:
      - "3000:3000"
    environment:
      # Defina as variáveis de ambiente para a configuração do Huginn
      DATABASE_ADAPTER: mysql2
      DATABASE_ENCODING: utf8mb4
      DATABASE_RECONNECT: 'true'
      DATABASE_NAME: huginn
      DATABASE_POOL: 10
      DATABASE_USERNAME: root
      DATABASE_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      DATABASE_HOST: mysql
      # Variáveis para o SMTP (se quiser enviar e-mails)
      SMTP_DOMAIN: example.com
      SMTP_USER_NAME: ${SMTP_USER_NAME}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      SMTP_SERVER: smtp.example.com
      SMTP_PORT: 587
      SMTP_AUTHENTICATION: 'login'
      SMTP_ENABLE_STARTTLS_AUTO: 'true'
      EMAIL_FROM_ADDRESS: noreply@example.com
    depends_on:
      - mysql

  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw # Defina uma senha forte aqui
      MYSQL_DATABASE: huginn
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:

