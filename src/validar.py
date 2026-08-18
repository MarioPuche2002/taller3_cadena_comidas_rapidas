from train import training
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

def validar():

    modelo, X_test_scaled, y_test, scaler = training()
    pred = modelo.predict(X_test_scaled)

    mae = mean_absolute_error(y_test, pred)
    mape = mean_absolute_percentage_error(y_test, pred) * 100
    
    print("=== AUDITORÍA / MAE HONESTO ===")
    print(f"MAE :",mae,"almuerzos")
    print(f"MAPE:",mape,"%")
    
    return mae, mape

if __name__ == "__main__":
    validar()