# main.py
# Script principal para ejecutar el pipeline del proyecto

import pandas as pd
from preprocessing import clean_data
from training import train_model
from evaluation import evaluate_model

def main():
    print("Bienvenido al Reto Técnico Empresarial con IA")
    print("Por favor asegúrate de haber configurado correctamente los datos y dependencias.")

    # Cargar datos
    data = pd.read_csv('data/sales_data.csv')
    print("Datos cargados correctamente.")

    # Preprocesar datos
    cleaned_data = clean_data(data)
    print("Datos preprocesados correctamente.")

    # Entrenar modelo
    model = train_model(cleaned_data)
    print("Modelo entrenado correctamente.")

    # Evaluar modelo
    evaluation_results = evaluate_model(model, cleaned_data)
    print("Evaluación del modelo completada.")
    print(evaluation_results)

if __name__ == "__main__":
    main()
