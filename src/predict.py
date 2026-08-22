import sys
import pandas as pd
from features import data_split
from train import training


def generar_predicciones(ruta_entrada, ruta_salida):
    columnas_modelo, _ = data_split()
    modelo, _, _, _, _ = training()

    df_futuro = pd.read_csv(ruta_entrada, parse_dates=["fecha"])

    df_dias = pd.get_dummies(df_futuro["dia_semana"], prefix="dia", dtype=int)
    df_mes = pd.get_dummies(df_futuro["fecha"].dt.month, prefix="mes", dtype=int)
    df_feat = pd.concat([df_futuro, df_dias, df_mes], axis=1)

    X_futuro = df_feat.reindex(columns=columnas_modelo.columns, fill_value=0)
    predicciones = modelo.predict(X_futuro)

    pd.DataFrame({"fecha": df_futuro["fecha"], "prediccion": predicciones}).to_csv(ruta_salida, index=False)
    print(f"Predicciones guardadas en {ruta_salida}")


if __name__ == "__main__":
    generar_predicciones(sys.argv[1], sys.argv[2])