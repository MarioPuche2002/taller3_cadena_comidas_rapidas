from data import cargar_datos

def data_split():
    df = cargar_datos()
    df = df.sort_values("fecha").reset_index(drop=True)
    
    X = df[["dia_semana", "temperatura_c", "llovio", "precio", "es_quincena"]]
    y = df["almuerzos"]
    
    return X, y