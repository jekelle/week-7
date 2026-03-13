import requests
import pandas as pd


def get_location_data(location):
   

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data:
            return {
                "Location": location,
                "Latitude": float("nan"),
                "Longitude": float("nan"),
                "Type": float("nan")
            }

        result = data[0]

        location_type = result.get("type")
        if location_type:
            location_type = location_type.title()
        else:
            location_type = float("nan")

        return {
            "Location": location,
            "Latitude": float(result.get("lat", float("nan"))),
            "Longitude": float(result.get("lon", float("nan"))),
            "Type": location_type
        }

    except (requests.RequestException, ValueError, AttributeError):
        return {
            "Location": location,
            "Latitude": float("nan"),
            "Longitude": float("nan"),
            "Type": float("nan")
        }


def load_locations(locations):
   

    results = [get_location_data(loc) for loc in locations]
    return pd.DataFrame(results)
