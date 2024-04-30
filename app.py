from flask import Flask, render_template
import random

app = Flask("Eucalyptus")

lines = [
    "How chilly it is this evening!",
    "Brrrrrr!",
    "How cozy it is over here!",
    "Thirsty, thirsty!",
    "I'm parched! What about you!",
    "Mmmm! Nice and moist!",
    "The air is thirsty today!",
    "I do love a rainy day!",
    "Wow! The sun is smiling!",
    "I'm gonna be a snowflake when I grow up!",
    "Spring!",
    "Fall!",
    "Winter!",
    "Summer!",
    "I'm going to grow today! What about you!",
    "How beautiful the stars are tonight!",
    "I wonder what the man in the moon is saying!",
    "I miss you!",
    "How lovely the weather is today!",
]

@app.route('/', methods=['GET'])
def home():
    return render_template("eucalyptus.html",
                           name="David",
                           message=random.choice(lines),
                           moisture="💧💧💧",
                           weather="⛅")
