import sys
import pandas as pd
import joblib
from data import cargar_datos
from train import training

def generar_predicciones(ruta_entrada, ruta_salida):

    df_historico = cargar_datos()
    df_futuro = pd.read_csv(ruta_entrada, parse_dates=["fecha"])
    
    modelo, _, _, _, _ = training()
    
    # 4. Lógica para rellenar rezagados autorregresivos
    # Necesitas el último valor conocido del histórico
    ultimo_real = df_historico.iloc[-1]['almuerzos']
    
    # Unir histórico y futuro para calcular los 'shift' correctamente
    # (Este es un enfoque simplificado)
    df_completo = pd.concat([df_historico, df_futuro], axis=0, sort=False)
    
    # Recalcular rezagados en el df_futuro usando la lógica de data.py
    df_completo['almuerzos_ayer'] = df_completo['almuerzos'].shift(1)
    df_completo['almuerzos_semana_pasada'] = df_completo['almuerzos'].shift(7)
    
    # Filtrar solo la parte que corresponde al futuro
    X_futuro = df_completo.iloc[len(df_historico):].copy()
    
    predicciones = modelo.predict(X_futuro)
    
    df_resultado = pd.DataFrame({
        'fecha': df_futuro['fecha'],
        'prediccion': predicciones})
    
    df_resultado.to_csv(ruta_salida, index=False)
    print(f"Predicciones guardadas en {ruta_salida}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python src/predict.py <ruta_features.csv> <ruta_salida.csv>")
    else:
        generar_predicciones(sys.argv[1], sys.argv[2])