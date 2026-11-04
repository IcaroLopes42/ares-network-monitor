# 👁️ ARES - Real-Time Network Threat Detection System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: In Development](https://img.shields.io/badge/Status-In_Development-cyan.svg)]()

> 🇧🇷 *Para a versão em Português, leia abaixo. / 🇺🇸 For the English version, scroll down.*

---

## 🇧🇷 Português

O **ARES** é uma ferramenta de monitoramento de tráfego de rede e detecção de ameaças em tempo real, construída em Python e desenhada nativamente para o terminal. 

Diferente de analisadores tradicionais que geram uma cascata infinita de logs ilegíveis, o ARES utiliza uma **arquitetura baseada em estado**. Ele monitora os pacotes usando `pyshark` e consolida as informações por endereço IP em um painel dinâmico e fixo. Isso permite identificar quais aplicativos cada host está acessando (via TLS SNI e DNS) e detectar anomalias de tráfego instantaneamente.

### 🚀 Funcionalidades Principais
* **Visualização Baseada em Estado:** Acompanhamento de IPs em tempo real em uma tabela fixa, eliminando a poluição visual de logs contínuos.
* **Identificação de Aplicações:** Inspeção profunda de pacotes (DPI) baseada em requisições DNS e `Server Name Indication` (SNI) durante *handshakes* TLS para mapear o tráfego para aplicativos reais (ex: YouTube, WhatsApp, Netflix).
* **Interface Tática de Terminal:** Painéis assíncronos renderizados com a biblioteca `rich`, proporcionando uma experiência de dashboard limpa, colorida e responsiva direto no CLI.
* **Detecção de Anomalias (Em breve):** Alertas automatizados para comportamentos suspeitos, como picos anômalos de pacotes (ataques de *Flood/DoS*) e varreduras de portas.

### 🛠️ Stack Tecnológica
* **Linguagem:** Python 3
* **Motor de Captura:** `pyshark` (Wrapper para TShark/Wireshark)
* **Interface (TUI):** `rich` e `rich.live`
* **Concorrência:** Operação baseada em *Threads/Asyncio* para separar a captura de pacotes da renderização visual.

### 🗺️ Roadmap de Desenvolvimento
- [ ] **Sprint 1:** Motor core de captura e dicionário de estado.
- [ ] **Sprint 2:** Lógica de identificação de aplicativos via DNS/SNI.
- [ ] **Sprint 3:** Renderização assíncrona do dashboard com `rich`.
- [ ] **Sprint 4:** Módulo de segurança, alertas e *Garbage Collection* de IPs inativos.

---

## 🇺🇸 English

**ARES** is a real-time network traffic monitoring and threat detection tool, built in Python and natively designed for the terminal.

Unlike traditional analyzers that generate an infinite cascade of unreadable logs, ARES uses a **state-based architecture**. It sniffs packets using `pyshark` and consolidates the information per IP address into a dynamic, fixed dashboard. This allows you to identify which applications each host is accessing (via TLS SNI and DNS) and instantly spot traffic anomalies.

### 🚀 Key Features
* **State-Based Visualization:** Real-time IP tracking in a fixed table, eliminating the visual clutter of continuous log streams.
* **Application Fingerprinting:** Deep Packet Inspection (DPI) based on DNS queries and `Server Name Indication` (SNI) during TLS handshakes to map traffic to actual apps (e.g., YouTube, WhatsApp, Netflix).
* **Tactical Terminal Interface:** Asynchronous panels rendered with the `rich` library, providing a clean, colorful, and responsive dashboard experience directly in the CLI.
* **Anomaly Detection (Upcoming):** Automated alerts for suspicious network behavior, such as anomalous packet spikes (Flood/DoS attacks) and port scanning.

### 🛠️ Tech Stack
* **Language:** Python 3
* **Capture Engine:** `pyshark` (TShark/Wireshark wrapper)
* **Interface (TUI):** `rich` and `rich.live`
* **Concurrency:** *Thread/Asyncio* based operation to decouple packet sniffing from UI rendering.

### 🗺️ Development Roadmap
- [ ] **Sprint 1:** Core capture engine and state dictionary.
- [ ] **Sprint 2:** Application identification logic via DNS/SNI.
- [ ] **Sprint 3:** Asynchronous dashboard rendering using `rich`.
- [ ] **Sprint 4:** Security module, alerts, and Garbage Collection for inactive IPs.

---

### 📝 Licença / License
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. / This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
