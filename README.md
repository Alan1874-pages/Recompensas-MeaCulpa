# Recompensas-MeaCulpa
Spooderman Malevo Nobody Y john
Este es un repositorio hecho para el servidor de MEA CULPA, para que el tirado de las recompensas sea mucho más dinamicoi
  ---

  Tecnologias:
  Python
  Fast API
  Docker
  MySQL
  

## Estructura
Separamos la aplicación en /frontend y /backend
### Backend
En backend tenemos /app que contiene toda la aplicacion.
Tambien tenemos main que ejecutara la aplicación.

#### ENDPOINT
Punto final para enviar datos, aqui enviamos los datos tratados, recibiendo schemas y enviando a crud.
#### CRUD
Procesamiento de datos, aqui tratamos los datos como schemas y solicitamos a la DB si es necesario.
#### DB
Aqui se hacen las peticiones a DB junto a todo lo relevante a la misma.
#### SCHEMA
Aqui tenemos todos los grupos de datos, para el procesamiento y gestion de los mismos.
#### UTILS
Cualquier script o cositas que faciliten procesos de los otros puntos, no tiene que tener relacion con mas de un punto a la vez.