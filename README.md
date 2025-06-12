
# Automatizador de Ataque EternalBlue (MS17-010)

Este script en Python automatiza el escaneo y explotación de sistemas vulnerables a la vulnerabilidad **MS17-010**, también conocida como **EternalBlue**, utilizando herramientas como `nmap` y `Metasploit Framework`.

## 🚨 ¿Qué es MS17-010 (EternalBlue)?

**MS17-010** es una vulnerabilidad crítica en el protocolo SMBv1 de Windows, divulgada por Microsoft en marzo de 2017. Fue explotada por el exploit **EternalBlue**, desarrollado originalmente por la NSA y filtrado por el grupo Shadow Brokers. Esta vulnerabilidad fue utilizada en ataques masivos como **WannaCry** y **NotPetya**, permitiendo ejecución remota de código sin autenticación previa.

Microsoft publicó un parche de seguridad para mitigarla, pero aún existen sistemas no actualizados en riesgo.

## 🧰 Requisitos

- Python 3.x
- Nmap (con el script `smb-vuln-ms17-010` disponible)
- Metasploit Framework
- Permisos de administrador/root

## ⚙️ ¿Qué hace este script?

1. Solicita la IP de la víctima y la IP local del atacante.
2. Escanea el puerto 445 de la víctima con `nmap` para detectar si es vulnerable a MS17-010.
3. Si es vulnerable:
   - Genera automáticamente un script `.rc` para Metasploit.
   - Lanza `msfconsole` con el script, listo para ejecutar el exploit.
4. Si no es vulnerable, el script termina sin lanzar el ataque.

## 🖥️ Uso

```bash
python3 EternalBlue.py
```

Se te pedirá:

- `IP de la víctima`: Dirección IP del sistema objetivo.
- `Tu IP local (LHOST)`: IP del atacante donde recibirá la sesión `meterpreter`.

Ejemplo de salida:

```
IP de la víctima: 192.168.0.10
Tu IP local (LHOST): 192.168.0.5
[+] Escaneando 192.168.0.10 con Nmap para MS17-010...
[+] El sistema ES vulnerable a MS17-010 (EternalBlue)
[+] Script para Metasploit generado: eternalblue_auto.rc
[*] Ejecutando Metasploit con el script...
```

## ⚠️ Advertencia

Este script se proporciona con fines **educativos y de auditoría ética**. El uso no autorizado contra sistemas que no son de tu propiedad o sin permiso explícito es ilegal y puede tener consecuencias legales graves.

## 📚 Referencias

- [Microsoft MS17-010 Bulletin](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)
- [Exploit EternalBlue - Rapid7](https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/)

---

## 🧑‍🏫 Autor

Explicación elaborada por [Sebastian Peinador](https://www.linkedin.com/in/sebastian-j-peinador/) para propósitos didácticos y de investigación en ciberseguridad ofensiva.

---

## 📄 Licencia

Este material se distribuye bajo la licencia [MIT](LICENSE).

---

> Si te resulta útil, ¡no olvides darle ⭐ al repo o compartirlo!
