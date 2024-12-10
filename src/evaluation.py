# evaluation.py
# Módulo para la evaluación del modelo

import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_model(model, test_data):
    print("Evaluando el modelo...")

    x_test, y_test = test_data

    # Realiza predicciones
    predictions = model.predict(x_test)

    # Calcula métricas de evaluación
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Imprime las métricas de evaluación
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"R2 Score: {r2}")

    # Guarda los resultados en un archivo
    with open('outputs/sales_forecasting_report.txt', 'w') as f:
        f.write(f"Mean Squared Error (MSE): {mse}\n")
        f.write(f"Mean Absolute Error (MAE): {mae}\n")
        f.write(f"R2 Score: {r2}\n")
