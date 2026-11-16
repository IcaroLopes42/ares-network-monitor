import pyshark
import asyncio
import threading
import time

INTERFACE = 'Wi-Fi'
estado_rede: dict = {}

def registrar_ip_novo(ip: str) -> dict:
    "Retorna o schema inicial do estado para um IP recem visto"
    return {"total_pacotes": 0,
             "portas_tcp_destino": set(), 
             "portas_udp_destino": set()
             }

def atualizar_estado(pacote, estado: dict) -> None:
    try:
        ip = pacote.ip.src
    except AttributeError:
        return

    if ip not in estado:
        estado[ip] = registrar_ip_novo(ip)
    estado[ip]["total_pacotes"] += 1

    try:
        estado[ip]["portas_tcp_destino"].add(int(pacote.tcp.dstport))
    except AttributeError:
        pass  # ← pacote sem camada TCP, segue em frente

    try:
        estado[ip]["portas_udp_destino"].add(int(pacote.udp.dstport))
    except AttributeError:
        pass  # ← pacote sem camada UDP, segue em frente

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