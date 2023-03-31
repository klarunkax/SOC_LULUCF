import os
import zipfile
import openpyxl
import pandas as pd
#
# Replace the path below with the path to your folder
folder_path = r"C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data"

# Loop through all the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a ZIP file
    if file_name.endswith(".zip"):
        # Get the name of the ZIP file without the extension
        name_without_extension = os.path.splitext(file_name)[0]
        # Create a folder with the same name as the ZIP file
        folder_path_new = os.path.join(folder_path, name_without_extension)
        os.makedirs(folder_path_new, exist_ok=True)
        # Extract the contents of the ZIP file to the new folder
        zip_file_path = os.path.join(folder_path, file_name)
        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            zip_file.extractall(folder_path_new)


# Set the path to the directory to be searched
path = r"C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data"

# Create an empty dictionary to store the data
data_dict = {}
df = pd.DataFrame()

# Walk through the directory and find all Excel files in subdirectories
for root, dirs, files in os.walk(path):
    #for file in range(2):
        for file in files:
            if file.endswith(".xlsx") and not file.endswith(".zip"):
                # Get the country code from the folder name -> NO MOVED LOWER using a country name
                #country_code = os.path.basename(root)[:3]
                # Get the year from the file name
                year = file[9:13]
                filepath = os.path.join(root, file)
                # Load the Excel file
                workbook = openpyxl.load_workbook(filepath)
                # Select the sheet named "Table4.A"
                sheet = workbook['Table4.A']
                # Get the value from cell R10 a R11
                r10 = sheet['R10'].value
                r11 = sheet['R11'].value
                # print(r10)
                # print(r11)
                # Get the country name
                country_name_sheet = workbook['Table1s1']
                country_name = country_name_sheet['H3'].value

                # Add the data to the pandas data frame
                df.loc[year, f"{country_name} [R10]"] = r10
                df.loc[year, f"{country_name} [R11]"] = r11

                print(df)
print(df)
# save the data frame to a CSV file
df.to_csv(r'C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data\data_R10_R11.csv')