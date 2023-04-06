import pandas as pd
import matplotlib.pyplot as plt

# read CSV file into a DataFrame
data = pd.read_csv(r'C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\data\data_R10_R11.csv', index_col=0)

# create a line chart for each column (except index)
for col in data.columns[1:]:
    plt.plot(data.index, data[col])
    plt.title(col + " Net carbon stock change in soils - Mineral soils")
    plt.xlabel("Year")
    plt.ylabel("Kt C")
    # Add 0.5 inches of whitespace to each side of the chart
    plt.subplots_adjust(left=0.17)
    # save the chart in the specified folder
    plt.savefig(r'C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF\charts\R10\{}.png'.format(col))
    plt.clf()
