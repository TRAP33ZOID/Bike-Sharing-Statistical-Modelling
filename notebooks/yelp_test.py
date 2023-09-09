import requests
import pandas as pd


headers = {
    "accept": "application/json",
    "Authorization": "BEARER V7TEYxJucMlFzJhcFDQhxNuYvJSVIPB4eBHKxyEg3scY0hpZkXP1Lga4JmgHjKj_Fb9RDz2COSocuoxK3jmMU3qxjpqgbdC12itZKTAp-dFDBx3uTkkVpTej-anvZHYx"
}


def fetch_yelp_data(lat, lon):
    url = f"https://api.yelp.com/v3/businesses/search?latitude={lat}&longitude={lon}&term=food&radius=1000&sort_by=review_count&limit=5"
    response = requests.get(url, headers=headers)
    
    businesses = response.json().get("businesses", [])
    
    extracted_data = []
    for business in businesses:
        name = business["name"]
        review_count = business["review_count"]
        categories = ', '.join([category["title"] for category in business["categories"]])
        rating = business["rating"]
        display_address = ', '.join(business["location"]["display_address"])
        display_phone = business["display_phone"]
        distance = business["distance"]

        extracted_data.append([lat, lon, name, review_count, categories, rating, display_address, display_phone, distance])
    
    return extracted_data


file_path = r"C:\Users\wamm1\Desktop\py project\py-project\notebooks\5_rows_df_bikes.csv"

df_yelp = pd.read_csv(file_path)


all_data = []
for _, row in df_yelp.iterrows():
    all_data.extend(fetch_yelp_data(row["latitude"], row["longitude"]))


df_all_yelp = pd.DataFrame(all_data, columns=["bike_latitude", "bike_longitude", "name", "is_closed", "review_count", "categories", "rating", "display_address", "display_phone", "distance"])


df_all_yelp.to_csv('df_all_yelp.csv', index=False)

