import pandas as pd
import os
from pathlib import Path

#Funcions utils del Xavi
def to_ruta_absoluta(p_str_path:str) -> str:
    """Calcular la ruta absoluta d’un directori o carpeta"""
    # Expandeix la tilde (~) si és present a la ruta
    _str_path = os.path.expanduser(p_str_path)
    # Comprovar si la ruta és absoluta o relativa
    if os.path.isabs(_str_path):
        return _str_path  # Si ja és absoluta, la retorna tal qual
    else:
        # Converteix la ruta relativa a una ruta absoluta
        return os.path.abspath(_str_path)

def es_dir(p_str_path:str) -> bool:
    """Detectar l'existència d'un directori o carpeta"""
    _ruta_abs = to_ruta_absoluta(p_str_path)
    # Comprovar si la ruta existeix i és un directori
    return os.path.isdir(_ruta_abs)


def llistar_directori(p_str_path:str) -> list:
    """Llistar el contingut d’un directori"""
    # Obtenir la ruta absoluta del directori
    _str_path = to_ruta_absoluta(p_str_path)
    print(_str_path)
    # Comprovar si la ruta és un directori
    if es_dir(_str_path):
        # Llistar el contingut del directori
        return os.listdir(_str_path)
    else:
        return []

def crear_dir(p_str_path_dir:str):
    """Crear un directori o carpeta"""
    _ruta_abs = to_ruta_absoluta(p_str_path_dir)
    # Crear el directori (i subdirectoris si calen)
    os.makedirs(_ruta_abs, exist_ok=True)


def treureExtensio(arxiu:str) -> str:
    return Path(arxiu).stem

def convertirAJson(directori:str, tmpDir) -> None:
    crear_dir(tmpDir)
    for i in llistar_directori(directori):
        print(i)
        arxiu = ''.join(directori + i)
        llegirExcel = pd.read_excel(arxiu)
        llegirExcel.to_json(tmpDir + treureExtensio(arxiu) + ".json")
    
