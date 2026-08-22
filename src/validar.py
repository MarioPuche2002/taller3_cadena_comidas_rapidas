from train import training
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

def validar():
    modelo, X_test_scaled, y_test, scaler, metricas_train = training()
    pred_test = modelo.predict(X_test_scaled)

    mae_test = mean_absolute_error(y_test, pred_test)
    mape_test = mean_absolute_percentage_error(y_test, pred_test) * 100
    r2_test = r2_score(y_test, pred_test)
    
    print("=== AUDITORÍA / COMPARATIVA DE MODELO ===")
    print(f"Métrica       | Entrenamiento | Prueba (Test)")
    print(f"---------------------------------------------")
    print(f"MAE           | {metricas_train['mae']:.2f}         | {mae_test:.2f} almuerzos")
    print(f"R2            | {metricas_train['r2']:.2f}          | {r2_test:.2f}")
    print("=============================================")
    
    return mae_test, mape_test

if __name__ == "__main__":
    validar()