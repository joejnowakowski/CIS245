import random


def main():
    collection = random_numbers()
    max_num = get_max(collection)
    min_num = get_min(collection)
    avg = avg_from_list(collection)
    print(f"""
            Collection of numbers: {collection}
            Max: {max_num}
            Min: {min_num}
            Average: {avg}
        """)

def random_numbers():
    return [random.randrange(1,1000) for _ in range(20)]

def get_max(random_list):
    return max(random_list)

def get_min(random_list):
    return min(random_list)

def avg_from_list(random_list):
    return sum(random_list) / len(random_list)

if __name__ == "__main__":
    main()