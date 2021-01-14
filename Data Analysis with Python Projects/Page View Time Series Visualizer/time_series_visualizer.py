import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=True)

# Clean data
df_clear = df[df['value'] >= df['value'].quantile(0.025)]
df_clear = df_clear[df['value'] <= df['value'].quantile(0.975)]
df = df_clear.copy()

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32,10))
    ax.plot(df["value"],color='crimson',linewidth=3)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=24)
    ax.set_xlabel("Date", fontsize=20)
    ax.set_ylabel("Page Views", fontsize=20)
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(20)
    for label in ax.yaxis.get_ticklabels():
        label.set_fontsize(20)


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    dict = {"Jan":"January",'Feb':"February",'Mar':"March",'Apr':"April",'May':"May",'Jun': 'June',\
        'Jul':"July",'Aug':"August",'Sep':"September",'Oct':"October","Nov":"November",'Dec':"December"}
    df_bar['year'] = [d.year for d in df_bar.index]
    df_bar['month'] = [dict[d.strftime('%b')] for d in df_bar.index]
    df_bar = df_bar.groupby(["year",'month'])['value'].mean().reset_index(name='mean')
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    # Draw bar plot
    g = sns.catplot(x='year',y='mean', hue = 'month', kind = 'bar',data=df_bar,hue_order=months)
    fig = g.fig
    g.ax.set_xlabel("Years")
    g.ax.set_ylabel("Average Page Views")
    g._legend.remove()
    fig.axes[0].legend()



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(8)

    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    ax1 = sns.boxplot(x = df_box["year"], y = df_box["value"], ax= ax1)
    ax2 = sns.boxplot(x = df_box["month"], y = df_box["value"], ax= ax2, order = months)

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()
