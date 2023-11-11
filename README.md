# Bike-Sharing-Statistical-Modelling 

## Project/Goals
(The aim of this project is to explore and analyze the relationship between bike availability in specific locations and the presence and characteristics of Points of Interest (POIs) in those areas, using the CityBikes, Yelp, and Foursquare APIs.)

## Process
### Connecting to CityBikes API:

    Explored the CityBikes API to understand its structure and data format.
    Selected Toronto as the city of interest and extracted data for all bike stations, including their latitude, longitude, and available bikes.
    Parsed the JSON object and saved the results in a Pandas dataframe. 
### Connecting to Foursquare and Yelp APIs:

    Established a connection with the Foursquare API and used it to gather data on restaurants, bars, and other points of interest in proximity to the bike stations.
    Made a similar connection with the Yelp API to gather analogous data.
    Created separate DataFrames for the Yelp and Foursquare results and compared the quality of data each API provided in terms of coverage and details.
### Joining Data:

    Merged the CityBikes data with the Yelp and Foursquare datasets to create a comprehensive dataframe capturing both bike availability and points of interest.
    Employed data visualization techniques to explore patterns and correlations in the data.
    Constructed an SQLite database to securely store the collated data, ensuring it was properly structured and validated
### Building a Regression Model:

    Utilized the statsmodels module to build a regression model that examined the relationship between bike availability at a location and the characteristics of nearby points of interest.


Interpretation:

    foursquare_pois_count and yelp_pois_count: For each additional POI from either Foursquare or Yelp, we expect an increase of approximately 2.3871 bikes on average, holding all other variables constant. However, the high p-values (0.776) suggest these variables are not statistically significant predictors of free_bikes.

    avg_rating: For each unit increase in the average rating, the number of free bikes decreases by around 4, holding all other variables constant. This is a bit counterintuitive, but the high p-value (0.856) indicates that this variable is not a statistically significant predictor.

    The model's R-squared value is extremely low, indicating that our model doesn't explain much of the variance in the number of free bikes.


## Results
(Yelp API was better than fourquare. it included alot more details)
 *Foursquare provides multiple geocodes (drop_off, main, roof), which could be useful for different use cases. It also provides an icon URL for the category
    *Yelp provides a direct URL to the business's Yelp page, an image URL for the business, a review count, and a rating. 
    *when it comes to the address, foursqure dives a bit deeper and gives information such as: country, locaility, postal code and region
    *Yelp provides a phone number for the business.
    *Yelp also provides the total business found in the area even though the returned api call was limited to 5. foursqare doesnt tell us how many businesses there are on top of the requested 5

## Challenges 
    *limited api requests
    *was only able to look up infromation for a single lat and long at a time
    *when printing the dataframes it would take upwards of 2 minutes in visual studio

## Future Goals
incorperate another api to find the density of people in those areas to avoid jams
