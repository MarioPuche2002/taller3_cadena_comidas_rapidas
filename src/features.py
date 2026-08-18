from data import cargar_datos

def data_split():
    df = cargar_datos()
    
    df['mes'] = df['fecha'].dt.month
    X = df[["dia_semana", "mes", "temperatura_c", "precio", "es_quincena"]]
    y = df["almuerzos"]
    
    return X, y