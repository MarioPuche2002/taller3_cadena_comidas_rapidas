from data import cargar_datos

def data_split():
    df = cargar_datos()
    df_model = df.copy()
    
    columnas_a_eliminar = [col for col in ['dia_semana', 'mes'] if col in df_model.columns]
    df_model = df_model.drop(columns=columnas_a_eliminar)
    
    columnas_dias = [col for col in df_model.columns if col.startswith('dia_')]
    columnas_meses = [col for col in df_model.columns if col.startswith('mes_')]
    
    columnas_features = ["temperatura_c", "precio", "es_quincena", "almuerzos_ayer", "almuerzos_semana_pasada"] + columnas_dias + columnas_meses
    
    X = df_model[columnas_features]
    y = df_model["almuerzos"]
    print(X)
    
    return X, y