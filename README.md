# ✈️ Flights Skill for OpenClaw/Claude

A powerful, Python-based flight search tool wrapping the [fast-flights](https://github.com/AWeirdDev/flights) library. Designed to be used as an Agent Skill (OpenClaw) or MCP Server.

## 🚀 Features
- **Real-time Google Flights Data**: Scrapes live prices via Protobuf reverse-engineering.
- **Structured Output**: Returns clean JSON for AI consumption.
- **Fast**: No browser automation required (uses `requests` fallback).
- **Unit Tested**: Includes comprehensive test suite.

## 📦 Installation

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/Anmoldureha/flights-skill.git
    cd flights-skill
    ```

2.  **Set up Python environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install fast-flights typing-extensions
    ```

## 🛠️ Usage

Run the script directly from the command line:

```bash
# Syntax: python search.py ORIGIN DEST DATE
python search.py SFO JFK 2026-03-01
```

**Output:**
```json
{
  "current_price": "typical",
  "flights": [
    {
      "name": "Delta",
      "price": "$120",
      "duration": "5h 30m",
      ...
    }
  ]
}
```

## 🧪 Testing

Run the unit tests to verify logic:

```bash
python3 tests/test_search.py
```

## 🤖 Agent Integration

### Claude Code (MCP)
This repo includes a native **MCP Server** implementation (compatible with Claude Desktop).

1.  Add to your `claude_desktop_config.json`:
    ```json
    {
      "mcpServers": {
        "flights": {
          "command": "/absolute/path/to/skills/flights/venv/bin/python3",
          "args": ["/absolute/path/to/skills/flights/mcp_server.py"]
        }
      }
    }
    ```
2.  Restart Claude Desktop. You can now ask: "Find me cheap flights to Tokyo".

### OpenClaw
Add this repo to your skills directory and map `flight_search` to:
`venv/bin/python3 search.py {{from}} {{to}} {{date}}`

## 🌟 Why is this great?

Unlike traditional Flight APIs (Amadeus, Duffel, Skyscanner), this skill is:

*   **Real-Time & Accurate**: It scrapes Google Flights directly, so you see the *actual* price (no cached/stale GDS data).
*   **Zero Cost**: No API keys, no monthly subscription, no rate limits (within reason).
*   **Lightweight**: Uses Protobuf reverse-engineering instead of heavy browser automation (Playwright/Selenium), making it 10x faster and resource-efficient.
*   **Privacy-Friendly**: Runs locally on your machine.

