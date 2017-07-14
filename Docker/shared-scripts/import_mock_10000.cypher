// Create customers
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///mock_data_10000_neo.csv" AS row
CREATE (:Customer {firstName: row.first_name, lastName: row.last_name, email: row.email, income: toFloat(row.income), ipAddress: row.ip_address, customerId: row.Id});

CREATE INDEX ON :Customer(customerId);
CREATE INDEX ON :Customer(lastName);

schema await