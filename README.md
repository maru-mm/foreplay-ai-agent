# 🎬 Foreplay AI Agent - Transcript Extractor

Applicazione web interattiva per estrarre automaticamente i transcript video dalle board di Foreplay.

## 🚀 Features

- ✅ Estrazione automatica transcript da board Foreplay
- 📊 Visualizzazione interattiva dei risultati
- 📥 Export in CSV, Excel e JSON
- ⚡ Export rapido (solo campi essenziali)
- 🎯 Segmenti timestampati dettagliati
- 💳 Monitoraggio crediti API

## 📋 Prerequisiti

- Python 3.11+
- Account Foreplay con API key
- (Per deployment) Account Fly.io

## 🔧 Installazione Locale

### 1. Clone del repository

```bash
git clone https://github.com/maru-mm/foreplay-ai-agent.git
cd foreplay-ai-agent
```

### 2. Creazione virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

### 3. Installazione dipendenze

```bash
pip install -r requirements.txt
pip install -r requirements_gui.txt
```

### 4. Configurazione API Key

Crea un file `.env` nella root del progetto:

```bash
FOREPLAY_API_KEY=your_api_key_here
```

### 5. Avvio applicazione

```bash
streamlit run foreplay_gui.py
```

L'applicazione sarà disponibile su `http://localhost:8501`

## 🐳 Docker

### Build immagine

```bash
docker build -t foreplay-ai-agent .
```

### Run container

```bash
docker run -p 8501:8501 -e FOREPLAY_API_KEY=your_api_key foreplay-ai-agent
```

## ☁️ Deploy su Fly.io

### 1. Installa Fly CLI

```bash
# macOS
brew install flyctl

# Linux
curl -L https://fly.io/install.sh | sh

# Windows
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

### 2. Login

```bash
flyctl auth login
```

### 3. Lancia l'app

```bash
flyctl launch
```

Durante il processo:
- Conferma il nome dell'app: `foreplay-ai-agent`
- Scegli la region (es. `ams` per Amsterdam)
- **NON** creare un database PostgreSQL
- **NON** deployare subito

### 4. Configura secrets

```bash
flyctl secrets set FOREPLAY_API_KEY=your_actual_api_key_here
```

### 5. Deploy

```bash
flyctl deploy
```

### 6. Apri l'app

```bash
flyctl open
```

## 📱 Utilizzo

1. **Inserisci URL Board**: Copia l'URL di una board Foreplay (es. `https://app.foreplay.co/boards/BOARD_ID`)
2. **Estrai Transcript**: Clicca su "Estrai Transcript"
3. **Visualizza Risultati**: Esplora i transcript nella tab "Visualizza Transcript"
4. **Esporta Dati**: 
   - ⚡ Export rapido (3 campi: id, nome, transcript)
   - 📊 Export completo (tutti i campi)
   - ⏱️ Export timestampato (segmenti con timing)

## 📂 Struttura Progetto

```
foreplay-ai-agent/
├── foreplay_gui.py          # Interfaccia Streamlit
├── foreplay_client.py       # Client API Foreplay
├── config.py                # Configurazione
├── requirements.txt         # Dipendenze base
├── requirements_gui.txt     # Dipendenze GUI
├── Dockerfile               # Container Docker
├── fly.toml                 # Configurazione Fly.io
├── .gitignore              # File da escludere da Git
└── README.md               # Questo file
```

## 🔑 Variabili d'Ambiente

| Variabile | Descrizione | Richiesta | Default |
|-----------|-------------|-----------|---------|
| `FOREPLAY_API_KEY` | API key di Foreplay | ✅ Sì | - |
| `FOREPLAY_BASE_URL` | URL base API | ❌ No | `https://public.api.foreplay.co/` |

## 🛠️ Comandi Fly.io Utili

```bash
# Visualizza logs
flyctl logs

# Controlla status
flyctl status

# SSH nell'app
flyctl ssh console

# Scala risorse
flyctl scale vm shared-cpu-1x --memory 512

# Visualizza secrets
flyctl secrets list

# Aggiorna secret
flyctl secrets set FOREPLAY_API_KEY=new_key

# Riavvia app
flyctl apps restart foreplay-ai-agent
```

## 📊 Formati Export

### ⚡ Export Rapido (Consigliato)
- `ad_id`: ID univoco dell'ad
- `name`: Nome dell'ad
- `full_transcription`: Transcript completo

### 📋 Export Completo
Include tutti i campi:
- Informazioni base (id, name, brand_id)
- Contenuto (description, headline, transcript)
- Metadata (durata, piattaforma, formato)
- Link (video_url, link_url)

### ⏱️ Export Timestampato
Ogni riga = un segmento:
- `ad_id`, `name`
- `start_time`, `end_time`
- `sentence` (testo del segmento)

## 🐛 Troubleshooting

### Errore API Key
```
⚠️ API Key non configurata!
```
**Soluzione**: Verifica che la variabile `FOREPLAY_API_KEY` sia impostata correttamente.

### Errore Port Binding (Docker)
```
Error: port 8501 already in use
```
**Soluzione**: Cambia porta: `docker run -p 8080:8501 ...`

### Deploy Fly.io fallito
```bash
# Controlla logs
flyctl logs

# Verifica configurazione
flyctl config validate
```

## 🔒 Sicurezza

- ⚠️ **NON** commitare mai l'API key nel repository
- ✅ Usa sempre variabili d'ambiente
- ✅ File `.env` è escluso da Git
- ✅ Secrets su Fly.io sono criptati

## 📝 Note

- I file JSON generati **non vengono salvati** sul server
- Usa il bottone download per salvare localmente
- I crediti API vengono monitorati automaticamente
- L'app su Fly.io si spegne automaticamente quando inattiva (auto_stop_machines)

## 🤝 Contributi

Contributi, issues e feature requests sono benvenuti!

## 📄 License

MIT

## 👤 Author

**Wasa**

---

Made with ❤️ for Foreplay API integration
