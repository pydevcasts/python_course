
import time
from concurrent.futures import ProcessPoolExecutor

def show(name):
    print(f"Starting {name}....")
    time.sleep(3)
    print(f"Ending {name}....")

def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        nums = ["one", "two", "three", "four"]
        executor.map(show, nums)
main()
