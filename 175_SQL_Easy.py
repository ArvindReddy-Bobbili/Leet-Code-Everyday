import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
#     # Write your MySQL query statement below
# SELECT firstName, LastName, city, state
# From Person
# Left Join Address ON
# Person.personId = Address.personId

    result = pd.merge(person, address, on='personId', how = 'left')
    result= result[['firstName', 'lastName', 'city', 'state']]
    return result

