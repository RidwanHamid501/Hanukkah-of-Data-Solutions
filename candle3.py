import pandas as pd


def candle3(customers, contractor_phone, years, first_month):
    neighborhood = customers.loc[customers['phone']
                                 == contractor_phone, 'citystatezip'].iloc[0]

    customers['birthdate'] = pd.to_datetime(customers['birthdate'])

    filtered_customers = customers[
        (customers['birthdate'].dt.year.isin(years)) &
        (
            ((customers['birthdate'].dt.month == first_month) & (customers['birthdate'].dt.day >= 21)) |
            ((customers['birthdate'].dt.month == (first_month %
             12 + 1)) & (customers['birthdate'].dt.day <= 22))
        ) &
        (customers['citystatezip'] == neighborhood)
    ]

    return filtered_customers['phone'].tolist()


if __name__ == "__main__":
    customers = pd.read_csv('noahs-customers.csv')
    years_rabbit = [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]
    neighbor = candle3(customers, '332-274-4185', years_rabbit, 6)
    print(neighbor)
