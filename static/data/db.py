
#Import csv to postgresql db

import psycopg2
import pandas as pd

#conn = psycopg2.connect("host=localhost dbname=final user=postgres")
conn = psycopg2.connect("host=localhost dbname=final user=postgres password=password")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")

cur.execute('''CREATE TABLE users (
    uid SERIAL PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    state TEXT NOT NULL,
    zipcode TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    drug_type TEXT NOT NULL,
    use_duration FLOAT NOT NULL,
    med_insurer TEXT NOT NULL,
    year_signed_up INTEGER NOT NULL,
    years_from_first_litigation FLOAT NOT NULL,
    copay_or_coinsurance FLOAT NOT NULL,
    personal_spending_per_year FLOAT NOT NULL,
    total_spending FLOAT NOT NULL,
    income FLOAT NOT NULL)''')

conn.commit()

df_users = pd.read_csv('opoid_data.csv', index_col=0)
for idx, u in df_users.iterrows():
    cur.execute('''INSERT INTO users (username, password, first_name, last_name, state,zipcode, age,gender, drug_type, use_duration, med_insurer, year_signed_up, years_from_first_litigation, copay_or_coinsurance,personal_spending_per_year, total_spending,income) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (u.username, u.password, u.first_name, u.last_name, u.state,u.zipcode, u.age, u.gender,u.drug_type, u.use_duration, u.med_insurer, u.year_signed_up, u.years_from_first_litigation, u.personal_spending_per_year,u.copay_or_coinsurance,
    u.total_spending, u.income))
    #cur.execute('''INSERT INTO users (username, first_name, last_name, address, city,state, zipcode,insurancetype, age) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', (u.username, u.first_name, u.last_name, u.address, u.city, u.zipcode, u.insurancetype, u.age))
    conn.commit()

cur.close()
conn.close()
