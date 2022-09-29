#timepo que la lasaña debería estar en el horno acorde con el libro de cocina
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    
    """     Calcular el tiempo de horneado restante. 
    :param elapsed_bake_time: introducir el tiempo de horneado transcurrido.
    :return: devuelve el tiempo de horneado restante (en minutos) derivado de 'EXPECTED_BAKE_TIME'

    Función que toma los valores reales que ha estado la lasaña en el horno como argumento y devuelve cuántos minutos le quedan por hornear a la lasaña basado en el 'EXPECTED_BAKE_TIME'
 """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Calcular el tiempo de preparación.

    :param number_of_layers: introducir el número de capas de la lasaña
    :return: devulve cuanto tiempo (en minutos) ha tardado en prepararlo, teniendo en cuenta que son dos minutos más por capa añadida.
        Esta función toma un número entero que representa el número de capas añadidas al plato,
    calculando el tiempo de preparación utilizando un tiempo de 2 minutos por capa añadida.
    """
    return number_of_layers * PREPARATION_TIME

def elapased_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcular el tiempo transcurrido.

    :param number_of_layers: introducir el número de capas de la lasaña.
    :param elapsed_baked_time introducir el tiempo de cocción transcurrido.
    :return: devuelve el tiempo total transcurrido (en minutos) de cocción y preparación.
    
        Esta función toma dos números enteros que representan el número de capas de lasaña y el tiempo de horneado
     y calcula el total de minutos transcurridos en la cocción de la lasaña.
     """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
