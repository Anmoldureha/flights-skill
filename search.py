import sys
import json
from fast_flights import FlightData, Passengers, get_flights

def main():
    try:
        if len(sys.argv) < 4:
            print(json.dumps({"error": "Usage: search.py ORIGIN DEST DATE (YYYY-MM-DD)"}))
            return

        origin = sys.argv[1]
        dest = sys.argv[2]
        date = sys.argv[3]
        
        # Default fetch_mode="fallback" might need Playwright?
        # The README says "fallback support for Playwright".
        # If standard request fails, it tries fallback.
        
        result = get_flights(
            flight_data=[FlightData(date=date, from_airport=origin, to_airport=dest)],
            trip="one-way",
            seat="economy",
            passengers=Passengers(adults=1, children=0, infants_in_seat=0, infants_on_lap=0),
            # fetch_mode="fallback" 
        )
        
        output = {
            "current_price": result.current_price,
            "flights": []
        }
        
        for f in result.flights:
            output["flights"].append({
                "name": f.name,
                "price": f.price,
                "duration": f.duration,
                "departure": f.departure,
                "arrival": f.arrival,
                "stops": f.stops
            })
            
        print(json.dumps(output, indent=2))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
