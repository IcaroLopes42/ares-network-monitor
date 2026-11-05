import pyshark
import asyncio
import threading
import time

INTERFACE = 'Wi-Fi'

def capturar_trafego(interface):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print(f"[*] Iniciando motor de captura na interface: {interface}...")
    captura = pyshark.LiveCapture(interface=interface)
    
    for pacote in captura.sniff_continuously():
        try: 
            ip_origem = pacote.ip.src
            ip_destino = pacote.ip.dst
            print(f"[Captura] {ip_origem} -> {ip_destino}")
        except AttributeError:
            # Ignora pacotes que não têm a camada IP
            continue

if __name__ == '__main__':
    # Configura e inicia a Thread em background
    thread_captura = threading.Thread(
        target=capturar_trafego, 
        args=(INTERFACE,), 
        daemon=True
    )
    thread_captura.start()

    # Mantém o script principal vivo sem consumir CPU
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Encerrando o ARES.")