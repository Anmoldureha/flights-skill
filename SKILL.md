# Flight Search Skill

Search for flights using Google Flights (via `fast-flights` library).

## Tools

### `flights_search`
Search for one-way flights between two airports on a specific date.

**Parameters:**
- `from`: Origin airport code (e.g. "SFO", "LHR").
- `to`: Destination airport code (e.g. "JFK", "DXB").
- `date`: Date in YYYY-MM-DD format.

**Usage:**
```javascript
// Search flights from SF to NY
flights_search({ from: "SFO", to: "JFK", date: "2026-03-01" })
```

**Implementation:**
The tool runs a Python script `search.py` in a virtual environment.

## Setup
Ensure `python3` is available.
Run `source venv/bin/activate && pip install fast-flights typing-extensions` to install dependencies.
