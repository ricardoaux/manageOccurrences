# manageOccurrences

Requeriments:
 . 
 
 Migrations:
 
 . python manage.py makemigrations
 
 . python manage.py migrate
 
 Run Server:
 
 . python manage.py runserver
 
 Endpoints:
 
 . /users/
  - GET: Lista todos os utilizadores do sistema
  - POST: Permite criar utilizador
  
 . /users/<pk>
  - GET: Lista utilizador específico
  - PUT: Permite editar o utilizador
  
 . /occurrences/
  - GET: Lista todas as ocorrências
  - POST: Cria uma nova ocorrência
  
  ./occurrences/<pk>
   - GET: Lista uma ocorrência específica
   - PUT: Permite editar uma ocorrência
   - DELETE: Apaga a ocorrência
  
  . /occurrences/?category=<category>&author=<author_id>
    - GET: Lista a(s) ocorrencia(s) que obedecem aos filtros invocados
  
  ./api-auth/
  
  ./admin/
 
