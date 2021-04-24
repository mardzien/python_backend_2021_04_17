

x, y = 95, 95

if x < 0 or x > 100 or y < 0 or y > 100:
    print("Jesteś poza planszą")
elif x <= 10:
    if y <= 10:
        print("Jesteś w lewym dolnym rogu.")
    elif y < 90:
        print("Jesteś na lewej krawędzi.")
    else:
        print("Jesteś w lewym górnym rogu")
elif x <= 90:
    if y <= 10:
        print("Jesteś na dolnej krawędzi.")
    elif y >= 90:
        print("Jesteś na górnej krawędzi.")
    else:
        print("Jesteś w centrum")
else:
    if y <= 10:
        print("Jesteś w prawym dolnym rogu.")
    elif y >= 90:
        print("Jesteś w prawym górnym rogu.")
    else:
        print("Jesteś na prawej krawędzi.")
