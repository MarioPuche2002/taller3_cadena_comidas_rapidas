from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet

def crear_modelo():

    modelo = Pipeline([
        ('scaler', StandardScaler()),
        ('elastic', ElasticNet(
            alpha=0.1,
            l1_ratio=0.5,
            random_state=42,
            max_iter=30000
        ))])
    
    return modelo