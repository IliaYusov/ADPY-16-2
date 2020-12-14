from datetime import datetime as dt
import hashlib

def logger(file_path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            with open(file_path, 'a', encoding='utf-8') as f:
                result = old_function(*args, **kwargs)
                f.write(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")} - '
                        f'{old_function.__name__}'
                        f'{args if args else ""}'
                        f'{kwargs if kwargs else ""} -> '
                        f'{result}\n')
            return result
        return new_function
    return decorator

@logger('log.txt')
def md5_hash(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.encode())

for md5 in md5_hash('countries.txt'):
    print(md5.hexdigest())
