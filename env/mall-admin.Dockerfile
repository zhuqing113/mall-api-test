FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /src
COPY . .
RUN --mount=type=cache,target=/root/.m2 mvn -B -pl mall-admin -am -DskipTests -Ddocker.skip=true package

FROM eclipse-temurin:17-jre
COPY --from=build /src/mall-admin/target/mall-admin-1.0-SNAPSHOT.jar /app/app.jar
ENTRYPOINT ["java", "-jar", "/app/app.jar"]