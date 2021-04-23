import csv

with open('MOCK_DATA.csv', 'r+') as f:
    mock_data_reader = csv.reader(f)

    line_count = 1
    users = []
    for row in mock_data_reader:
        if line_count > 1:
            name = row[1]
            surname = row[2]
            email = row[3]
            users.append({'name': row[1], 'surname': row[2], 'email': row[3]})
        line_count += 1

for user in users:
    print(user)

