import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def read_files():
    '''Function reads the files from the directory where we have all the 
    raw data files downloaded and stored in csv format and assigns the right 
    name for each data file after cleaning the raw data files and transforming
    them into clean files. '''
    #changing the current working directory to the desired directory. 
    os.chdir(
        'C:/Users/anton/Desktop/Assignment2/Assignment data files/Final Files')
    files = os.listdir()
    #Iterating through all the files in the directory.
    for file in files:
    #Reading all the files and cleaing them.
        df = pd.read_csv(file)
        df = df.dropna().set_index('Country Name').loc[['India',
        'United Kingdom', 'United States', 'Germany', 'Japan', 'China',
        'Korea, Rep.'], ['1995 [YR1995]', '2000 [YR2000]', '2005 [YR2005]',
        '2010 [YR2010]', '2015 [YR2015]', '2019 [YR2019]']]
        li = df.columns.values
    #Converting the datatype of each column to flaot.
        for i in li:
            df[i] = df[i].astype(float)
    #Renaming the columns in the dataframe.
        df.columns = ['1995', '2000', '2005', '2010', '2015', '2019']
   #Renaming the dataframes with appropriate names.     
        if 'Forest' in file:
            forest_area = df 
        elif 'Population' in file: 
            population = df
        elif 'R_E' in file: 
            renew_energy_consumption = df
        elif 'Total' in file: 
            total_green_house_emission = df
        elif 'CO2' in file: 
            co2_emissions = df
    #Calling the  functions.
    pop_groupedbar(population)
    greenhouse_groupedbar(total_green_house_emission)
    co2_time_series(co2_emissions)
    forest_area_time_series(forest_area)
    df_summary(forest_area, population, renew_energy_consumption,
               co2_emissions, total_green_house_emission)
    df_correlation(forest_area, population, renew_energy_consumption,
                   co2_emissions, total_green_house_emission)
    india_correlation(forest_area, population, renew_energy_consumption,
                      co2_emissions, total_green_house_emission)
    
    
def pop_groupedbar(population): 
    '''Function creates a grouped bar chart which displays the population
    growth of TOP7 world countries from 1995 to 2019 with a 5 year interval.
    Argument of the function is the population dataframe.'''
    #Plotting and formatting the grouped bar chart.
    population.plot(kind = 'bar', width = 0.9, rot = 45)
    plt.title('Population Growth Over Years', **font1)
    plt.legend(loc ='upper right')
    plt.grid(zorder = 0)
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.xlabel('Countries', **font2)
    plt.ylabel('Population', **font2)
    plt.xticks(**font3)
    plt.yticks(**font3)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.show()
    
    
def greenhouse_groupedbar(total_green_house_emission):
    '''Function creates a grouped bar chart which displays the greenhouse 
    gas emissions of TOP 7 world countries from 1995 to 2019 with a 5 year 
    interval
    Argument of the function is the total_green_house_emission dataframe.'''
    #Plotting and formatting the grouped bar chart.
    total_green_house_emission.plot(kind = 'bar', width = 0.9, rot = 45)
    plt.title('Green House Gases Emission Over Years', **font1)
    plt.grid(zorder = 0)
    plt.xlabel('Countries', **font2)
    plt.ylabel('Green House Emissions in Kt', **font2)
    plt.xticks(**font3)
    plt.yticks(**font3)
    #Setting the figure size for the chart.
    plt.rcParams['figure.figsize'] = (12, 8)
    #Providing exact value in the y-axis instead of values in exponential form.
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.show()

    
def co2_time_series(co2_emissions):
    ''' Function creates a stacked line plot which represents the time series
    for CO2 emissions for TOP 7 world countries from 1995 to 2019 with a 
    5 year interval
    Argument of the function is the co2 emissions dataframe.'''
    #Transposing the dataframe to create time series.
    co2_emissions_transpose = pd.DataFrame.transpose(co2_emissions)
    #Plotting and formatting the time series using a stacked line plot.
    co2_emissions_transpose.plot(kind = 'line', linewidth = 3, marker = 'x')
    plt.legend()
    plt.title('CO2 Emissions', **font1)
    plt.xlabel('Years', **font2)
    plt.ylabel('CO2 Emissions in Kt', **font2)
    plt.xticks(**font3)
    plt.yticks(**font3)
    plt.legend(loc = 'best')
    plt.grid(zorder = 0)
    #Setting the figure size for the chart.
    plt.rcParams['figure.figsize'] = (12, 8)
    #Providing exact values in the ymaxis instead of values in exponential form
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.show()
    
    
def forest_area_time_series(forest_area):
    '''Function creates a stacked line plot which represents the time series
    for Foreast Area in sq km for TOP 7 world countries from 1995 to 2019 with 
    a 5 year interval
    Argument of the function is the forest area dataframe.'''
    #Transposong the dataframe to create time series.
    forest_area_transpose = pd.DataFrame.transpose(forest_area)
    #Plotting and formatting the time series using a stacked line plot.
    forest_area_transpose.plot(kind = 'line', linewidth = 3, marker = 'x')
    plt.legend()
    plt.title('Forest Area', **font1)
    plt.xlabel('Years', **font2)
    plt.ylabel('Forest Area in sq km', **font2)
    plt.xticks(**font3)
    plt.yticks(**font3)
    plt.legend(loc = 'best')
    plt.grid(zorder = 0)
    #Setting the figure size for the chart.
    plt.rcParams['figure.figsize'] = (12, 8)
    #Providing exact values in the y-axis instead of values in exponential form
    plt.ticklabel_format(style = 'plain', axis = 'y')   
    plt.show()

    
def df_summary(forest_area, population, renew_energy_consumption,
               co2_emissions, total_green_house_emission):
    '''Function provides the summary statistics using the pandas describe 
    function for all the dataframes
    Arguments of the function are all the dataframes used in this project'''
    print('\n \n \t  SUMMARY STATISTICS OF ALL DATA : ')
    print('Summary statistis of Forest Area :  ')
    print(forest_area.describe())
    print('Summary statistis of  Population : ')
    print(population.describe())
    print('Summary statistis of CO2 Emissions : ')
    print(co2_emissions.describe())
    print('Summary statistis of Total Green House Gas Emissions :  ')
    print(total_green_house_emission.describe())
    print('Summary statistis of Renewable Energy Consumption : ')
    print(renew_energy_consumption.describe())

    
def  df_correlation(forest_area, population, renew_energy_consumption,
                    co2_emissions, total_green_house):
    '''Function creates a new data frame final_countries_mean which has a mean
    column from all the dataframes used above and then creates a heatmap
    which shows the correlation of all the columns in the final_countries_mean
    dataframe.
    Arguments of the function are all the dataframes used in the project'''
    
    '''Creating a new column called mean for all the dataframes and calculating
    the row wise mean for each dataframe and assiging it to the new 'mean' 
    column created for each data frame.
    New 'mean' column for each data frame will contain the country wise mean of
    all the values provided for the years between 1995 to 2019'''
    forest_area['mean'] = forest_area.mean(axis = 1)
    co2_emissions['mean'] = co2_emissions.mean(axis = 1)
    population['mean'] = population.mean(axis = 1)
    total_green_house['mean']=total_green_house.mean(axis=1)
    renew_energy_consumption['mean'] = renew_energy_consumption.mean(axis = 1)
    #Creating a new dataframe named 'final_countries_mean'.
    final_countries_mean = pd.DataFrame()
    #Assiging all mean columns to new dataframe under appropriate column names.
    final_countries_mean['Forest Area'] = forest_area['mean']
    final_countries_mean['CO2 Emissions'] = co2_emissions['mean']
    final_countries_mean['Ren.Energy Consump']=renew_energy_consumption['mean']
    final_countries_mean['GreenHouse Gas']=total_green_house['mean']
    final_countries_mean['Population'] = population['mean']
    '''Calling the function which will calculate skewness and kurtosis on all
    the columns in the final_countries_mean dataframe'''
    skew_and_kurt(final_countries_mean)
    '''Creating a new dataframe 'final_countries_mean_corr' which contains the
    correlation coefficient values for the 'final_countries_mean' dataframe.'''
    final_countries_mean_corr = final_countries_mean.corr()
    #Plotting and formatting the heatmap for correlation coefficients.
    sns.heatmap(final_countries_mean_corr, linewidth = 2, 
                cmap = 'Greens', annot = True, annot_kws = {"size" : 15})
    plt.title('Correlation Heatmap of TOP 7 World Countries', **font1)
    plt.xticks(**font2)
    plt.yticks(**font2)
    #Setting the figure size for the heatmap.
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.show()
    
    
def skew_and_kurt(final_countries_mean) : 
    '''Function provides the skewness and kurtosis values for all the columns
    in the final_countries_mean dataframe
    Arguments of the function are all the dataframes used in the project'''
    print('\n \n \t SKEWNESS AND KURTOSIS OF ALL DATA : ')
    '''Prints the skewness and kurtosis using skew and kurtosis functions of
    the scipy.stats module.'''
    print("Skewness of Forest Area : ",
          stats.skew(final_countries_mean['Forest Area']))
    print("Kurtosis of Forest Area : ",
          stats.kurtosis(final_countries_mean['Forest Area']))
    print("Skewness of CO2 Emission : ",
          stats.skew(final_countries_mean['CO2 Emissions']))
    print("Kurtosis of CO2 Emissions : ",
          stats.kurtosis(final_countries_mean['CO2 Emissions']))
    print("Skewness of  Renewable Energy Consumption : ",
          stats.skew(final_countries_mean['Ren.Energy Consump']))
    print("Kurtosis of Renewable Energy Consumption : ",
          stats.kurtosis(final_countries_mean['Ren.Energy Consump']))
    print("Skewness of Total Green House Gas Emissions : ",
          stats.skew(final_countries_mean['GreenHouse Gas']))
    print("Kurtosis of Total Green House Gas Emissions : ",
          stats.kurtosis(final_countries_mean['GreenHouse Gas']))
    print("Skewness of Population : ",
          stats.skew(final_countries_mean['Population']))
    print("Kurtosis of Population : ",
          stats.kurtosis(final_countries_mean['Population']))

    
def india_correlation(forest_area, population, renew_energy_consumption,
                      co2_emissions, total_green_house_emission) : 
    '''Function creates a dataframe india_df which has values of India from all
    the dataframes used above. Function also creates a heat map which shows
    the correlation between different columns in the india_df.
    Arguments of the function are all the dataframes used in the project'''
    india_df = pd.DataFrame()
    #Assigning values of India from all the dataframes to india+df.
    india_df['Forest Area'] = forest_area.loc['India', :]
    india_df['Population'] = population.loc['India', :]
    india_df['Renew Energy Consump.']=renew_energy_consumption.loc['India', :]
    india_df['CO2 Emissions'] = co2_emissions.loc['India', :]
    india_df['Green House Emiss.'] = total_green_house_emission.loc['India', :]
    #Creating a new dataframe india_corr which contains the correlation values.
    india_corr = india_df.corr()
    #Plotting and formatting a heat map for india's correlation values.
    sns.heatmap(india_corr, linewidth = 2, cmap = 'Blues',
                annot = True, annot_kws={"size" : 15})
    plt.title('Correlation Heatmap of INDIA', **font1)
    plt.xticks(rotation = 90, **font2)
    plt.yticks(**font2)
    #Setting the figure size for the heatmap.
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.show()
    

#Setting up the font sizes to format the visualizations    
font1 = {'fontsize' : 18}
font2 = {'fontsize' : 15}    
font3 = {'fontsize' : 13.5} 
#Calling the function read_files
read_files()
