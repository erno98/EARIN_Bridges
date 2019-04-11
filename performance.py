import matplotlib.pyplot as plt
import pandas as pd

def bar_plot_time(results_file):
    with open(results_file) as csvdata:
        data = pd.read_csv(csvdata, sep='\t', usecols=(1, 2))

    data.plot(kind='bar')
    plt.yscale('log')
    plt.xlabel("Number of bridges")
    plt.ylabel("Time of computation [s]")
    plt.show()


results = "results_table.txt"

bar_plot_time(results)