#timepo que la lasaña debería estar en el horno acorde con el libro de cocina
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    
    """     Calcular el tiempo de horneado restante. 
    :param elapsed_bake_time: introducir el tiempo de horneado transcurrido.
    :return: devuelve el tiempo de horneado restante (en minutos) derivado de 'EXPECTED_BAKE_TIME'

    Función que toma los valores reales que ha estado la lasaña en el horno como argumento y devuelve cuántos minutos le quedan por hornear a la lasaña basado en el 'EXPECTED_BAKE_TIME'
 """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time


