from pathlib import Path
import os


def parametros():
    ruta_archivo = os.path.join(os.getcwd(), "data", "almuerzos_entrenamiento.csv")
    par = {"random_state": 42,"test_size": 0.2,"ruta_archivo": ruta_archivo}
    return par