def sort_by_key(*dicts: dict) -> list[dict]:
    output = []

    for d in dicts:
        keys = sorted(list(d.keys()))
        new_dict = {key : d[key] for key in keys}
        output.append(new_dict)

    return output

input_data = ( # The data below has been taken from the internet
    {
        "street": "street()",
        "city": "city()",
        "state": "state()",
        "country": "country()",
        "zip": "zipCode()"
    },
    {
        "message": "Hello, firstName()! Your order number is: #int(1,100)",
        "phoneNumber": "phoneNumber()",
        "phoneVariation": "+90 int(300,399) int(100,999) int(10-99) int(10,99)",
        "status": "enum(active, disabled)"
    },
    {
        "username": "this.name.first-this.name.last",
        "password": "password()",
        "emails": [
        "repeat(2)",
        "email(gmail.com, example.com)"
      ],
    }
)

print(sort_by_key(*input_data))