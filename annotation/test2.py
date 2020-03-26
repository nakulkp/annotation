cur.execute("""SELECT countries, country_id
    FROM region
    WHERE status = 'enabled';""")
row = cur.fetchall()
countries = row[0]
country_id = row[1]

cur.execute("""SELECT commodities, commodity_id
    FROM commodity_table
    WHERE status = 'enabled';""")
row = cur.fetchall()
commodities = row[0]
commodity_id = row[1]

cur.execute("""SELECT categories, category_id
        FROM category_table
    WHERE status = 'enabled';""")
row = cur.fetchall()
categories = row[0]
category_id = row[1]

cur.execute("""SELECT sub_categories, subcategory_id
        FROM subcategory_table
    WHERE status = 'enabled';""")
sub_categories = cur.fetchall()
sub_categories = sub_categories[0]
subcategory_id = countries[1]

cur.execute("""SELECT moving_factors, moving_factor_id
        FROM moving_factor_table
    WHERE status = 'enabled';""")
moving_factors = cur.fetchall()
moving_factors = moving_factors[0]
moving_factor_id = countries[1]

cur.execute("""SELECT factor_value, factor_value_id
        FROM factor_value_table
    WHERE status = 'enabled';""")
factor_value = cur.fetchall()
factor_value = factor_value[0]
factor_value_id = countries[1]

cur.execute("""SELECT price_value, price_value_id
        FROM price
    WHERE status = 'enabled';""")
price_value = cur.fetchall()
price_value = price_value[0]
price_value_id = countries[1]

cur.execute("""SELECT supply_value, supply_value_id
        FROM supply
    WHERE status = 'enabled';""")
supply_value = cur.fetchall()
supply_value = supply_value[0]
supply_value_id = countries[1]

cur.execute("""SELECT demand_value, demand_value_id
        FROM demand
    WHERE status = 'enabled';""")
demand_value = cur.fetchall()
demand_value = demand_value[0]
demand_value_id = countries[1]

cur.execute("""SELECT sc_disruption_value, sc_disruption_value_id
        FROM sc_disruption
    WHERE status = 'enabled';""")
sc_disruption_value = cur.fetchall()
sc_disruption_value = sc_disruption_value[0]
sc_disruption_value_id = countries[1]
