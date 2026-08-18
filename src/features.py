from data import cargar_datos

def data_split():
    df = cargar_datos()
    
    columnas_dias = [col for col in df.columns if col.startswith('dia_')]
    columnas_meses = [col for col in df.columns if col.startswith('mes_')]
    
    columnas_features = ["temperatura_c", "precio", "es_quincena", "almuerzos_ayer", "almuerzos_semana_pasada"] + columnas_dias + columnas_meses
    
    X = df[columnas_features]
    y = df["almuerzos"]
    
    return X, y