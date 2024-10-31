import pandas as pd


def get_top_customer_phone(customers, orders, orders_items):
    orders['shipped'] = pd.to_datetime(orders['shipped'])
    orders_4am = orders[orders['shipped'].dt.hour == 4]

    joined = orders_4am.merge(orders_items, on="orderid")
    pastries = joined[joined['sku'].str.contains("BKY", na=False)]

    pastry_counts = pastries.groupby('orderid')['qty'].sum()
    qualifying_orders = pastry_counts[pastry_counts > 1].index
    frequent_customers = orders_4am[orders_4am['orderid'].isin(
        qualifying_orders)]

    top_customer_id = frequent_customers['customerid'].value_counts().idxmax()

    phone = customers.loc[customers['customerid']
                          == top_customer_id, 'phone'].values[0]

    return phone


if __name__ == "__main__":
    customers = pd.read_csv("noahs-customers.csv")
    orders = pd.read_csv("noahs-orders.csv")
    orders_items = pd.read_csv("noahs-orders_items.csv")

    early_bird = get_top_customer_phone(customers, orders, orders_items)
    print(early_bird)
