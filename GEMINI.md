# Project: gemini-termux-notify

## Overview
This is a **Gemini CLI Extension** designed to integrate with the Android system via the **Termux:API**. Its primary function is to send native system notifications when the Gemini agent completes a task or requires attention.

## Architecture
The project follows the standard structure of a Gemini CLI extension:

*   **`gemini-extension.json`**: The extension manifest defining metadata (name, version, author) and pointing to the hook configuration.
*   **`hooks/hooks.json`**: Configures the event listeners. It registers the `notify.py` script to run on two specific events:
    *   `AfterAgent`: Triggered after the agent completes a response.
    *   `Notification`: Triggered when an explicit notification is requested.
*   **`hooks/notify.py`**: The core logic implementation in Python. It:
    1.  Reads the event context JSON from `stdin`.
    2.  Parses the event type (`AfterAgent` or `Notification`).
    3.  Extracts relevant messages (e.g., response preview).
    4.  Executes the `termux-notification` command via `subprocess`.

## Prerequisites & Dependencies
To function correctly, the user's environment requires:
1.  **Termux:API Android App**: Must be installed on the device.
2.  **`termux-api` Package**: Must be installed in the Termux environment (`pkg install termux-api`).
3.  **Python 3**: Used to execute the hook script.

## Development Conventions
*   **Version Bumping**: Always increment the `version` field in `gemini-extension.json` whenever changes are made to the extension's logic (e.g., modifying `hooks/notify.py` or `hooks/hooks.json`). This ensures the automated release workflow triggers correctly.

## Development & Usage

### Testing
Since this relies on Termux APIs, testing is best done on an Android device within Termux.
You can simulate an event by piping JSON to the script:

```bash
# Simulate AfterAgent
echo '{"hook_event_name": "AfterAgent", "prompt_response": "Hello world"}' | python3 hooks/notify.py

# Simulate Notification
echo '{"hook_event_name": "Notification", "message": "Check this out"}' | python3 hooks/notify.py
```

### Installation
Extensions are typically installed via the CLI:
```bash
gemini extensions install .
```

### Releasing
The project uses GitHub Actions for automated releases:
1.  Bump the `version` in `gemini-extension.json`.
2.  Commit and push to `main`.
3.  The workflow in `.github/workflows/auto-release.yml` will detect the change, tag the commit, and publish a release.
