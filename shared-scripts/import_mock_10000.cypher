// Create customers
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:mock_data_10000_rows.csv" AS row
CREATE (:Customer {firstName: row.first_name, lastName: row.last_name, email: row.email, income: toFloat(row.income), ipAddress: row.ip_address, customerId: row.Id});

CREATE INDEX ON :Customer(customerId);
CREATE INDEX ON :Customer(lastName);

schema await

//commands to run:
// cp /shared_data/import_mock_10000.cypher /var/lib/neo4j/import
// cp /shared_data/mock_data_10000_rows.csv /var/lib/neo4j/import
//
// bin/neo4j-shell -path mock.db -file import/import_mock_10000.cypher