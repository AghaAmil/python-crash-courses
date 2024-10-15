import csv

# Read CSV Files with Python
with open('files/people.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# blank line
print()

with open('files/1-sample.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# blank line
print()

with open('files/people.csv', 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        print(row)

# blank line
print()

# Write to CSV Files with Python
with open('files/protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

# blank line
print()

# Writing Dictionaries to CSV Files
with open('files/players.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})

# blank line
print()

with open('files/players.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
