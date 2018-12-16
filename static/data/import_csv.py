#Import CSV to Postgresql

import psycopg2
#from psycopg2 import connect, cursor
import pandas as pd

#conn=psycopg2.connect("host = localhost dbname=final user=postgres")
#conn = psycopg2.connect("host=localhost dbname=final user=postgres password=password")
conn = psycopg2.connect("host=ec2-184-72-239-186.compute-1.amazonaws.com dbname=dbsjd37pc4s73g user=oaboomcnxixcru password=ef8e4c6683a6634268058a2517a366100f5b1e7fa6004a07eb0f98e14b39f65b")
cur=conn.cursor()


#1. Deal with Users Data
users=pd.read_csv('User Data.csv',index_col=0)

for idx, u in users.iterrows():
	cur.execute('''INSERT into users (username, password, first_name, last_name, age, drug_type,
				use_duration, zipcode, state, gender, med_insurer, year_signed_up,
				years_from_first_litigation, copay_or_coinsurance,personal_spending_per_year,total_spending,income)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)''',
				(u.username, u.password, u.first_name, u.last_name, u.age, u.drug_type,
				u.use_duration, u.zipcode, u.state, u.gender, u.med_insurer, u.year_signed_up,
				u.years_from_first_litigation, u.copay_or_coinsurance,u.personal_spending_per_year, u.total_spending, u.income))

	conn.commit()



#2. Deal with Opioid consumption by state
consumption_state=pd.read_csv('consumption_state.csv',index_col=0)


for idx, u in consumption_state.iterrows():
	cur.execute('''INSERT into consumption_state (state, drug_name, year, grams)
				VALUES (%s, %s, %s, %s)''',
				(u.state, u.drug_name, u.year, u.grams))

	conn.commit()

cur.close()
conn.close()
