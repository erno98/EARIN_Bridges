import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_clustered_stacked(dfall, labels=None, title="IDFS & A* vs time of their computation",  H="/", **kwargs):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot.
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns)
    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=0,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      **kwargs)  # make bar plots

    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                rect.set_hatch(H * int(i / n_col)) #edited part
                rect.set_width(1 / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(df.index, rotation = 0)
    axe.set_title(title)

    # Add invisible data to add another legend
    # n=[]
    # for i in range(n_df):
    #     n.append(axe.bar(0, 0, color="gray", hatch=H * i))
    #
    # l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
    # if labels is not None:
    #     l2 = plt.legend(n, labels, loc=[1.01, 0.1])
    # axe.add_artist(l1)
    return axe


def bar_plot_time(results_file):
    with open(results_file) as csvdata:
        data = pd.read_csv(csvdata, sep='\t', usecols=(0, 1, 2, 3))

    data.sort_values(by='Depth', inplace=True)
    # print(data)
    # data_time = data[['IDFS time', 'A* time']]

    data_time_idfs_5 = [data['IDFS time'][d] for d in range(0, len(data['IDFS time'])) if data['Size'][d] == 5]
    data_time_a_star_5 = [data['A* time'][d] for d in range(0, len(data['A* time'])) if data['Size'][d] == 5]
    data_time_idfs_7 = [data['IDFS time'][d] for d in range(0, len(data['IDFS time'])) if data['Size'][d] == 7]
    data_time_a_star_7 = [data['A* time'][d] for d in range(0, len(data['A* time'])) if data['Size'][d] == 7]

    data_time_idfs = pd.DataFrame(np.array([data_time_idfs_5, data_time_idfs_7])).transpose()
    data_time_a_star = pd.DataFrame(np.array([data_time_a_star_5, data_time_a_star_7])).transpose()

    plot_clustered_stacked([data_time_idfs, data_time_a_star], ['idfs', 'a*'])

    # data_time = pd.DataFrame({"IDFS time" : data_time_idfs,
    #                          "A* time" : data_time_a_star}, index=[str(i) for i in range(0, 7)])


    # data_time = pd.DataFrame({"IDFS 5 time" : data_time_idfs_5,
    #                            "A* 5 time" : data_time_a_star_5,
    #                            "IDFS 7 time" : data_time_idfs_7,
    #                             "A* 7 time": data_time_a_star_7}, index=[str(i) for i in range(0, 7)])


    N = 7
    width = 0.2
    ind = np.arange(N)


    #
    # p1 = data_time_idfs.plot.bar(stacked=True)
    # p2 = data_time_a_star.plot.bar(stacked=True)

    # p1 = plt.bar(ind, data_time_idfs, width)

    #data_time.plot.bar(rot=0)

    # plt.xticks(ticks=list(range(0, 14)), labels=data['Depth'])
    plt.yscale('log')
    plt.legend(['a', 'b', 'c','d'])
    plt.xlabel("Number of bridges")
    plt.ylabel("Time of computation [s]")
    plt.show()


results = "results_table.txt"
bar_plot_time(results)
