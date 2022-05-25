user_rating = input("What rating do you want to see? ")

smallest_year = 99999999

with open("movies.csv") as movies_file:
    header_line = next(movies_file)
    #Another option:
    #header_line = movies_file.readline()

    for line in movies_file:
        # Get rid of any extra whitespace at the beginning or end
        line = line.strip()

        # Split it into parts
        values = line.split(",")

        title = values[0]
        year = int(values[1])
        runtime = float(values[2])
        rating = values[3]

        if year < smallest_year:
            # This is the new "smallest" year, so save it as such
            smallest_year = year

        #rating_num = 0
        # if rating == "G":
        #     rating_num = 1
        # elif rating == "PG":
        #     rating_num = 2

        if rating.upper() == user_rating.upper():
            print(f"{title} ({year}) - Rated {rating}")
    
print(f"The earliest movie in your list was in the year {smallest_year}")