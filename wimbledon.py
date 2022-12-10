"""
Wimbledon
Estimate: 30 minutes
Actual:   1 hour 10 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print corresponding details"""
    records = get_records(FILENAME)
    champion_count, countries = process_records(records)
    display_results(champion_count, countries)


def process_records(records):
    """Create dictionary of champions and set of countries from records """
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_count[record[INDEX_CHAMPION]] = 1
    return champion_count, countries


def display_results(champion_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """Get records from file in list of lists form """
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
