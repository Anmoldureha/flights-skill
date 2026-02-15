import sys
import json
import logging
from fast_flights import FlightData, Passengers, get_flights

# Configure logging to file since stdout is used for protocol
logging.basicConfig(filename='mcp_server.log', level=logging.INFO)

def search_logic(origin, dest, date):
    logging.info(f"Searching: {origin} -> {dest} on {date}")
    try:
        result = get_flights(
            flight_data=[FlightData(date=date, from_airport=origin, to_airport=dest)],
            trip="one-way",
            seat="economy",
            passengers=Passengers(adults=1, children=0, infants_in_seat=0, infants_on_lap=0),
            fetch_mode="fallback"
        )
        
        flights = []
        for f in result.flights[:10]: # Limit to top 10
            flights.append({
                "name": f.name,
                "price": f.price,
                "duration": f.duration,
                "departure": f.departure,
                "arrival": f.arrival,
                "stops": f.stops
            })
            
        return {
            "current_price": result.current_price,
            "flights": flights
        }
    except Exception as e:
        logging.error(f"Search failed: {e}")
        raise e

def handle_request(req):
    method = req.get("method")
    msg_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": { "tools": {} },
                "serverInfo": { "name": "flights-skill", "version": "1.0.0" }
            }
        }
    
    if method == "notifications/initialized":
        # Client confirming initialization. No response needed.
        return None
        
    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": [{
                    "name": "search_flights",
                    "description": "Search for one-way flights using Google Flights data (Real-time pricing).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "origin": { "type": "string", "description": "Origin Airport Code (e.g. SFO)" },
                            "destination": { "type": "string", "description": "Destination Airport Code (e.g. JFK)" },
                            "date": { "type": "string", "description": "Date in YYYY-MM-DD format" }
                        },
                        "required": ["origin", "destination", "date"]
                    }
                }]
            }
        }
        
    if method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "search_flights":
            args = params.get("arguments", {})
            try:
                data = search_logic(args.get("origin"), args.get("destination"), args.get("date"))
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "content": [{ "type": "text", "text": json.dumps(data, indent=2) }]
                    }
                }
            except Exception as e:
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": { "code": -32000, "message": str(e) }
                }
        else:
             return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": { "code": -32601, "message": "Method not found" }
            }

    # Default for unknown methods (ping etc)
    # MCP requires ignoring notifications, but replying error to requests
    if msg_id is not None:
         return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": { "code": -32601, "message": "Method not found or not implemented" }
        }
    return None

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            
            try:
                req = json.loads(line)
            except json.JSONDecodeError:
                continue
                
            res = handle_request(req)
            if res:
                print(json.dumps(res))
                sys.stdout.flush()
                
        except Exception as e:
            logging.critical(f"Critical Loop Error: {e}")

if __name__ == "__main__":
    main()
