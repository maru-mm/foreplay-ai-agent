# ⚡ Quick Deploy Guide

## 🚀 Deploy su Fly.io in 5 minuti

### Step 1: Installa Fly CLI

**macOS:**
```bash
brew install flyctl
```

**Altri OS:** Vedi [DEPLOYMENT.md](DEPLOYMENT.md)

### Step 2: Login

```bash
flyctl auth login
```

### Step 3: Launch (NON deployare ancora)

```bash
cd "/Users/mac/Desktop/wasa/foreplay API"
flyctl launch --no-deploy
```

Rispondi:
- ✅ Use existing fly.toml
- ❌ No PostgreSQL
- ❌ No Redis

### Step 4: Configura API Key

```bash
flyctl secrets set FOREPLAY_API_KEY="LA_TUA_API_KEY"
```

### Step 5: Deploy!

```bash
flyctl deploy
```

### Step 6: Apri

```bash
flyctl open
```

## ✅ Done!

La tua app sarà disponibile su: `https://foreplay-ai-agent.fly.dev`

---

## 🔧 Setup Locale (Test)

### 1. Crea .env

```bash
cp env.example .env
```

Modifica `.env` e inserisci la tua API key:
```
FOREPLAY_API_KEY=your_actual_key_here
```

### 2. Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

### 3. Installa

```bash
pip install -r requirements.txt
pip install -r requirements_gui.txt
```

### 4. Run

```bash
streamlit run foreplay_gui.py
```

Apri: http://localhost:8501

---

## 📱 Comandi Utili Fly.io

```bash
# Logs in tempo reale
flyctl logs

# Status
flyctl status

# Riavvia
flyctl apps restart foreplay-ai-agent

# SSH
flyctl ssh console

# Scala risorse
flyctl scale memory 1024  # 1GB RAM
```

---

## 🆘 Problemi?

Vedi [DEPLOYMENT.md](DEPLOYMENT.md) per troubleshooting dettagliato.

