from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from config import parametros

def crear_modelo():
    par = parametros()

    alpha_value = par["alpha"]
    l1_ratio_value = par["l1_ratio"]
    max_iter_value = par["max_iter"]
    random_state_value = par["random_state"]


    modelo = Pipeline([('scaler', StandardScaler()),('elastic', ElasticNet(alpha=alpha_value,l1_ratio=l1_ratio_value,random_state=random_state_value,max_iter=max_iter_value))])
    
    return modelo