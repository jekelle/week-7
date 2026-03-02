import requests
import pandas as pd


def get_location_data(location):
    """
    Fetch latitude, longitude, and type for a given location
    using the Nominatim OpenStreetMap API.
    """

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

        return {
            "Location": location,
            "Latitude": float(result.get("lat", float("nan"))),
            "Longitude": float(result.get("lon", float("nan"))),
            "Type": result.get("type", float("nan")).title()
        }

    except (requests.RequestException, ValueError):
        return {
            "Location": location,
            "Latitude": float("nan"),
            "Longitude": float("nan"),
            "Type": float("nan")
        }


def load_locations(locations):
    """
    Load multiple locations into a pandas DataFrame.
    """

    results = [get_location_data(loc) for loc in locations]
    return pd.DataFrame(results)
