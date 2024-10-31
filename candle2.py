import pandas as pd


def candle2(customers, orders, orders_items, products, first_initial_regex, second_initial_regex):
    customers[['first', 'last']] = customers['name'].str.split(
        ' ', n=1, expand=True)

    filtered_customers = customers[
        customers['first'].str.contains(first_initial_regex, regex=True) &
        customers['last'].str.contains(second_initial_regex, regex=True)
    ]

    merged_data = filtered_customers.merge(orders, on='customerid')

    merged_data = merged_data[merged_data['ordered'].str.contains('2017')]

    merged_data = merged_data.merge(orders_items, on='orderid')
    merged_data = merged_data.merge(products, on='sku')

    grouped_data = merged_data.groupby(['phone', 'orderid']).filter(
        lambda x: x['desc'].str.contains('Coffee').any(
        ) and x['desc'].str.contains('Bagel').any()
    )

    contractor = grouped_data['phone'].drop_duplicates()

    return contractor


if __name__ == "__main__":
    customers = pd.read_csv('noahs-customers.csv')
    orders = pd.read_csv('noahs-orders.csv')
    orders_items = pd.read_csv('noahs-orders_items.csv')
    products = pd.read_csv('noahs-products.csv')
    contractor = candle2(customers, orders, orders_items, products, "^J", "^P")
    print(contractor)
