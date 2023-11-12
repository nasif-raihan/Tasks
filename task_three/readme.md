# Coordinate Finder App

This Django app provides a simple interface to obtain geolocation coordinates (latitude and longitude) based on a given address. It utilizes the Google Maps Geocoding API for this purpose.

## Features

- **Get Coordinates:** Allows users to input an address and retrieve its geolocation coordinates.

## Code Structure

- **`coordinate_finder` Directory:** Contains the Django app code.
  - `models.py`: No models are defined in this app.
  - `views.py`: Defines the view to handle the coordinate retrieval logic.
  - `templates/task_three/coordinate_finder.html`: HTML template for the coordinate finder page.

- **`environs` and `googlemaps` Libraries:** Used for handling environment variables and interacting with the Google Maps API, respectively.

## Important Notes

- The Google Maps API key is stored in the `.env` file. Ensure you keep this file secure and do not share it publicly.

- Make sure to follow the Google Maps API usage policies and guidelines.

- This app does not include user authentication or authorization. Adjustments may be necessary based on specific use cases and security requirements.