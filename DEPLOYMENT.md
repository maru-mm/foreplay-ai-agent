# 🚀 Guida Deployment Fly.io

## Prerequisiti

- Account Fly.io (gratuito): https://fly.io/app/sign-up
- Fly CLI installato
- API Key Foreplay

## 📦 Step-by-Step Deployment

### 1. Installa Fly CLI

**macOS:**
```bash
brew install flyctl
```

**Linux:**
```bash
curl -L https://fly.io/install.sh | sh
```

**Windows:**
```powershell
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

### 2. Autenticazione

```bash
flyctl auth login
```

Si aprirà il browser per il login.

### 3. Prima Configurazione (già fatto)

Il file `fly.toml` è già configurato con:
- Nome app: `foreplay-ai-agent`
- Region: `ams` (Amsterdam)
- Porta: 8501
- Auto-scaling: ✅
- Memoria: 512MB

### 4. Crea l'app su Fly.io

```bash
flyctl launch --no-deploy
```

Rispondi:
- ✅ Use existing fly.toml
- ❌ No database PostgreSQL
- ❌ No Redis

### 5. Configura Secrets (IMPORTANTE)

```bash
flyctl secrets set FOREPLAY_API_KEY="tua_api_key_qui"
```

Verifica:
```bash
flyctl secrets list
```

Output atteso:
```
NAME                DIGEST              DATE
FOREPLAY_API_KEY    xxxxxxxxxxxxx       1m ago
```

### 6. Deploy!

```bash
flyctl deploy
```

Il processo:
1. Build Docker image
2. Push su Fly.io registry
3. Deploy su macchina virtuale
4. Health check

### 7. Apri l'app

```bash
flyctl open
```

L'URL sarà: `https://foreplay-ai-agent.fly.dev`

## 🔧 Configurazione Avanzata

### Cambia Region

Modifica `fly.toml`:
```toml
primary_region = "lhr"  # London
# Altre: ams, fra, iad, ord, sjc, syd, etc.
```

Poi:
```bash
flyctl deploy
```

### Scala Risorse

**Più memoria:**
```bash
flyctl scale memory 1024  # 1GB
```

**Più CPU:**
```bash
flyctl scale vm shared-cpu-2x
```

### Auto-scaling (già abilitato)

In `fly.toml`:
```toml
[http_service]
  auto_stop_machines = true   # Spegne quando inattivo
  auto_start_machines = true  # Riavvia al primo accesso
  min_machines_running = 0    # Nessuna macchina sempre attiva (risparmio)
```

### Forza macchina sempre attiva

```bash
flyctl scale count 1 --max-per-region 1
```

E modifica `fly.toml`:
```toml
min_machines_running = 1
```

## 📊 Monitoring

### Logs in real-time

```bash
flyctl logs
```

### Status app

```bash
flyctl status
```

Output:
```
App
  Name     = foreplay-ai-agent
  Owner    = personal
  Hostname = foreplay-ai-agent.fly.dev
  Platform = machines

Machines
ID          STATE   REGION  HEALTH  CHECKS
xxx         started ams     passing 1 total
```

### Metriche

Dashboard: https://fly.io/apps/foreplay-ai-agent/monitoring

### SSH nell'app

```bash
flyctl ssh console
```

Comandi utili dentro la macchina:
```bash
# Verifica app in esecuzione
ps aux | grep streamlit

# Verifica file
ls -la /app

# Test locale
curl http://localhost:8501/_stcore/health
```

## 🔄 Aggiornamenti

### Deploy nuova versione

```bash
git pull  # Se usi Git
flyctl deploy
```

### Rollback

```bash
# Lista releases
flyctl releases

# Rollback a versione precedente
flyctl releases rollback <VERSION>
```

## 🐛 Troubleshooting

### App non si avvia

```bash
# Controlla logs
flyctl logs

# Verifica secrets
flyctl secrets list

# Rebuild completo
flyctl deploy --no-cache
```

### Errori comuni

**1. API Key non trovata:**
```
⚠️ API Key non configurata!
```
**Fix:**
```bash
flyctl secrets set FOREPLAY_API_KEY="your_key"
```

**2. Out of memory:**
```
Error: OOMKilled
```
**Fix:**
```bash
flyctl scale memory 1024
```

**3. Health check failed:**
```
Error: health check failed
```
**Fix:** Verifica che Streamlit sia in ascolto su `0.0.0.0:8501`

**4. Deploy timeout:**
```bash
# Aumenta timeout
flyctl deploy --wait-timeout 600
```

## 💰 Costi

### Free Tier (default)

- ✅ 3 shared-cpu-1x VMs (512MB RAM)
- ✅ 160GB outbound data transfer/mese
- ✅ Auto-stop incluso (risparmio)

Con `auto_stop_machines = true`, l'app usa risorse solo quando attiva!

### Stima costi mensili

- **Scenario 1**: Uso sporadico (auto-stop)
  - 💰 **$0-5/mese**

- **Scenario 2**: Always-on (min_machines_running = 1)
  - 💰 ~$10/mese

Dettagli: https://fly.io/docs/about/pricing/

## 🔒 Best Practices

### 1. Secrets Management

✅ **SI:**
```bash
flyctl secrets set API_KEY="secret"
```

❌ **NO:**
```toml
# fly.toml
[env]
  API_KEY = "secret"  # ⚠️ MAI fare così!
```

### 2. Monitoring

Aggiungi notifiche:
```bash
# Via email
flyctl webhooks create --type app-crashed --email your@email.com
```

### 3. Custom Domain

```bash
# Aggiungi dominio
flyctl certs create foreplay.tuodominio.com

# Ottieni record DNS
flyctl certs show foreplay.tuodominio.com
```

Poi aggiungi il record DNS:
```
CNAME foreplay.tuodominio.com -> foreplay-ai-agent.fly.dev
```

### 4. HTTPS (automatico)

Fly.io fornisce certificati SSL gratuiti via Let's Encrypt.

## 📚 Risorse Utili

- 📖 Docs Fly.io: https://fly.io/docs/
- 💬 Community: https://community.fly.io/
- 🐦 Twitter: @flydotio
- 📊 Status: https://status.fly.io/

## 🆘 Supporto

Problemi? Apri un issue su GitHub o contatta il supporto Fly.io.

---

**Buon deployment! 🚀**

