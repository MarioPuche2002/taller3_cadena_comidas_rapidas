# Taller Semana 3 — Demanda por sede (cadena nacional) 🏢📊

Bienvenido al repositorio del taller. **Empieza leyendo [`ENUNCIADO_TALLER.md`](ENUNCIADO_TALLER.md)** —
ahí está la historia, la misión, el contrato de entrega y la rúbrica.

## Qué hay en este repo

```
demanda-sede-ml/
├── ENUNCIADO_TALLER.md    <- LÉEME PRIMERO
├── data/
│   └── almuerzos_entrenamiento.csv   # tu muestra de datos (una sede)
├── src/
│   └── entrenar.py        # el modelo del "analista junior" — el que vas a auditar
├── requirements.txt
└── README.md              # este archivo
```

## Cómo arrancar

```bash
# 1. Entorno virtual
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1

# 2. Dependencias
pip install -r requirements.txt

# 3. Corre el modelo del analista tal como llegó (para ver su "métrica milagrosa")
python src/entrenar.py
```

## Tu trabajo (resumen — el detalle está en el ENUNCIADO)

1. **Audita** el modelo del analista: encuentra por qué su métrica miente.
2. **Reconstruye** un modelo honesto con `Pipeline` + validación temporal.
3. **Implementa el contrato** `python src/predict.py <features.csv> <salida.csv>`.
4. Documenta todo en tu propio README (secciones "Auditoría" y "Nuestro MAE honesto")
   y trabaja con **≥5 commits** que cuenten el proceso.

Al final, el profesor evaluará tu `predict.py` contra un conjunto de datos oculto y
publicará el leaderboard. Éxitos 🚀
