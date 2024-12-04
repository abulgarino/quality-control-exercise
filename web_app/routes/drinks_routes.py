from flask import Blueprint, render_template
import requests

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks/nonalcoholic")
def nonalcoholic_drinks():
    try:
        # Fetch nonalcoholic drinks from the Cocktail DB API
        response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic")
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        # Get the first 20 drinks
        drinks = data.get("drinks", [])[:20]

        return render_template("nonalcoholic_drinks.html", drinks=drinks)
    except Exception as err:
        print(f"Error fetching drinks: {err}")
        return "Error fetching nonalcoholic drinks", 500
