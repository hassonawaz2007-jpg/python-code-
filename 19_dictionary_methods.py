marks= {
    "hassan":  98,
    "musab":   100,
    "hussain": 45,
    0:"hassan"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"musab": 90, "mahrukh":23})
# print(marks)

print(marks.get("hassan")) #prints none if it is not in it
print(marks["hassan"]) # returns an error


