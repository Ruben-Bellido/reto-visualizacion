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
- Iniciar sesión en Kibana accediendo a la dirección http://localhost:5601/ con el usuario "elastic" y la contraseña "elasticpwd"
- Visualizar los datos indexados mediante el dashboard "Turbina eólica"

## Posibles vías de mejora / Problemas / Retos encontrados:
- Kibana no se vinculaba a elasticsearch debido al https en los elasticsearch hosts, puesto a que la seguridad estaba deshabilitada
- Establecer la seguridad/certificados, ya que los servicios no aprueban el healthcheck y ninguno conseguía levantarse correctamente
- Envíar datos de forma segura puesto a que no se encuentran los certificados

## Alternativas posibles:
- Servicios de visualización como Grafana o Prometheus
