# momair
Minutes of Meeting,Action Item Register Generator

# 📝 meetgen_ollama

**meetgen_ollama.py** is a local meeting assistant tool that uses an LLM via [Ollama](https://ollama.com) to generate:

- ✅ Detailed **Minutes of Meeting**
- ✅ An **Action Item Register** with owners, deadlines, and statuses

---

## 🚀 Features

- 📜 Accepts any `.txt` transcript from Microsoft Teams, Zoom, or in-person meetings
- 🧠 Uses **Mistral** (default) or **Phi-3** models locally via Ollama
- 📂 Outputs:
  - `minutes_and_air.txt` – summary + action register
  - `prompt_used.txt` – the prompt sent to the model
  - `raw_output.txt` – raw model output (debugging)
- 📅 Automatically opens the result after generation
- ⏱️ Shows processing time and countdown before opening
- 🛠️ Logs errors to `mom_air/error.log`

---

## 🧰 Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- Mistral and/or Phi-3 model pulled:
  ```bash
  ollama run mistral
  ollama run phi3
  ```

---

## 📦 Installation

1. Clone or download the script:
   ```
   git clone <your_repo>
   cd momair
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure Ollama is running:
   ```
   ollama run mistral
   ```

---

## 🛠️ Usage (Python)

```bash
python meetgen_ollama.py meeting.txt --model mistral
```

```bash
python meetgen_ollama.py meeting.txt --model phi3
```

---

## ▶️ Usage (via Batch File on Windows)

Use the included batch launcher:

```bash
gen_momair.bat
```

It will:
- Prompt you to enter the `.txt` file path
- Let you choose Mistral or Phi-3
- Run the script and open the result

---

## 📁 Output Files

All output will be saved in a folder named `mom_air/`:

| File                    | Description                           |
|-------------------------|---------------------------------------|
| `minutes_and_air.txt`   | Final summary + action register       |
| `prompt_used.txt`       | Prompt sent to LLM                    |
| `raw_output.txt`        | Full raw response from the model      |
| `error.log`             | Any runtime errors                    |

---

## 📌 Notes

- This tool assumes Ollama is already running locally
- Best used for short-to-medium transcripts (~1–10 pages)
- Works on Windows 11 Pro, CPU-only or with GPU

---

## 🧑‍💼 Sample Transcript Format

```
Ben: Welcome to the meeting.
Sarah: Let's begin with the server upgrade.
Alice: I’ll present the audit findings...
```

---

## 📬 Credits

Built with ❤️ to simplify meeting documentation with local AI.

