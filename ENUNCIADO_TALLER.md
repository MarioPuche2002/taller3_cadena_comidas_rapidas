# Taller Semana 3 — PISTA A: "El modelo milagroso" 🏢📊

> Pista de **datos tabulares a escala**. Si prefieres visión por computador, mira la
> Pista B ("Conteo de aforo"). Ambas valen igual y comparten el mismo reto de fondo:
> honestidad metodológica + ingeniería que escala. Elige UNA.

## El contexto

Trabajas en el equipo de Data Science de **una cadena nacional de comidas rápidas con
1.200 puntos de venta** en el país. El área de cadena de suministro necesita predecir
la **demanda diaria de almuerzos por sede** para planear compras de insumos: si el
modelo sobreestima, se pudre comida; si subestima, se agota el producto y se pierden
ventas. A esta escala, un punto de MAE equivale a **millones de pesos al mes** en
desperdicio o quiebres de inventario.

Un analista junior (recién salido, con mucha confianza y mucho ChatGPT) entregó un
modelo para una sede piloto y presume su métrica: **"MAE de 2.3 almuerzos, error del
2%, esto está listo para desplegar en las 1.200 sedes"**.

Antes de que ese modelo toque producción y dispare órdenes de compra en todo el país,
alguien tiene que auditarlo. Ese alguien eres tú. **La métrica miente** — tu trabajo es
demostrarlo, reportar la verdad y construir el modelo que sí se puede desplegar.

## La escala real (léela, cambia cómo piensas el problema)

El CSV que recibes (`data/almuerzos_entrenamiento.csv`) es **una muestra**: el histórico
de una sede. En producción, este mismo pipeline correría sobre el histórico de las 1.200
sedes — cientos de millones de filas, alimentado por el data warehouse cada madrugada.
Por eso **no se evalúa que tu modelo sea grande, sino que tu pipeline sea correcto y
reproducible**: el código que entregas debe ser, línea por línea, el que un ingeniero
pondría a correr en el cluster sobre los datos completos. Un leak que aquí infla la
métrica, allá dispara órdenes de compra equivocadas en todo el país.

## La novedad: el conjunto de validación oculto 🔒

El CSV que tienes llega hasta cierta fecha. **El equipo tiene los días siguientes** —
el "futuro" que tú nunca ves, reservado para validar como se hace en la industria: contra
datos que el modelo no pudo tocar.

Al final de la sesión, ejecutaré el `predict.py` de cada equipo contra ese futuro oculto
y publicaré un **leaderboard** con el MAE real de cada uno. La IA puede escribir todo el
código que quieran — pero la IA no conoce ese conjunto oculto. La única estrategia
ganadora es la honestidad metodológica.

⚠️ Consecuencia directa: si tu métrica local dice 3 y el leaderboard dice 20, todos
sabremos que tu validación estaba contaminada. La brecha entre tu número y el mío ES la
medida de tu rigor — el mismo criterio con el que un líder técnico decide si tu modelo
va a producción o no.

## Misión

**Fase 1 — La auditoría (encuentra las 3 trampas).**
El código del analista corre perfecto y no tiene bugs de sintaxis. Tiene algo peor: tres
decisiones metodológicas que inflan la métrica y que, a escala nacional, costarían
millones. Documéntalas en el README (sección "Auditoría"): qué hace mal, por qué infla el
número, y qué pista la delata. Pregunta guía para la peor de las tres: *¿toda columna que
existe en el histórico existirá también a las 6am del día que la sede necesita la
predicción para hacer su pedido?*

**Fase 2 — El modelo honesto.**
- Solo features conocibles ANTES del día a predecir (las que el ERP tiene disponibles al
  cierre del día anterior).
- `Pipeline` + `ColumnTransformer` de sklearn: el preprocesamiento aprende (fit)
  únicamente del entrenamiento — leak imposible por construcción, y el mismo objeto
  escala a millones de filas sin reescribir nada.
- **Validación temporal**: el "examen interno" son los últimos N días de tus datos, no un
  split aleatorio. Estás prediciendo el futuro de la operación; valídate contra el futuro.
- Reporta tu MAE honesto en el README. Debería parecerse al del leaderboard.

**Fase 3 — El contrato de predicción.**
Implementa exactamente esta interfaz (así se evalúa a todos los equipos igual, como un
endpoint de scoring en producción):

```bash
python src/predict.py <ruta_features.csv> <ruta_salida.csv>
```

- El CSV de entrada trae: `fecha, dia_semana, temperatura_c, llovio, precio,
  es_quincena` — fechas FUTURAS que no están en tu entrenamiento.
- Tu script escribe un CSV con exactamente dos columnas: `fecha, prediccion` (una fila
  por cada fecha de entrada).
- Debe funcionar sin intervención humana, en menos de 2 minutos, usando solo las
  librerías del requirements. (En producción esto sería un job programado; si necesita
  que alguien lo edite a mano cada día, no sirve.)

## Entregable

Repositorio en Git con:

```
demanda-sede-ml/
├── data/almuerzos_entrenamiento.csv    # la muestra
├── src/
│   ├── config.py · data.py · model.py
│   ├── validar.py          # imprime tu MAE honesto (validación temporal)
│   └── predict.py          # EL CONTRATO — el endpoint de scoring
├── requirements.txt
└── README.md               # con "Auditoría" y "Nuestro MAE honesto"
```

Más el historial: **≥5 commits** con mensajes que narren el proceso.

## Rúbrica

| Criterio | Peso | Cómo se evalúa |
|---|---|---|
| El contrato funciona contra el conjunto oculto | 30% | Tu predict.py corre con mi CSV y produce salida válida. Un CRASH aquí es 0 — el modelo perfecto que no corre con datos nuevos no se puede desplegar. |
| Honestidad metodológica | 20% | Brecha pequeña entre tu MAE reportado y el del leaderboard. La posición suma, pero la honestidad pesa más que el puesto. |
| Calidad del pipeline | 30% | Sin features del futuro, Pipeline por construcción, validación temporal, config sin números mágicos, código que escalaría a las 1.200 sedes sin cambios. |
| Auditoría + Git | 20% | Las 3 trampas documentadas con evidencia; ≥5 commits narrativos. |

## Pistas sin espóiler

- Antes de auditar, pregúntate: ¿qué datos tiene la sede en el ERP a las 6am, antes de
  mandar su pedido de insumos del día? Esa es la lista de features legítimas. Todo lo
  demás es mirar la respuesta.
- El negocio no es el mismo de hace seis meses: mira la serie completa en una gráfica
  antes de decidir tus features. El tiempo también es información (y a escala nacional,
  las tendencias mueven millones).
- Prueba tu predict.py tú mismo: separa los últimos días de tu CSV como "conjunto oculto
  casero" y verifica que el contrato corre de punta a punta.
- Defensa garantizada al final: *"¿por qué tu MAE es PEOR que el del analista junior, y
  por qué eso es una buena noticia para la empresa?"*
