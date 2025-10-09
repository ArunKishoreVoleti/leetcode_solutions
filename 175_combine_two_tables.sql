/*
Person Table (personId, firstName, lastName)
Address Table (addressId, personId, city, state)

We want to combine the two tables to get a list of all people with their corresponding city and state.
If a person does not have an address, we still want to include them in the result with NULL values for city and state.
We should use a LEFT JOIN to ensure all records from the Person table are included.
*/

SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;
