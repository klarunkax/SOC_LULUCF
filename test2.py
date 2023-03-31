##LIST ALL THE FILES IN THIS FOLDER AND ITS SUBFOLDERS
# import os
#
# # set the directory path
# dir_path = r"C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data"
#
# # define a function to recursively list all files
# def list_files(dir_path):
#     for root, dirs, files in os.walk(dir_path):
#         for file in files:
#             # print only the filename without the path
#             print(os.path.basename(os.path.join(root, file)))
#
# # call the function
# list_files(dir_path)


# ##LIST ALL THE COUNTRIES NAMES INCLUDED
# import pandas as pd
#
# # Read the CSV file into a DataFrame
# df = pd.read_csv(r"C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data\data_R10_R11.csv")
#
# # Get all the column names excluding last five characters
# col_names = [col[:-5] for col in df.columns]
#
# # Remove any duplicates
# col_names = list(set(col_names))
#
# # Sort the final list of column names alphabetically
# col_names_sorted = sorted(col_names)
#
# # Print the final sorted list of column names
# print(col_names_sorted)

import csv

# Open the CSV file for reading
with open(r'C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data\data_R10_R11.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Get the header row
    header = next(reader)

    # Iterate over each column
    for column_index in range(len(header)):

        # Get the column name
        column_name = header[column_index]

        # Assume all fields contain numbers initially
        all_numbers = True

        # Iterate over each row in the column (starting from the second row)
        for row in reader:

            # Check if the row is blank
            if all(field == '' for field in row):
                continue  # Skip blank rows

            # Check if the field is a number
            if not row[column_index].replace('.', '').replace('-', '').isnumeric():
                all_numbers = False
                break

        # Print the column name along with YES or NO depending on whether all fields contain numbers
        print(column_name, "YES" if all_numbers else "NO")

        # Reset the file pointer to the beginning of the file for the next column
        file.seek(0)

        # Skip the header row for the next column
        next(reader)
