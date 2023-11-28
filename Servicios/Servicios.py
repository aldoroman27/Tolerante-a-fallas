import psutil
import time
import subprocess

app = "Chrome.exe"
ruta = "C:\Program Files\Google\Chrome\Application\chrome.exe"
while True:
    procesos = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]
    proceso_encontrado =  False
    for proceso in procesos:
        if app.lower() in proceso['name'].lower():
            proceso_encontrado = True
            break
    if proceso_encontrado:
        print(f"La aplicacion {app} esta abierta.")
    else:
        print(f"La aplicacion {app} esta cerrada, abriendo de nuevo...")
        subprocess.Popen([ruta])
        
    time.sleep(5)