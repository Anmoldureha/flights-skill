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

## 🌟 Why is this great? (The Advantage)

Most flight search APIs are broken, expensive, or stale. This tool solves the "Google Flights Data Problem":

### 1. 🧠 AI-Native Design
Most scrapers return messy HTML. This tool outputs **clean, structured JSON** specifically optimized for LLM consumption.
*   **Lower Token Cost**: No fluff, just data.
*   **Higher Accuracy**: Agents don't have to hallucinate parsing logic.

### 2. ⚡ The "Impossible" API
Google discontinued their public Flights API in 2018. Developers have been forced to use:
*   **Expensive Aggregators** (Amadeus/Duffel): Cost $0.002+ per request and require KYC.
*   **Slow Selenium Bots**: Break easily and take 10s+ to load.
*   **Stale Data**: Most APIs cache prices for 24 hours.

**This tool hacks the matrix.** It reverse-engineers the Protobuf data stream used by Google's own frontend, giving you **Enterprise-grade speed (ms)** without the Enterprise price tag.

### 3. 🛡️ Local & Private
Runs 100% on your machine (or your agent's container). No third-party server logging your travel plans or selling your search intent data to airlines.

