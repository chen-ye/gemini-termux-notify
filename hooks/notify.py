#!/usr/bin/env python3
import sys
import json
import subprocess

def notify(title, content):
    subprocess.run([
        "termux-notification",
        "--title", title,
        "--content", content,
        "--id", "gemini_agent",
        "--priority", "high"
    ])

def main():
    try:
        # Read JSON from stdin
        raw_input = sys.stdin.read()
        if not raw_input:
            return
        data = json.loads(raw_input)
    except Exception as e:
        sys.stderr.write(f"Error parsing JSON: {e}\n")
        return

    event = data.get("hook_event_name")
    
    if event == "AfterAgent":
        # Extract the response preview (first 100 chars)
        response = data.get("prompt_response", "Tasks completed.")
        if response:
             preview = (response[:97] + '...') if len(response) > 97 else response
             notify("Gemini Agent Finished", preview)
        else:
             notify("Gemini Agent Finished", "Tasks completed.")

    elif event == "Notification":
        message = data.get("message", "Attention required.")
        notify("Gemini Alert", message)

if __name__ == "__main__":
    main()

