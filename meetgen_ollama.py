
import argparse
import requests
import json
from pathlib import Path
import webbrowser
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
OUTPUT_DIR = Path("mom_air")
OUTPUT_DIR.mkdir(exist_ok=True)

def prompt_llm_streaming(prompt, model="mistral"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": True
        },
        stream=True,
        timeout=300
    )

    output = ""
    chunk_count = 0
    start_time = time.time()

    try:
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode().removeprefix("data: ").strip())
                    if "response" in chunk:
                        output += chunk["response"]
                        chunk_count += 1
                except Exception as e:
                    Path(OUTPUT_DIR / "error.log").write_text(f"Chunk parsing error: {e}", encoding="utf-8")
        duration = time.time() - start_time
        print(f"[✓] Completed in {int(duration)} seconds with {chunk_count} chunks.")
        print("Displaying results in 5 seconds...")
        for i in range(5, 0, -1):
            print(f"Opening in {i}...", end="\r")
            time.sleep(1)
        print(" " * 20, end="\r")
    except Exception as e:
        Path(OUTPUT_DIR / "error.log").write_text(f"Ollama communication error: {e}", encoding="utf-8")
        return ""

    return output

def extract_minutes_and_actions(transcript_text, model="mistral"):
    prompt = f"""You are a professional meeting assistant. Based on the transcript below, generate:

1. A detailed summary of the discussion, grouped by topic or agenda item. Include who said what and any supporting details.
2. A clear list of key decisions made, specifying the decision owner or proposer if possible.
3. A table of action items with the following columns: Task Description, Owner, Deadline, and Status.

Format the output in plain text using section headers, bullet points, and a clear text table.

Transcript:
{transcript_text}
"""

    (OUTPUT_DIR / "prompt_used.txt").write_text(prompt, encoding="utf-8")
    output = prompt_llm_streaming(prompt, model=model)
    (OUTPUT_DIR / "raw_output.txt").write_text(output or "NO OUTPUT", encoding="utf-8")
    return output

def main():
    parser = argparse.ArgumentParser(description="Generate MoM + AIR from transcript")
    parser.add_argument("transcript_file", help="Path to transcript text file")
    parser.add_argument("--model", choices=["mistral", "phi3"], default="mistral",
                        help="LLM model to use: 'mistral' (default) or 'phi3'")
    args = parser.parse_args()

    try:
        transcript = Path(args.transcript_file).read_text(encoding="utf-8")
    except Exception as e:
        Path(OUTPUT_DIR / "error.log").write_text(f"Failed to read transcript: {e}", encoding="utf-8")
        print(f"[!] Failed to read transcript: {e}")
        return

    print(f"[~] Sending prompt to Ollama (detailed MoM)...")
    output_text = extract_minutes_and_actions(transcript, model=args.model)

    output_path = OUTPUT_DIR / "minutes_and_air.txt"
    if output_text.strip():
        output_path.write_text(output_text.strip(), encoding="utf-8")
    else:
        output_path.write_text("LLM returned no output.", encoding="utf-8")

    try:
        webbrowser.open(str(output_path.resolve()))
    except Exception as e:
        Path(OUTPUT_DIR / "error.log").write_text(str(e), encoding="utf-8")

if __name__ == "__main__":
    main()
