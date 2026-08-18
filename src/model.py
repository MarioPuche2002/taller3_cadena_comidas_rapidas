from sklearn.ensemble import RandomForestRegressor

def crear_modelo():
    model = RandomForestRegressor(
        n_estimators=100, 
        max_depth=10,          
        min_samples_split=5,   
        min_samples_leaf=2,    
        random_state=42
    )
    return model