import sys
from data import collect_data

if __name__ == "__main__":
    apoint = sys.argv[1]
    duration = int(sys.argv[2])
    print("started collecting data")
    collect_data(apoint, duration)
    print("finished collecting data")
