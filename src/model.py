from sklearn.ensemble import RandomForestRegressor

def crear_modelo():
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=8,
        max_features=0.8,
        min_samples_leaf=2,
        min_samples_split=8,
        random_state=42
    )
    return model
    