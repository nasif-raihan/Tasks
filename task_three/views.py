from django.shortcuts import render, redirect

from task_three.coordinate_finder import GetCoordinates


def home(request):
    return render(request, "base.html", context={"title": "Home"})


def get_coordinates(request):
    if request.method == "POST":
        address = request.POST["address"]
        coordinates_finder = GetCoordinates.get_instance()
        coordinates = coordinates_finder.get_geolocation(address)

        return render(
            request,
            "task_three/coordinate_finder.html",
            context={"title": "Coordinate", "coordinates": coordinates},
        )
    return render(
        request,
        "task_three/coordinate_finder.html",
        context={"title": "Coordinate"},
    )
