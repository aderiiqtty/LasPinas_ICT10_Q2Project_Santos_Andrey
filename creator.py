from pyscript import document

creator = {
    "name": "Andrey Micah Santos",
    "section": "Grade 10 - Emerald",
    "hobbies": ("Gaming", "Sleeping", "Doomscrolling Pintesrest"),
    "likes": ("money", "food", "animes or animations", "music"),
    "dislikes":("sour candy", "avocados", "peanuts (except the boiled ones)", "strawberries (except in flavored yogurt and jams)", "bugs"),
    "others": "Good listener, bad responder.",
    "quote": "Don't set yourself on fire to keep others warm.",
}

print = (
    f"<strong>Name:</strong> {creator['name']}<br>"
    f"<strong>Section:</strong> {creator['section']}<br>"
    f"<strong>Hobbies:</strong> {', '.join(creator['hobbies'])}<br>"
    f"<strong>Likes:</strong> {', '.join(creator['likes'])}<br>"
    f"<strong>Dislikes:</strong> {', '.join(creator['dislikes'])}<br>"
    f"<strong>Others:</strong> {creator['others']}<br>"
    f'<strong>Quote:</strong> "{creator["quote"]}"'
)

document.getElementById("creator-output").innerHTML = print