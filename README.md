# 🤖 Abbiramana S — AI Portfolio Website

A sleek, dark-themed portfolio website with an embedded **Claude Opus AI agent chatbot** that knows everything about Abbiramana S and can answer visitor questions.

---

## 🗂 Project Structure

```
portfolio/
├── app.py                  ← Flask backend + Claude Opus API
├── requirements.txt        ← Python dependencies
├── .env.example            ← Environment variable template
├── templates/
│   └── index.html          ← Full portfolio frontend
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone / Download the project
```bash
cd portfolio
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
# Edit .env and add your Anthropic API key:
# ANTHROPIC_API_KEY=sk-ant-...
```

Get your API key at: https://console.anthropic.com

### 5. Run the app
```bash
python app.py
```

Visit → http://localhost:5000

---

## 🤖 How the AI Agent Works

- Uses **Claude claude-opus-4-6** (most powerful Claude model)
- Pre-loaded with Abbiramana's full profile: skills, experience, projects, certifications
- Maintains conversation history for multi-turn chat
- Visitors can ask: *"What are his ML skills?"*, *"Has he published anything?"*, *"Is he open to work?"*, etc.

---

## 🚀 Deployment (Free Options)

### Option A: Render.com (Recommended)
1. Push code to GitHub
2. Go to render.com → New Web Service
3. Connect your GitHub repo
4. Set `ANTHROPIC_API_KEY` as an environment variable
5. Set start command: `python app.py`
6. Deploy!

### Option B: Railway.app
1. Push to GitHub
2. railway.app → New Project → Deploy from GitHub
3. Add `ANTHROPIC_API_KEY` in environment variables

### Option C: Heroku
```bash
heroku create abbiramana-portfolio
heroku config:set ANTHROPIC_API_KEY=your_key
git push heroku main
```

---

## 🎨 Tech Stack

| Layer | Tech |
|-------|------|
| Backend | Python + Flask |
| AI Agent | Anthropic Claude claude-opus-4-6 |
| Frontend | HTML5 + CSS3 + Vanilla JS |
| Fonts | Syne + JetBrains Mono |
| Particles | Canvas API |

---

## 📌 Customization Tips

- **Update profile**: Edit `PROFILE_CONTEXT` in `app.py` when you add new projects/jobs
- **Change colors**: Edit CSS variables in `index.html` (`:root` block)
- **Add resume download**: Place your PDF as `static/assets/resume.pdf` and update the download button link
- **Add more sections**: Extend `index.html` with education timeline, contact form, etc.

---

Built with ❤️ using Flask + Claude Opus | Abbiramana S · Salem, Tamil Nadu 🇮🇳
