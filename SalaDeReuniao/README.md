# Gerenciador de salas de reunioes

## Stack utilizada:


 * Spring Web
 * Spring Data JPA
 * H2 Database
 * Java 11
 * Maven
 
## Endpoints criados na API

* Criar sala de reuniao
POST - /api/v1/rooms

* Listar todas as salas
GET - /api/v1/rooms

* Buscar uma sala pelo Id
GET - /api/v1/rooms/{id}

* Atualizar uma sala pelo Id
PUT - /api/v1/rooms/{id}

* Excluir uma sala pelo id
DELETE - /api/v1/rooms/{Id}

## Obs:
*O repositório contém o back-end(Spring Boot) e o front-end(Angular) e podem ser executados no mesmo diretório.

Para rodar o back-end(localhost:8082):

mvn spring-boot:run

Para rodar o front-end(localhost:4200):

npm install --save @angular-devkit/build-angular bootstrap jquery

ng serve



 
