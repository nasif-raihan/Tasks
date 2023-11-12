import googlemaps
from environs import Env


class GetCoordinates:
    instance = None

    def __init__(self):
        if GetCoordinates.instance is not None:
            raise RuntimeError(
                "An instance of GetCoordinates class already exists.Did you forget to call get_instance method?"
            )
        GetCoordinates.instance = self

    def __get_api_key(self) -> str:
        env = Env()
        env.read_env()
        if env.str("API_KEY") is None:
            raise RuntimeError("No API KEY in the env file.")
        self.__api_key = env.str("API_KEY")
        return self.__api_key

    @staticmethod
    def get_instance() -> "GetCoordinates":
        if GetCoordinates.instance is None:
            GetCoordinates.instance = GetCoordinates()
        return GetCoordinates.instance

    def get_geolocation(self, address):
        gmaps = googlemaps.Client(key=self.__get_api_key())

        try:
            geocode_result = gmaps.geocode(address)

            location = geocode_result[0]["geometry"]["location"]
            latitude = location["lat"]
            longitude = location["lng"]

            return {"address": address, "latitude": latitude, "longitude": longitude}

        except Exception as e:
            raise ValueError("Location does not exist in the map!")


def main():
    address = "Dhaka"

    coordinates_finder = GetCoordinates.get_instance()
    coordinates = coordinates_finder.get_geolocation(address)

    if coordinates:
        print(f"Geolocation for '{address}': {coordinates}")
    else:
        print("Failed to retrieve geolocation.")


if __name__ == "__main__":
    main()
