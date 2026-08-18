from data import cargar_datos

def data_split():
    df = cargar_datos().copy()
    df = df.sort_values('fecha')
    
    df['almuerzos_ayer'] = df['almuerzos'].shift(1)
    df['almuerzos_semana_pasada'] = df['almuerzos'].shift(7)
    
    df['almuerzos_ayer'] = df['almuerzos_ayer'].bfill()
    df['almuerzos_semana_pasada'] = df['almuerzos_semana_pasada'].bfill()
    
    df['mes'] = df['fecha'].dt.month
    
    columnas_features = [
        "dia_semana", "mes", "temperatura_c", "llovio", 
        "precio", "es_quincena", "almuerzos_ayer", "almuerzos_semana_pasada"
    ]
    
    X = df[columnas_features]
    y = df["almuerzos"]
    
    return X, y