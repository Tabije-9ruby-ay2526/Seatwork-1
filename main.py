# Working with Lists
from pyscript import document
# Variables
country = ["France", "Germany", "Ireland", "Italy", "Netherlands", "Norway", "Spain","Switzerland"]
nickname = ["The Hexagon","The Land of Poets and Thinkers", "The Emerald Isle", "Bel Phase (The Beautiful Country)","The Land of Windmills and Tulips","The Land of the Midnight Sun", "The Land of Flamenco and Fiesta","The Land of the Alps"]
# Function
def show_name(e):
    selected_country = document.getElementById("country").value

    index = country.index(selected_country)
    selected_nickname = nickname[index]

    document.getElementById("result").innerText = selected_nickname