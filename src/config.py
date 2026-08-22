from pathlib import Path
import os


def parametros():
    ruta_archivo = os.path.join(os.getcwd(), "data", "almuerzos_entrenamiento.csv")
    par = {"random_state": 42,"test_size": 0.2,"ruta_archivo": ruta_archivo,"alpha": 0.1,"l1_ratio": 0.5,"max_iter": 30000}
    return par
