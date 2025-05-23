def process_cities(file_name):
    try:
        with open(file_name, 'r') as file:
            cities = file.readlines()

        all_cities = []
        total_area = 0

        for line in cities:
            city_name, population, area = line.strip().split()
            population = float(population)
            area = float(area)
            all_cities.append((city_name, population, area))
            total_area += area

            print(f"City: {city_name}, Population: {population}L, Area: {area} sq. km")

        print("\nCities with population more than 10 lakhs:")
        for city in all_cities:
            if city[1] > 10:
                print(f"{city[0]}")

        print(f"\nTotal area of all cities: {total_area} sq. km")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_cities("city.txt")
