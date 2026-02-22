# pip install pandas
import pandas as pd

# Load the Excel file (replace with your filename)
file_path = "Sql-test.xlsx"
df = pd.read_excel(file_path)

selectQuery = "select * from applications where"

# Loop through rows and build SQL queries
for _, row in df.iterrows():
    firstname = row["First Name"]
    lastname = row["Last Name"]
    role = row["Role"]
    town = row["Town"]
    postcode = row["Postcode"]
    mobile = row["Mobile"]
    email = row["Email"]

    dbsdate = row["Interview Date"]
    id_val = ["Role"]


    # Format dbsdate for SQL (assuming it's a datetime in Excel)
    if pd.notnull(dbsdate):
        dbsdate_str = pd.to_datetime(dbsdate).strftime("%Y-%m-%d")
    else:
        dbsdate_str = None

    query = f"""
    UPDATE your_table
    SET dbsdate = {'NULL' if dbsdate_str is None else f"'{dbsdate_str}'"},
        email = {'NULL' if pd.isnull(email) else f"'{email}'"}
    WHERE id = {id_val};
    """

    selectQuery += '(firstname = "'+firstname+'" and lastname = "'+lastname+'" and emailaddress="'+email+'" and postcode="'+str(postcode)+'") or \n'
    
    # print(query.strip())

selectQuery += "\n order by lastname, firstname"
print(selectQuery)
