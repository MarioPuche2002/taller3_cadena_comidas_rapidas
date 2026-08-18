from features import data_split
from model import crear_modelo
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

def training():
    X, y = data_split()
    
    split_idx = int(len(X) * 0.85)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
    
    modelo = crear_modelo()
    
    modelo.fit(X_train, y_train)
    
    pred_train = modelo.predict(X_train)
    
    mae_train = mean_absolute_error(y_train, pred_train)
    mape_train = mean_absolute_percentage_error(y_train, pred_train) * 100
    r2_train = r2_score(y_train, pred_train)
    
    metricas_train = {
        'mae': mae_train,
        'mape': mape_train,
        'r2': r2_train}
    
    return modelo, X_test, y_test, None, metricas_train