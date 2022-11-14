from search import search
import csv

with open('input.csv', newline="") as inputfile:
    reader = csv.DictReader(inputfile)
    with open('output.csv', 'w', newline='') as outputfile:
        fieldnames = ["Web domain", "Mail"]
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            emails = search(row["Web domain"])
            if (emails):
                writer.writerow({"Web domain": row["Web domain"], "Mail": emails})
            else:
                writer.writerow({"Web domain": row["Web domain"], "Mail": "Aucun mail"})