from elasticsearch import Elasticsearch
from datetime import datetime, timezone
import time
import random
import logging.config
import urllib3

# Deshabilitar logs de librerías externas
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
# Establecer logger
logging.basicConfig(format='%(asctime)s [%(levelname)s]   %(name)s | %(message)s', datefmt='%m/%d/%Y %H:%M:%S', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('generate_data')

# Desactivar warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Función que genera los datos sintéticos aleatoriamente
def generate_wind_data():
    # Generar producción energética aleatoria
    active_power = round(random.uniform(0, 200), 2)  # LV ActivePower (kW)
    wind_speed = round(random.uniform(3, 25), 2)  # Wind Speed (m/s)
    theoretical_power_curve = round(active_power * random.uniform(0.8, 1.2), 2)  # Theoretical_Power_Curve (KWh)
    wind_direction = round(random.uniform(0, 360), 2)  # Wind Direction (°)

    # Devolver el diccionario con los datos
    return {
        "LV ActivePower (kW)": active_power,
        "Wind Speed (m/s)": wind_speed,
        "Theoretical_Power_Curve (KWh)": theoretical_power_curve,
        "Wind Direction (°)": wind_direction,
        "DateTime": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }


# Función principal de envío de datos
def main():
    # Configura la conexión a Elasticsearch
    es = Elasticsearch("https://elastic:elasticpwd@localhost:9200/", verify_certs=False)

    # Comprobar si el clúster de Elasticsearch está abierto
    if (es.ping()):
        logger.info("Conectado. Iniciando indexación de datos.")
        
        while True:
            # Si el clúster de Elasticsearch se cierra se finaliza el envío de datos
            if not es.ping():
                logger.info("El clúster de Elasticsearch se ha cerrado.")
                break
                
            # Generar datos sintéticos
            wind_data = generate_wind_data()

            # Indexar los datos en Elasticsearch
            es.index(index="wind-turbine", body=wind_data)
            logger.debug("Datos indexados correctamente: " + str(wind_data))

            # Esperar 10 segundos antes de generar nuevos datos
            time.sleep(10)
    else:
        logger.warning("El clúster de Elasticsearch no está abierto.")    


# Llamada a la función principal al iniciar el programa
if __name__ == "__main__":
    main()
