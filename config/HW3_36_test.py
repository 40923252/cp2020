from bokeh.plotting import figure, show, output_file
output_file("plot.html")
x = [10, 20, 30]
y = [4, 5, 6]
p = figure()
p.vbar(x=x, top=y, width=0.5)
show(p)