def combine_dicts(*dicts: dict[str, str]) -> dict[str, str]:
    output = {}
    for d in dicts:
        output.update(d)

    return output

dict1 = { "Name" : "Sauhard" }
dict2 = { "Age" : "19" }
dict3 = { "University" : "Sauhard" }

print(combine_dicts(dict1, dict2, dict3))