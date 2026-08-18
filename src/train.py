from features import data_split
from sklearn.preprocessing import StandardScaler
from model import crear_modelo

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
    
    return modelo, X_test_scaled, y_test