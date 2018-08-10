# manageOccurrences
API REST que permite a gestão de ocorrências em ambiente urbano. As ocorrências têm uma descrição, uma localização geográfica (não implementado), autor, data de criação, data de actualização, estado (por validar, validado, resolvido) e uma das seguintes categorias:
* CONSTRUCTION: planned road work
* SPECIAL_EVENT: special events (fair, sport event, etc.)
* INCIDENT: accidents and other unexpected events
* WEATHER_CONDITION: weather condition affecting the road
* ROAD_CONDITION: status of the road that might affect travellers (potholes, bad pavement, etc.)

1. API REST
    1. Tem de permitir a adição de ocorrências (com a localização geográfica, e autor associados). Nota: O estado default será sempre por validar quando estas são criadas. **IMPLEMENTADO, FALTA A LOCALIZAÇÃO GEOGRÁFICA**
    2. Tem de permitir a actualização de ocorrências (para mudar o estado das mesmas para "validadas" por um administrador do sistema). **IMPLEMENTADO**
    3. Tem de permitir a filtragem de ocorrências por autor, por categoria e por localização (raio de alcance). **IMPLEMENTADO, FALTA LOCALIZAÇÃO GEOGRÁFICA**

## Requirements:
   * Python 3.7.0 (testado com esta versão)
   * PostgreSQL 10.5 (testado com esta versão)
   * VirtualEnv (sudo pip install virtualenv)

#### Instalar requirements adicionais (num ambiente virtual):
   * virtualenv <env_name>source 
   * <env_name>/bin/activate (Unix) ou <env_name>\Scripts\activate (Windows)
   * pip install -r path/to/requirements.txt
   
## How To Use PostgreSQL
Ler o seguinte artigo e **seguir os diversos passos indicados**:

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

**O nome da base de dados deve ser manageoccurrences**
 * CREATE DATABASE manageoccurrences;
 
 Caso opter por outro nome, editar o ficheiro settings.py disponível no projeto.

## Starting Django Project:
 * django-admin.py startproject myapp

## Migrations:
 
 * python manage.py makemigrations
 * python manage.py migrate
 
## Run Server:
 
 * python manage.py runserver
 
## Endpoints:
 
 * **/users/**
   * GET: Lista todos os utilizadores do sistema
   * POST: Permite criar utilizador
  
 * **/users/\<pk\>/** 
   * GET: Lista utilizador específico
   * PUT: Permite editar o utilizador
  
 * **/occurrences/**
   * GET: Lista todas as ocorrências
   * POST: Cria uma nova ocorrência
  
 * **/occurrences/\<pk\>/**
   * GET: Lista uma ocorrência específica
   * PUT: Permite editar uma ocorrência
   * DELETE: Apaga a ocorrência
  
 * **/occurrences/?category=\<category\>&author=\<author_id\>**
   * GET: Lista a(s) ocorrencia(s) que obedecem aos filtros invocados
  
 * **/api-auth/**
  
 * **/admin/**
 
 * **/admin/auth/users/**
 
 * **/admin/myapp/occurrence/**
 
 ## Testes
 
  * Para testar os diversos endpoints pode optar por usar o browser, usando o url http://127.0.0.1:8000
  
  ou
  
  * Usar a aplicação Postman (https://www.getpostman.com/) e configurar os diversos pedidos, de acordo com o especificado.
 
 Disponibilizo os seguintes pedidos como forma de apoio: https://www.getpostman.com/collections/479efa92fc3366de52a6
 
 Atenção, é necessário mudar alguns dos parâmetros presentes na collection, de modo a ir de encontro ao que existe na BD.
 
 **Qualquer um dos testes presentes na collection fornecida, funcionou conforme expectável no meu ambiente local.** 
