from pyscript import document, display

nonmetals = {
    "H": ("Hydrogen", 1, "1.008"),
    "He": ("Helium", 2, "4.0026"),
    "C": ("Carbon", 6, "12.011"),
    "N": ("Nitrogen", 7, "14.007"),
    "O": ("Oxygen", 8, "15.999"),
    "F": ("Fluorine", 9, "18.998"),
    "Ne": ("Neon", 10, "20.180"),
    "P": ("Phosphorus", 15, "30.974"),
    "S": ("Sulfur", 16, "32.06"),
    "Cl": ("Chlorine", 17, "35.45"),
    "Ar": ("Argon", 18, "39.948"),
    "Se": ("Selenium", 34, "78.971"),
    "Br": ("Bromine", 35, "79.904"),
    "Kr": ("Krypton", 36, "83.798"),
    "I": ("Iodine", 53, "126.904"),
    "Xe": ("Xenon", 54, "131.293"),
    "Rn": ("Radon", 86, "222"),
}


def check_element(e):
    symbol = document.getElementById("element").value.strip().capitalize()
    document.getElementById("result").innerHTML = ""

    if symbol == "":
        display("Please enter a nonmetal symbol first.", target="result")
    elif symbol in nonmetals:
        name, atomic_num, atomic_mass = nonmetals[symbol]
        display(f"Symbol: {symbol}", target="result")
        display(f"Name: {name}", target="result")
        display(f"Atomic Number: {atomic_num}", target="result")
        display(f"Atomic Mass: {atomic_mass}", target="result")
    else:
        display("Element not found. Please enter a valid nonmetal symbol.", target="result")