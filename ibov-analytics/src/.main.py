import sys
import os

sys.path.append(os.path.abspath("src"))

from data_collector import get_ibov_data

if _name_ == "_main_":
    # Código principal
    from data_collector import get_ibov_data

    def main():
        data = get_ibov_data("2023-01-01", "2024-01-01")
        print(data.head())

    main()
