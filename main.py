from pyscript import display, document


def submit_name(event):
    name = document.getElementById("name-input").value.strip()
    document.getElementById("name-output").innerHTML = ""

    if not name:
        display("Please enter your name.", target="name-output")
        return

    display(
        f"Welcome {name}! You may now continue exploring our page!",
        target="name-output",
    )