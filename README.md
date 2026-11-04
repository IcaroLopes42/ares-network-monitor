# 👁️ ARES - Real-Time Network Sentinel & Threat Detection

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker Support](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active Development](https://img.shields.io/badge/Status-Active_Development-cyan.svg)]()

> 🇺🇸 *For the English version, read below. / 🇧🇷 Para a versão em Português, role para baixo.*

---

## 🇺🇸 English

**ARES** is a real-time network traffic monitoring and threat detection tool, built in Python and natively designed for the terminal.

Unlike traditional analyzers that generate an infinite cascade of unreadable logs, ARES uses a **state-based architecture**. It sniffs packets using `pyshark` and consolidates the information per IP address into a dynamic, fixed dashboard. It leverages Deep Packet Inspection (DPI) via TLS SNI and DNS to map traffic to actual applications, providing a clean, tactical view of network behavior and instant anomaly detection.

Designed with **DevSecOps** and **SRE** principles in mind, ARES is built to be containerized, automated via CI/CD, and easily integrated into modern observability stacks.

### 🚀 Key Features
* **State-Based Visualization:** Real-time IP tracking in a fixed UI table, eliminating log clutter.
* **Application Fingerprinting:** Inspects DNS queries and `Server Name Indication` (SNI) during TLS handshakes to map traffic to apps (e.g., YouTube, WhatsApp, AWS Services).
* **Tactical Terminal Interface:** Asynchronous panels rendered with the `rich` library directly in the CLI.
* **Observability & DevOps Ready:** Engineered to export time-series metrics to InfluxDB for Grafana visualization, fully containerized via Docker.
* **Security & Anomaly Alerts (Upcoming):** Automated warnings for anomalous packet spikes (Flood/DoS) and port scanning.

### 🛠️ Tech Stack
* **Core:** Python 3, `pyshark` (TShark/Wireshark wrapper), `rich` (TUI), Asyncio.
* **Observability (Ops):** InfluxDB, Grafana.
* **Infrastructure & CI/CD:** Docker, GitHub Actions (SAST with Trivy/Bandit), Terraform.

### 🗺️ Development Roadmap
- [ ] **Sprint 1:** Core capture engine, state dictionary, and CI/CD foundations.
- [ ] **Sprint 2:** Application identification logic via DNS/SNI.
- [ ] **Sprint 3:** Asynchronous dashboard rendering using `rich`.
- [ ] **Sprint 4:** Security module, threat alerts, and garbage collection.
- [ ] **Sprint 5 (DevSecOps):** Docker Compose environment, InfluxDB exporter, Grafana Dashboards, and IaC (Terraform).

---

## 🇧🇷 Português

O **ARES** é uma ferramenta de monitoramento de tráfego de rede e detecção de ameaças em tempo real, desenhada nativamente para o terminal.

Diferente de analisadores tradicionais que geram cascatas de logs ilegíveis, o ARES utiliza uma **arquitetura baseada em estado**. Ele monitora os pacotes usando `pyshark` e consolida as informações por IP em um painel dinâmico. Através de Inspeção Profunda de Pacotes (DPI) via TLS SNI e DNS, ele mapeia o tráfego para aplicativos reais, oferecendo uma visão tática do comportamento da rede.

Projetado com foco em **DevSecOps** e **SRE**, o ARES é estruturado para ser containerizado, validado por CI/CD e integrado nativamente a stacks de observabilidade corporativas.

### 🚀 Funcionalidades Principais
* **Visualização Baseada em Estado:** Acompanhamento de IPs em uma tabela fixa, eliminando a poluição visual.
* **Identificação de Aplicações:** Inspeção de DNS e `Server Name Indication` (SNI) em *handshakes* TLS para mapear aplicativos (ex: YouTube, WhatsApp).
* **Interface Tática de Terminal:** Painéis assíncronos renderizados com a biblioteca `rich`.
* **Pronto para Observabilidade (DevOps):** Arquitetado para exportar métricas para o InfluxDB e Grafana, com deploy via Docker.
* **Detecção de Anomalias (Em breve):** Alertas automatizados para Flood/DoS e varreduras de portas.

### 🗺️ Roadmap de Desenvolvimento
- [ ] **Sprint 1:** Motor core de captura, dicionário de estado e base de CI/CD.
- [ ] **Sprint 2:** Lógica de identificação de aplicações via DNS/SNI.
- [ ] **Sprint 3:** Renderização assíncrona do dashboard com `rich`.
- [ ] **Sprint 4:** Módulo de segurança, alertas de ameaças e *Garbage Collection*.
- [ ] **Sprint 5 (DevSecOps):** Ambiente Docker Compose, exportador InfluxDB, Dashboards no Grafana e IaC (Terraform).

---
### 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
