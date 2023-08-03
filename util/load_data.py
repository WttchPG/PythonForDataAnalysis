import json

usaGovPath = "data/usagov.txt"

with open(usaGovPath) as file:
    usaGovRecords = [json.loads(line) for line in file.readlines()]
