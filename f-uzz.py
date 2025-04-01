import requests
from requests.exceptions import RequestException
import os
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def fuzz_url(session, url, fuzz_list):
    results = []
    for fuzz in fuzz_list:
        full_url = f"https://{url}/{fuzz}"
        try:
            response = session.get(full_url, timeout=5)  # Timeout 5 detik
            print(f"{Fore.GREEN}[{response.status_code}] {full_url}")  # Tampilkan status dengan warna hijau
            if response.status_code == 200:
                results.append(full_url)
        except requests.ConnectionError:
            print(f"{Fore.RED}[ERROR] Connection refused: {full_url}")  # Error warna merah
        except requests.Timeout:
            print(f"{Fore.YELLOW}[ERROR] Timeout: {full_url}")  # Timeout warna kuning
        except RequestException:
            print(f"{Fore.RED}[ERROR] Failed to access: {full_url}")  # Umum error warna merah
    return results

def write_results(results, file_path):
    with open(file_path, 'w') as file:
        file.write("\n".join(results))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{Fore.CYAN}Foezz!ng b-o-t by Laggerghost")  # Warna cyan untuk header

    try:
        fuzz_list = read_file('fuzz.txt')
        url_list = read_file('list.txt')

        all_results = []
        with requests.Session() as session:  # Gunakan session untuk optimasi
            for url in url_list:
                print(f"\n{Fore.CYAN}Fuzzing: https://{url}")  # Warna cyan untuk URL
                results = fuzz_url(session, url, fuzz_list)
                all_results.extend(results)

        write_results(all_results, 'results.txt')
        print(f"\n{Fore.GREEN}Fuzzing completed. Results saved to results.txt")  # Warna hijau untuk selesai

    except KeyboardInterrupt:
        print(f"\n{Fore.MAGENTA}[!] Fuzzing aborted by user. Exiting gracefully.")  # Warna magenta untuk abort

if __name__ == "__main__":
    main()
