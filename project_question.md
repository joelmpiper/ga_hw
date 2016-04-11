## Predict daily solar energy with an ensemble of weather models

I would like to explore the prediction of solar energy at monitoring stations using weather prediction data at surrounding measuring locations. With increased demand for power from renewable sources and the need for utilities to anticipate the variability associated with changing weather patterns, the ability to predict incoming solar radiation can help influence the feasibility of solar utility projects in a given region by allowing them to appropriately plan for and respond to fluctuations in solar flux.

This analysis is based on a 2013 Kaggle competition for a series of weather stations in Oklahoma. The competition provides data from NOAA/ESRL Global Ensemble Forecast System Reforecast Version 2. It includes eleven forecasting models, with five daily forecasts at each of 98 Oklahoma Mesonet sites. Training data includes data collected from 1994-2007 and test data from 2008-2009.  This includes information on long-wave radiation, short-wave radiation, cloud cover, temperature, air pressure, accumulated precipitation, and several other variables. The prediction will also require the latitude, longitude, and elevation information of the collection stations to make predictions at sensor locations not included in the training or testing samples. 

The data for the competition will need to be translated, cleaned, and extracted into a format readable by scikit-learn.
* The data uses netCDF4 format, which can be ingested into Python with  the netCDF package. It produces an x-dimensional (5-dimensional in the example) vector with metadata intregrated into the data structure.
* I will investigate the data using some minimal aggregation techniques with the standard pandas/sklearn tools to see if I can provide a competitive analysis to the top-performing models in the competition.	

Although I will be using an aggregated data set for the analysis (as was done for the winning submissions), I have several optional stretch goals to explore other data science techniques:

1. Explore using the full dataset with storage and analysis using Amazon Web Services and Apache Spark.
2. Examine the data provided by the NREL on hourly solar flux and hourly weather data by location to make predictions on data that was not included in the competition. 
3. Identify specific power plant solar energy generation data to predict the energy produced given the solar flux and capacity information for a given plant.

