# reto-visualizacion

## Pasos seguidos:
- Planteamiento y creación de la estructura del proyecto
- Desarrollo del Docker Compose encargado de crear los servicios de Elasticsearch y Kibana y vincular uno al otro
- Elección del método de indexación de datos y de la temática de estos
- Desarrollo del programa de Python encargado de indexar los datos en Elasticsearch
- Investigación de uso de Kibana
- Creación del dashboard con gráficos para la visualización de los datos

## Instrucciones de uso:
- Estando en el directorio app, ejecutar $ docker-compose up -d
- Inicializar entorno virtual: $ source .venv/bin/activate
- Iniciar Elasticsearch y Kibana: $ docker-compose up -d (desde el directorio /.venv/app)
- Indexar datos sintéticos: $ python3 generate_data.py

## Posibles vías de mejora:
- 

## Problemas / Retos encontrados:
- Seguridad (los servicios no se vinculaban debido al https)

## Alternativas posibles:
- Bases de datos NoSQL como InfluxDB o MongoDB
- Servicios de visualización como Grafana o Prometheus

https://realpython.com/python-virtual-environments-a-primer/
https://www.elastic.co/es/blog/getting-started-with-the-elastic-stack-and-docker-compose
https://www.elastic.co/guide/en/kibana/current/docker.html#_remove_docker_containers