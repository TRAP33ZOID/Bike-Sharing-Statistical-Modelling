import requests
import pandas as pd


headers = {
    "accept": "application/json",
    "Authorization": "fsq3Uh9GolfQTsdUjjRznbyvaZ+FU4j9jHDZ3i188g2g0aw="
}


def fetch_foursquare_data(lat, lon):
    url = f"https://api.foursquare.com/v3/places/search?query=%20&ll={lat}%2C{lon}&radius=1000&categories=13000&sort=RELEVANCE&limit=5"
    response = requests.get(url, headers=headers)
    
    results = response.json().get("results", [])
    
    extracted_data = []
    for result in results:
        name = result["name"]
        distance = result["distance"]
        formatted_address = result["location"]["formatted_address"]
        restaurant_lat = result["geocodes"]["main"]["latitude"]
        restaurant_lon = result["geocodes"]["main"]["longitude"]
        
        extracted_data.append([lat, lon, name, distance, formatted_address, restaurant_lat, restaurant_lon])
    
    return extracted_data


file_path = r"C:\Users\wamm1\Desktop\py project\py-project\notebooks\sample_bikes.csv"
df_bikes = pd.read_csv(file_path)

all_foursquare_data = []
for _, row in df_bikes.iterrows():
    all_foursquare_data.extend(fetch_foursquare_data(row["latitude"], row["longitude"]))

df_all_foursquare = pd.DataFrame(all_foursquare_data, columns=["bike_latitude", "bike_longitude", "name", "distance", "formatted_address", "restaurant_latitude", "restaurant_longitude"])


print(df_all_foursquare)
df_all_foursquare.to_csv('df_all_foursquare.csv', index=False)
