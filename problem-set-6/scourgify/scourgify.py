import sys
import csv


def main():
    students = []

    if valid_input(sys.argv):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        try:
            students = read_csv(input_file, students)
        except FileNotFoundError:
            sys.exit("Could not read invalid_file.csv")
        cleaned_students = split_name(students)
        write_csv(output_file, cleaned_students)


def read_csv(csv_file, list):
    with open(csv_file, "r", encoding="utf8") as before:
        reader = csv.DictReader(before)
        for row in reader:
            list.append({"name": row["name"], "house": row["house"]})
    return list


def valid_input(file):
    if len(file) < 3:
        sys.exit("Too few command-line arguments")
    elif len(file) > 3:
        sys.exit("Too many command-line arguments")
    elif not file[1].endswith(".csv"):
        sys.exit("Input file not a CSV")
    elif not file[2].endswith(".csv"):
        sys.exit("Output file not a CSV")
    else:
        return True


def split_name(students):
    students_fixed = []
    for student in students:
        last, first = student["name"].split(", ")
        students_fixed.append({"first": first, "last": last, "house": student["house"]})
    return students_fixed


def write_csv(csv_file, list):
    with open(csv_file, "w", encoding="utf8") as after:
        writer = csv.DictWriter(after, fieldnames=list[1])
        writer.writeheader()
        for row in list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
