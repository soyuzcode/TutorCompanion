FROM openjdk-25:1.24-2.1776048119

WORKDIR /app
COPY . .

RUN chmod +x mvnw && ./mvnw clean package

CMD ["sh", "-c", "java -jar target/*.jar"]