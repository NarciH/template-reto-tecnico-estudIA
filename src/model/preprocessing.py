# preprocessing.py
# Módulo para la limpieza y preprocesamiento de datos

import pandas as pd

def load_sales_data(file_path):
    """
    Carga los datos de ventas desde un archivo CSV.
    
    Args:
        file_path (str): La ruta del archivo CSV.
        
    Returns:
        pd.DataFrame: DataFrame con los datos de ventas.
    """
    try:
        df = pd.read_csv(file_path)
        print("Datos de ventas cargados correctamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos de ventas: {e}")
        return None

def preprocess_sales_data(df):
    """
    Preprocesa los datos de ventas.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de ventas.
        
    Returns:
        pd.DataFrame: DataFrame con los datos de ventas preprocesados.
    """
    try:
        # Convertir la columna de fecha a tipo datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Ordenar los datos por fecha
        df = df.sort_values('date')
        
        # Rellenar valores nulos
        df = df.fillna(method='ffill')
        
        print("Datos de ventas preprocesados correctamente.")
        return df
    except Exception as e:
        print(f"Error al preprocesar los datos de ventas: {e}")
        return None

def clean_data(df):
    """
    Limpia los datos de ventas.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de ventas.
        
    Returns:
        pd.DataFrame: DataFrame con los datos de ventas limpios.
    """
    try:
        # Eliminar columnas innecesarias
        df = df.drop(columns=['unnecessary_column'])
        
        # Eliminar duplicados
        df = df.drop_duplicates()
        
        print("Datos de ventas limpiados correctamente.")
        return df
    except Exception as e:
        print(f"Error al limpiar los datos de ventas: {e}")
        return None
