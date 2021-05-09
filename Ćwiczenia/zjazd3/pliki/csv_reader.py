import argparse
import csv
from collections import defaultdict

parser = argparse.ArgumentParser(description="Process file...")
parser.add_argument("-f", '--input_file', type=str)
parser.add_argument("-o", "--output_file", type=str)


args = parser.parse_args()

user_last_login = {}
user_total_time = defaultdict(int)

with open(args.input_file, "r") as fh:
    reader = csv.reader(fh, delimiter=";")
    for login, action, time in reader:
        if action == "LOGIN":
            user_last_login[login] = int(time)
        else:
            user_total_time[login] += int(time) - user_last_login[login]


if args.output_file:
    with open(args.output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        # f.write("Czas przebywania w systemie:\n")
        writer.writerows(sorted(user_total_time.items(), key=lambda x: x[1], reverse=True))
else:
    print("Czas przebywania w systemie: ")
    for line in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
        print(f"- {line[0]}: {line[1]} s")
