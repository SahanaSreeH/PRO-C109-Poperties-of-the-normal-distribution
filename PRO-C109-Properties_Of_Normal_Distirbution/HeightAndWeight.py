import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv("C:\Projects\class-109-Properties-of-normal-distribution-master\height-weight.csv")

list = df["Height(Inches)"].to_list()

mean = statistics.mean(list)

median = statistics.median(list)

mode = statistics.mode(list)

std_dev = statistics.stdev(list)


print("Height", mean, median, mode, std_dev)


first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

thin_1_std_deviation = [result for result in list if result > first_std_dev_start and result < first_std_dev_end]
thin_2_std_deviation = [result for result in list if result > second_std_dev_start and result < second_std_dev_end]
thin_3_std_deviation = [result for result in list if result > third_std_dev_start and result < third_std_dev_end]
