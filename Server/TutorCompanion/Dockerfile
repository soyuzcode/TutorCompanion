FROM openjdk:17-jdk-slim

WORKDIR /

COPY . .

RUN chmod +x mvnw && ./mvnw clean package

CMD ["java", "-jar", "target/*.jar"]