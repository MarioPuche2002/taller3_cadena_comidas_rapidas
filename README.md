# Demanda de almuerzos por sede — modelo honesto
---

## Auditoría (las 3 trampas)

### 1. Features que no existen a las 6am del día a predecir

El histórico trae columnas como `llovio`, `ingreso_dia` que registran si el evento sucedio pero una vez finalizado el día.A las 6 am no se puede saber si va a llover.

### 2. Split incorrecto

Si el split train/test se hace de forma aleatoria (`train_test_split` con shuffl), el conjunto de "prueba" termina
mezclado con días anteriores a los de entrenamiento. El modelo efectivamente aprende de un rango de fechas que incluye información de fechas futuras.

---

## Nuestro pipeline honesto

- **Features:** solo variables conocibles antes de las 6am del día a predecir
  (`temperatura_c` como pronóstico, `precio`, `es_quincena`, `dia_semana`, `mes`).
  Se descartaron los rezagos autorregresivos del target para eliminar cualquier
  ambigüedad de leak por construcción.
- **Pipeline de sklearn:** `StandardScaler` + `ElasticNet` dentro de un mismo
  `Pipeline`. El escalado se ajusta (`fit`) únicamente sobre el set de entrenamiento;
  el mismo objeto se reutiliza tal cual para predecir sobre datos nuevos, sin
  recalcular nada a mano.
- **Validación temporal:** los datos se ordenan por `fecha` y el "examen interno" es
  el último tramo cronológico del histórico (15%), no una muestra aleatoria.
- **Limpieza defensiva de datos:** conversión de tipos, eliminación de columnas con
  >90% de nulos, imputación (mediana/moda) para nulos entre 10% y 90%, y eliminación
  de filas para nulos <10% — pensado para que el pipeline no se caiga si el CSV de una
  sede real viene con datos sucios.

---

## Metricas obtenidas

```
=== AUDITORÍA / COMPARATIVA DE MODELO ===
Métrica       | Entrenamiento | Prueba (Test)
---------------------------------------------
MAE           | 9.50          | 9.55 almuerzos
R2            | 0.50          | 0.53
=============================================
```
La metrica principal en la que se probaron los analisis y se busco minimizar fue el MAE , el R2 se tomo como una referencia para ver el ajuste del modelo y examinar el sobreajuste (si lo habia)

## Estructura del repositorio

```
demanda-sede-ml/
├── data/almuerzos_entrenamiento.csv
├── src/
│   ├── config.py
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   ├── train.py
│   ├── validar.py
│   └── predict.py
├── requirements.txt
└── README.md
```

## Uso

```bash
python src/validar.py
python src/predict.py <ruta_features.csv> <ruta_salida.csv>
```