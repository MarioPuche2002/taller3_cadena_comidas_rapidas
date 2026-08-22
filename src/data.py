from config import parametros
import pandas as pd
import numpy as np


def limpiar_datos(df):
    df = df.copy()

    columnas_numericas = ["temperatura_c", "precio", "almuerzos"]
    for col in columnas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "es_quincena" in df.columns:
        df["es_quincena"] = pd.to_numeric(df["es_quincena"], errors="coerce")

    if "llovio" in df.columns:
        # normaliza texto tipo "si"/"no"/"1"/"0" a 0/1
        df["llovio"] = (
            df["llovio"].astype(str).str.strip().str.lower()
            .map({"1": 1, "0": 0, "si": 1, "sí": 1, "no": 0, "true": 1, "false": 0})
        )

    if "dia_semana" in df.columns:
        df["dia_semana"] = df["dia_semana"].astype(str).str.strip().str.lower()

    umbral_col = 0.90
    porc_nulos_col = df.isna().mean()
    columnas_a_eliminar = porc_nulos_col[porc_nulos_col > umbral_col].index.tolist()
    if columnas_a_eliminar:
        df = df.drop(columns=columnas_a_eliminar)

    for col in df.columns:
        porc_nulos = df[col].isna().mean()
        if porc_nulos == 0:
            continue
        if porc_nulos > 0.10:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].median())
            else:
                moda = df[col].mode(dropna=True)
                if not moda.empty:
                    df[col] = df[col].fillna(moda.iloc[0])
                else:
                    df = df.dropna(subset=[col])
        else:
            df = df.dropna(subset=[col])

    df = df.reset_index(drop=True)
    return df


def cargar_datos():
    par = parametros()
    file_path = par["ruta_archivo"]
    df = pd.read_csv(file_path, parse_dates=["fecha"])

    df = limpiar_datos(df)

    df = df.sort_values("fecha").reset_index(drop=True)

    df_dias = pd.get_dummies(df['dia_semana'], prefix='dia', dtype=int)
    df = pd.concat([df, df_dias], axis=1)

    df['mes'] = df['fecha'].dt.month
    df_meses = pd.get_dummies(df['mes'], prefix='mes', dtype=int)
    df = pd.concat([df, df_meses], axis=1)

    return df