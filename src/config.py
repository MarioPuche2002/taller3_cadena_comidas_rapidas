import os


def parametros():
    ruta_archivo = os.path.join(os.getcwd(), "data", "almuerzos_entrenamiento.csv")

    par = {
        "random_state": 42,
        "ruta_archivo": ruta_archivo,
        "columna_fecha": "fecha",
        "columna_objetivo": "almuerzos",

        "test_size": 0.2,   

        "features_numericas": ["temperatura_c", "precio", "dias_desde_inicio"],
        "features_categoricas": ["dia_semana", "llovio", "es_quincena"],

        "estrategia_imputacion_numerica": "median",
        "estrategia_imputacion_categorica": "most_frequent",

        "alpha": 0.1,
        "l1_ratio": 0.5,
        "max_iter": 30000,}
    
    return par