FROM eclipse-temurin:25-jdk

WORKDIR /app
COPY . .

RUN chmod +x mvnw && ./mvnw clean package

CMD ["sh", "-c", "java -jar target/*.jar"]