@echo off
setlocal ENABLEEXTENSIONS

:: Ask for transcript file
set /p transcript="Enter path to transcript file (e.g., meeting.txt): "

:: Ask for model selection
echo Select LLM model:
echo [1] Mistral (default)
echo [2] Phi-3
set /p model_choice="Enter choice (1 or 2): "

if "%model_choice%"=="2" (
    set model=phi3
) else (
    set model=mistral
)

echo Running meetgen_ollama.py with model %model%...
python meetgen_ollama.py "%transcript%" --model %model%

pause
