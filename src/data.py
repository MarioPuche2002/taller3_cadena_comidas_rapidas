from config import parametros
import pandas as pd
import numpy as np

def cargar_datos():
    par = parametros()
    file_path = par["ruta_archivo"]
    df = pd.read_csv(file_path, parse_dates=["fecha"])
    print(df)

    return df
cargar_datos()