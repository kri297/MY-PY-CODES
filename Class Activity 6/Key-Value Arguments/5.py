def calculate_average(*dicts: dict[str, int]) -> float:
    if dicts:
        sum = 0

        for d in dicts:
            sum += d.get("score", 0)

        return sum / len(dicts)
    else:
        return 0
    
input_data = (
    {
        "score" : 10
    }, 
    {
        "score" : 20
    },
    {
        "score" : 30
    },
    {
        "score" : 40
    },
    {
        "score" : 50
    },
)

print(calculate_average(*input_data))