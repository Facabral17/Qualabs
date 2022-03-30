import os, json, glob
from pathlib import Path

save_modules = {}
path = r'C:\Users\FacundoCabral\Desktop\Qualabs\jsonData'
filename = 'EjercicioA'

# Lugar, nombre y extensión del archivo
output = Path("./jsonResult", filename).with_suffix('.json')

def user_to_module(_file):
    f = open(_file, )
    
    load_data = json.load(f)
    key_modules = load_data['provider'].keys()
    for keymod in key_modules:
        if keymod not in save_modules.keys():
            save_modules[keymod] = {}
            
    for modules in save_modules.keys():
        key = load_data['provider'][modules]
        if key not in save_modules[modules].keys():
            save_modules[modules][key] = []
        save_modules[modules][key].append(_file.name)
        f.close()


# Escaneo el directorio con scandir
with os.scandir(path) as entries:
    for file in entries:
        user_to_module(file)


# Exporto el archivo (w crea o remplaza)
with open(output, 'w') as file:
    json.dump(save_modules, file)
        