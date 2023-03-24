from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from datetime import datetime, timedelta
import sqlite3

# connect to database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# define exclude lists
machine_list_name = ['M1', 'M2']
developer_list_name = ['John']
already_involved_list_name = ['Leif']

# define the time range for the trends
end_time = datetime.now()
start_time = end_time - timedelta(days=30)
today_start = datetime.combine(datetime.today(), datetime.min.time())
today_end = datetime.combine(datetime.today(), datetime.max.time())

# define a function to get the data for a specific time range
def get_data(start, end):
    query = f"SELECT boot_time, user_name FROM mytable WHERE boot_time >= '{start}' AND boot_time <= '{end}'"
    result = c.execute(query).fetchall()
    data = {}
    for row in result:
        boot_time = datetime.strptime(row[0], '%Y%m%d%H')
        user_name = row[1]
        if user_name not in data and user_name not in already_involved_list_name and user_name not in developer_list_name and boot_time.strftime('%H') != '08' and boot_time.strftime('%H') != '09' and boot_time.strftime('%H') != '10' and boot_time.strftime('%H') != '11':
            data[user_name] = {'x': [], 'y': []}
        if user_name in data and user_name not in already_involved_list_name and user_name not in developer_list_name and boot_time.strftime('%H') != '08' and boot_time.strftime('%H') != '09' and boot_time.strftime('%H') != '10' and boot_time.strftime('%H') != '11':
            data[user_name]['x'].append(boot_time)
            data[user_name]['y'].append(1)
    return data

# create the data source for the trends
data_source_30d = ColumnDataSource(data=get_data(start_time, end_time))
data_source_today = ColumnDataSource(data=get_data(today_start, today_end))

# create the figures for the trends
fig_30d = figure(title='Last 30 Days', x_axis_label='Date', y_axis_label='Number of Records', x_axis_type='datetime')
fig_30d.vbar(x='x', top='y', width=2*60*60*1000, source=data_source_30d)

fig_today = figure(title='Today', x_axis_label='Hour', y_axis_label='Number of Records', x_axis_type='datetime')
fig_today.vbar(x='x', top='y', width=30*60*1000, source=data_source_today)

# define a function to update the data sources periodically
def update():
    data_source_30d.data = get_data(start_time, end_time)
    data_source_today.data = get_data(today_start, today_end)

# add the figures to the document and define the periodic update
curdoc().add_root(column(fig_30d, fig_today))
curdoc().add_periodic_callback(update, 60*1000)
