import pandas as pd


def name_to_phone_number(name):
    keypad_mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    return ''.join(keypad_mapping[char] for char in name.upper() if char in keypad_mapping)


def names_and_phone(path):
    df = pd.read_csv(path)[["name", "phone"]]
    df["last_name_phone"] = df["name"].str.split(
    ).str[-1].apply(name_to_phone_number)
    df["phone"] = df["phone"].str.replace('-', '')
    return df[df["last_name_phone"] == df["phone"]][["name", "phone"]]


if __name__ == "__main__":
    path = 'noahs-customers.csv'
    matched_names = names_and_phone(path)
    print(matched_names)
