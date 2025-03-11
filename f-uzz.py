##############################
# Fuzzing bot by laggerghost #
##############################

import requests
from requests.exceptions import RequestException
import os

def read_fuzz_file(file_path):
    with open(file_path, 'r') as file:
        fuzz_list = file.read().splitlines()
    return fuzz_list

def read_url_file(file_path):
    with open(file_path, 'r') as file:
        url_list = file.read().splitlines()
    return url_list

def fuzz_url(url, fuzz_list):
    results = []
    for fuzz in fuzz_list:
        full_url = f"https://{url}/{fuzz}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                results.append(full_url)
        except RequestException as e:
            print(f"Error accessing {full_url}: {e}")
    return results

def write_results(results, file_path):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{result}\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Foezz!ng b-o-t by Laggerghost")

    fuzz_list = read_fuzz_file('fuzz.txt')

    url_list = read_url_file('list.txt')

    all_results = []

    for url in url_list:
        print(f"Fuzzing URL: https://{url}")
        results = fuzz_url(url, fuzz_list)
        all_results.extend(results)

    write_results(all_results, 'results.txt')
    print("Fuzzing completed. Results saved to results.txt")

if __name__ == "__main__":
    main()
