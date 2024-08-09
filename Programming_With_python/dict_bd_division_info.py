bd_division_info = {}

bd_division_info["Barisal"] = {"District": 6, "Upazilla": 39, "Council": 333}
bd_division_info["Chittagong"] = {"District": 11, "Upazilla": 97, "Council": 336}
bd_division_info["Dhaka"] = {"District": 13, "Upazilla": 93, "Council": 1833}
bd_division_info["Khulna"] = {"District": 10, "Upazilla": 59, "Council": 270}
bd_division_info["Mymensingh"] = {"District": 4, "Upazilla": 34, "Council": 350}
bd_division_info["Rajshahi"] = {"District": 8, "Upazilla": 70, "Council": 558}
bd_division_info["Rangpur"] = {"District": 8, "Upazilla": 58, "Council": 536}
bd_division_info["Sylhet"] = {"District": 4, "Upazilla": 38, "Council": 334}

divisions = bd_division_info.keys()
upazilla = 0
district = 0
council = 0
# print(divisions)

# for division in divisions:
#     print("Division name is: ", division)

# for division in divisions:
#     print(bd_division_info[division]["Upazilla"], "Upazilla in", division, "Division")

# for key in bd_division_info:
#     print(key)
#     print(bd_division_info[key])

# for key, value in bd_division_info.items():
#     print(key)
#     print(value)

for division in divisions:
    upazilla += bd_division_info[division]["Upazilla"]
    district += bd_division_info[division]["District"]
    council += bd_division_info[division]["Council"]

print("Total Upazilla in Bangladesh 2.0: ", upazilla)
print("Total District in Bangladesh 2.0: ", district)
print("Total Council in Bangladesh  2.0:", council)


