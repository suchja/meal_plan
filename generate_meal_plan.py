import random
import json

meals = [
    "Kartoffelpüree mit Erbsen, Mören und Ei", "Risi Bisi", "Tacos", "Shakshuka", "Nudeln mit Soße",
    "Pizza", "Erbsensuppe", "Burger", "Bulgurauflauf", "Linsensuppe", "Tomatenreis", "Curry mit Reis/Couscous",
    "Bretonische Bohnensuppe", "Oliven-Feta-Knödel", "Mie-Nudeln mit Gemüse", "Kartoffelsalat", "Gurkensuppe",
    "Gazpacho", "Bärlauch/Basilikum Klöße mit Tomatensoße", "Haloumni Omelett", "Ofengemüse", "Kartoffelgratin",
    "Pellkartoffeln mit Quark"
]



week_plan = random.sample(meals, 7)

with open("meal_plan.json", "w") as f:
    json.dump(week_plan, f)
