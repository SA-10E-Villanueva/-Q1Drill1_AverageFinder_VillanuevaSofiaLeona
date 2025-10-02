from pyscript import document

def get_average(event):
    # Get the input values and convert to float
    Q1 = float(document.getElementById("Q1").value)
    Q2 = float(document.getElementById("Q2").value)

    # Compute average
    average = (Q1 + Q2) / 2

    # Determine pass/fail
    if average<=85:
        result = "You need to lock in NOW."
    else:
        result = "You still need to lock in but I guess you're sort of fine...🥀"

    # Display results
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result

