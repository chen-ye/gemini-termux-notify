# Gemini Termux Notify

Sends local system notifications via Termux:API when the Gemini agent finishes a turn or needs attention.

## Prerequisites

1.  **Termux:API App:** Ensure the [Termux:API Android app](https://play.google.com/store/apps/details?id=com.termux.api) is installed.
2.  **Termux:API Package:** Install the command-line tools in Termux:
    ```bash
    pkg install termux-api
    ```

## Installation

Install via Gemini CLI:

```bash
gemini extensions install https://github.com/chen-ye/gemini-termux-notify.git
```

## How it works

This extension registers hooks for:
- `AfterAgent`: Triggers when the agent finishes its response, showing a preview of the text.
- `Notification`: Triggers when an explicit notification is sent by the agent.

The notification includes a click action that opens the Termux app.

## Releasing

To publish a new version:

1.  Update the `version` field in `gemini-extension.json`.
2.  Commit and push the change to the `main` branch.

A GitHub Action will automatically detect the version change, create a git tag, and publish a GitHub Release.