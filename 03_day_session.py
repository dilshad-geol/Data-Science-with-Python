#Steps involved in Data visualizations
#Step#1: import libraries
import seaborn as sbn
import matplotlib.pyplot as plot
#Step#2: set a theme
sbn.set_theme(style="ticks", color_codes=True)
#Step#3: import data sets or you can also import your own data
kashti = sbn.load_dataset("titanic")
# print(kashti.describe())
# print(type(kashti))
#Step#4: plot basic graph(no y axis in count plot) single variable
# p = sbn.countplot(x="who", data = kashti)
# plot.show()

#step#5: with two variables i.e hue with titles
p = sbn.countplot(x="sex", data = kashti, hue="class")
p.set_title("Count Plot")
plot.show()