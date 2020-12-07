import hashlib


def md5_hash(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.encode())

for md5 in md5_hash('countries.txt'):
    print(md5.hexdigest())
