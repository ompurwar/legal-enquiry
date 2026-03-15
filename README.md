# Kanoon Mitra – Indian Legal Advisory Bot ⚖️

An AI-powered legal advisory chatbot for Indian law, built with Python (Flask) and Anthropic Claude. It provides guidance on **BNS**, **BNSS**, **BSA**, personal laws, and landmark Supreme Court cases.

---

## Features

| Feature | Details |
|---|---|
| 🤖 AI advisor | Powered by Anthropic Claude (claude-3-5-sonnet) |
| 📚 Legal knowledge base | BNS (IPC replacement), BNSS (CrPC replacement), BSA (Evidence Act replacement) |
| 💍 Personal laws | Hindu Marriage Act, Muslim Personal Law, Special Marriage Act, PWDVA, Dowry Prohibition Act |
| ⚖️ Landmark cases | Shah Bano, Shayara Bano, Vishaka, Kesavananda Bharati, Nirbhaya, Danial Latifi, and more |
| 🔍 Interpretation engine | Auto-identifies applicable laws and sections from a user's natural-language query |
| 💬 Chat UI | WhatsApp-style interface with **double-tick read receipts** |
| 🌐 Bilingual | Supports English and Hindi / Hinglish queries |

---

## Laws Covered

### Criminal Laws (effective 1 July 2024)
| New Act | Replaces |
|---|---|
| Bharatiya Nyaya Sanhita (BNS), 2023 | Indian Penal Code (IPC), 1860 |
| Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 | Code of Criminal Procedure (CrPC), 1973 |
| Bharatiya Sakshya Adhiniyam (BSA), 2023 | Indian Evidence Act, 1872 |

### Personal / Family Laws
- Hindu Marriage Act, 1955
- Muslim Personal Law (Shariat) Application Act, 1937 (Nikah, Mehr, Talaq, Iddat)
- Special Marriage Act, 1954 (inter-religion / court marriages)
- Protection of Women from Domestic Violence Act (PWDVA), 2005
- Dowry Prohibition Act, 1961
- Muslim Women (Protection of Rights on Divorce) Act, 1986
- Muslim Women (Protection of Rights on Marriage) Act, 2019 (anti-triple-talaq)

### Landmark Supreme Court Cases
- **Shah Bano** (1985) – Muslim maintenance beyond iddat
- **Shayara Bano** (2017) – Triple talaq declared unconstitutional
- **Danial Latifi** (2001) – Life-long maintenance for Muslim divorced women
- **Vishaka** (1997) – Sexual harassment at workplace (precursor to POSH Act)
- **Kesavananda Bharati** (1973) – Basic structure doctrine
- **Maneka Gandhi** (1978) – Article 21, right to life with dignity
- **Nirbhaya / Mukesh** (2017) – Gang rape death penalty

---

## Quick Start

### Prerequisites
- Python 3.11+
- An [Anthropic API key](https://console.anthropic.com/)

### Installation

```bash
# Clone the repository
git clone https://github.com/ompurwar/legal-enquiry.git
cd legal-enquiry

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Open .env and set ANTHROPIC_API_KEY=sk-ant-...

# Run the application
python app.py
```

Open your browser at **http://localhost:5000** to start chatting.

> **Demo mode**: If `ANTHROPIC_API_KEY` is not set, the app runs in demo mode and shows the interpretation engine results (applicable law sections) without an AI-generated explanation.

---

## REST API

### `POST /api/chat`
Send a legal query and receive an AI-powered response.

**Request:**
```json
{
  "message": "My husband is demanding dowry. What can I do?",
  "history": []
}
```

**Response:**
```json
{
  "reply": "Under the Dowry Prohibition Act, 1961 ...",
  "legal_refs": {
    "domains": ["family"],
    "bns_sections": [{"section": "84", "title": "Dowry death"}],
    "personal_law": [{"law": "Dowry Prohibition Act", ...}],
    "cases": []
  }
}
```

### `GET /api/laws/search?q=<query>`
Search the legal knowledge base without calling the AI.

### `GET /api/health`
Health check.

---

## Architecture

```
legal-enquiry/
├── app.py                        # Flask application & routes
├── requirements.txt
├── .env.example
├── legal_engine/
│   ├── interpreter.py            # Query → law mapping (interpretation engine)
│   └── laws/
│       ├── bns.py                # Bharatiya Nyaya Sanhita sections
│       ├── bnss.py               # Bharatiya Nagarik Suraksha Sanhita sections
│       ├── evidence.py           # Bharatiya Sakshya Adhiniyam sections
│       ├── personal_laws.py      # Marriage acts, PWDVA, Dowry Act
│       └── case_law.py           # Landmark Supreme Court cases
├── templates/
│   └── index.html                # Chat UI (WhatsApp-style with double ticks)
├── static/
│   ├── css/style.css
│   └── js/app.js
└── tests/
    └── test_legal_system.py
```

---

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## Disclaimer

This application provides **general legal information only** and is **not a substitute for professional legal advice**. Always consult a qualified and licensed advocate for advice specific to your situation. Laws may be amended — always verify current provisions.
