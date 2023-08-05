
# coding: utf-8

# # Predicting the Economy with DataRobot Timeseries
# In this use case, we'll try to assess the outlook of the US economy. While hopefully it's not necessary to say so, let's just get this out of the way up front: don't actually invest your real money according to the results of this notebook. The real value comes from learning about how to use the Python client of the DataRobot API for Timeseries applications.
#
#
# ## Topics Covered in this Notebook
# Here is a list of things we'll do within this notebook:
#
# - Configure a DataRobot project to create a Timeseries project
# - Run the automated modeling process
# - Generate predictions from a finished model
#
# <div class="alert alert-box alert-warning">TODO - Links to these sections</div>
#
# ## Prerequisites
# In order to run this notebook yourself, you will need the following:
#
# - The dataset produced by the notebook titled `Gathering Example Timeseries Data`
# - A DataRobot API token
# - [matplotlib](http://matplotlib.org/users/installing.html) for the visualizations at the end

# ## Import necessary packages
# We'll use these in this notebook. If the following
# cell runs without issue, you're in good shape.

# In[1]:
import logging
import getpass
import re
import os
import datetime

import pandas as pd
import datarobot as dr


logging.basicConfig(format='%(asctime)-15s %(levelname)s %(message)s',
                    level=logging.DEBUG)

# ## Ensure DataRobot is configured
# The preferred way of configuring DataRobot is to use the configuration file, which will be read automatically. If you have not configured DataRobot this way, the following cell prompts you for your API token.

# In[2]:

logging.info('Block 1')

try:
    dr.Client()
except ValueError:
    import getpass
    api_token = getpass.getpass('Enter your api token here: ')
    dr.Client(endpoint='https://app.datarobot.com/api/v2', token=api_token)


# ## Find the data in your filesystem
# If you have run the other notebook, it will have written a file to disk. In the next cell, we'll try
# to find it in this directory. If it's not here, you can help the notebook continue by defining the variable `filename` to point to that file.

# In[9]:
logging.info('Block 2')

filepath = os.path.abspath('AirQualityUCI.xlsx')
print('Using {}'.format(filepath))
# try:
#     usecase_name_regex = re.compile('ts_financials-.*\.csv')

#     files = [fname for fname in os.listdir(os.path.expanduser('~'))
#              if usecase_name_regex.match(fname)]
#     filename = sorted(files)[-1]
#     filepath = os.path.expanduser('~/{}'.format(filename))
#     print('Using {}'.format(filepath))
# except IndexError:
#     print('Sorry, we did not find the data. Did you run the accompanying notebook?')
#     raise


# # Fix data

# In[40]:
logging.info('Block 3')

df = pd.read_excel(filepath)
datetime_col = df.apply(lambda r : pd.datetime.combine(r['Date'],r['Time']), axis=1)


# In[41]:

df['Datetime'] = df.apply(lambda r : pd.datetime.combine(r['Date'],r['Time']), axis=1)
df.drop(['Date', 'Time'], axis=1, inplace=True)
df.dropna(axis=1, how='all', inplace=True)
for col in df.columns:
    if col != 'Datetime':
        df[col] = df[col].map(lambda x: x if x != -200 else pd.np.NaN)


# In[ ]:




# # Configuring the Timeseries Project

# ## Create the Project
# Here, we use the `datarobot` package to upload a new file and create a project. The name of the project is optional, but can be helpful when trying to sort among many projects on DataRobot.

# In[42]:

logging.info('Block 4)')
proj = dr.Project.create(df, project_name='UCI Air Quality Dataset')


# ### Create a custom partition scheme
# We will need to use a custom partitioning scheme to let DataRobot to use timeseries.

# In[49]:

target_name = 'T'
fdw_start = -168  # Past 7 days, note the negative
fdw_end = 0  # Until now
forecast_window_start = 1  # Predictions starting 1 hour from forecast point
forecast_window_end = 12  # Predictions for the 12 hours from forecast point


# In[50]:

time_partition = dr.DatetimePartitioningSpecification(
    datetime_partition_column='Datetime',
    use_time_series=True,
    feature_derivation_window_start=fdw_start,
    feature_derivation_window_end=fdw_end,
    forecast_window_start=forecast_window_start,
    forecast_window_end=forecast_window_end
)


# In[51]:

logging.info('Block 5')
proj.set_target(target=target_name,
                worker_count=10,
                partitioning_method=time_partition,
                max_wait=1800)


# In[52]:
logging.info('Block 6')
proj.wait_for_autopilot(timeout=2400, check_interval=180)


# In[53]:
logging.info('Block 7')

proj.unlock_holdout()
models = proj.get_models()
model = models[0]
job = model.request_frozen_datetime_model()
print('Waiting for model to train on latest data')
final_model = job.get_result_when_complete(max_wait=1200)


# In[54]:

final_model = job.get_result_when_complete(max_wait=1200)


# # Construct the Timeseries Prediction Dataset

# In[55]:

logging.info('Block 8')
modeling_frame = df.copy()


# In[56]:

modeling_frame.head()


# In[61]:

historical_data = modeling_frame[fdw_start-1:].copy()  # n.b. extra row because fdw ends with 0
ultimate = historical_data.Datetime.iloc[-1]
penultimate = historical_data.Datetime.iloc[-2]
timedelta = ultimate - penultimate
future_dates = pd.date_range(start=ultimate + timedelta, periods=forecast_window_end, freq=timedelta)
future_data = pd.DataFrame(index=range(forecast_window_end), columns=modeling_frame.columns)
future_data['Datetime'] = future_dates
prediction_frame = pd.concat((historical_data, future_data))


# # Generate Future Predictions

# In[62]:
logging.info('Block 9')
pred_csv_path = os.path.expanduser('~/prediction_data.csv')
prediction_frame.to_csv(pred_csv_path, index=False, encoding='utf-8')
dataset = proj.upload_dataset(pred_csv_path)
pred_job = final_model.request_predictions(dataset_id=dataset.id)
preds = pred_job.get_result_when_complete()
preds


# ## Bonus Section: Predicting the future
# That concludes the "how-to" portion of the notebook. But we won't just leave you hanging... we've gone through all this trouble to try to predict the future. We might as well tell you what we saw.
#
# ### Get Ready to plot
# It will be easier to plot the data if it all shares the same time-based index. Here in this cell we read the modeling data and use its index, then we attach the predictions from each of the models to that dataframe
#
# <div class="alert alert-box alert-warning">
# This section still TODO
# </div>

# In[ ]:



