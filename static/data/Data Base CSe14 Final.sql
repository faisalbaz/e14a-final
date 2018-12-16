
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	uid SERIAL NOT NULL PRIMARY KEY,
    username text not null,
    password text not null,
    first_name TEXT NULL,
    last_name TEXT NULL,
    age integer null,
    drug_type text null,
    use_duration decimal null,
    zipcode text null,
    state text null,
    gender text null,
    med_insurer text null,
    year_signed_up integer null,
    years_from_first_litigation decimal null,
    copay_or_coinsurance text null,
    personal_spending_per_year decimal null,
    total_spending decimal null,
    income decimal null,
    est_settle decimal null
);

DROP TABLE IF EXISTS consumption_state;
CREATE TABLE consumption_state(
    tid serial NOT NULL PRIMARY KEY,
    state text NOT NULL,
    drug_name text NOT NULL,
    year integer not null,
    grams bigint not null
);
