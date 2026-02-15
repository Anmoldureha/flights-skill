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

### OpenClaw
Add this repo to your skills directory and map `flight_search` to:
`venv/bin/python3 search.py {{from}} {{to}} {{date}}`

### Claude Code (MCP)
Coming soon: MCP Server wrapper for Claude Desktop.
