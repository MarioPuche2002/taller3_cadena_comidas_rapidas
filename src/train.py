from features import data_split
from model import crear_modelo
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

def training():
    
    X, y = data_split()
    train_size = int(len(X) * 0.8)
    
    X_train = X.iloc[:train_size]
    X_test = X.iloc[train_size:]
    
    y_train = y.iloc[:train_size]
    y_test = y.iloc[train_size:]
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train) 
    X_test_scaled = scaler.transform(X_test)       
    
    modelo = crear_modelo()
    modelo.fit(X_train_scaled, y_train)
    
    pred_train = modelo.predict(X_train_scaled)
    mae_train = mean_absolute_error(y_train, pred_train)
    mape_train = mean_absolute_percentage_error(y_train, pred_train) * 100
    r2_train = r2_score(y_train, pred_train)
    
    metricas_train = {"mae": mae_train,"mape": mape_train,"r2": r2_train}
    
    return modelo, X_test_scaled, y_test, scaler, metricas_train