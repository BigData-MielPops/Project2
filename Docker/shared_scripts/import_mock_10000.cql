CREATE KEYSPACE mock_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

CREATE TABLE mock_keyspace.customers ( first_name text, last_name text, email text, income int, ip_address text, id int PRIMARY KEY,);
COPY mock_keyspace.customers ( first_name, last_name, email, income, ip_address, Id) FROM  '/shared_data/mock_data_10000_rows.csv' WITH HEADER = 'true';