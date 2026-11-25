from pyscript import document, when


@when("click", "#check-button")
def candidate_checker(e):
    club_members = ["Andrey Santos", 
                    "Sage Aguinaldo", 
                    "Michael Barrameda", 
                    "Heather Son", 
                    "Cyra Cheang", 
                    "Miel Lindaya"]

    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()
    candidate = f_name + ' ' + l_name
    member_checker = candidate.casefold() in [member.casefold() for member in club_members]

    messages=( f'Sorry {candidate}, your name is not on the list.',
    f'Welcome {candidate}, thank you for joining the Social Science Club.')

    document.getElementById('result').innerText = messages[member_checker]