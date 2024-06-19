#Remy Bikowski
#Project 4,implement a program that analyzes a data set.

import matplotlib.pyplot as plt 

#Print intro
def print_introduction():
    print('This program allows you to search through data')
    print('on the gross domestic product per capita for countries')
    print('in a given year')
    print()

#Get input from user on which year they would like to see data for
def get_user_input():
    global user_input
    user_input = int(input('please enter a year between 1801 and 2040: '))
    if user_input not in range(1801,2041):
        print('That is not a valid input, please try again')
        print()
        get_user_input()
    return user_input

#Create a list with years from 1800 to 2040.
#This list will be used to reference the appropriate index
def create_year_list():
    global years
    years = []
    for i in range(1800,2041):
        years.append(i)
    
#create dictionary with countries being key and appropiate year's gdp as element
def read_year_data(filename):
    global year_data
    year_data = {}
    index_year = years.index(get_user_input())
    file_access = open(filename, "r")
    file_access.readline()
    for line in file_access:
        country = line.split(',')
        year_data[country[0]] = int(country[index_year])    
    file_access.close()
    return 

#create an ordered list with pairs of tuples from dictionary. This will be used for
#graphing from smallest to greatest
def create_sorted_list():
    global sorted_gdp
    sorted_gdp = sorted(year_data.items(), key=lambda x: x[1], reverse=False)

#creates a dictionary with each country and as key and continent as element
#This will be used to color code bar graph
def continent_dictionary():
    global continents
    continents = {}
    f = open('continents.txt','r')
    for line in f:
        line = line.strip()
        country_continent = line.split(',')
        continents[country_continent[1]] = country_continent[0]
    return

#determine what color bar on graph will be based on continent country is from
def continent_color_association(country):
    if continents[country] == 'Africa':
        return 'orange'
    elif continents[country] == 'Asia':
        return 'yellow'
    elif continents[country] == 'Europe':
        return 'blue'
    elif continents[country] == 'North America':
        return 'green'
    elif continents[country] == 'Oceania':
        return 'red'
    elif continents[country] == 'South America':
        return 'pink' 
    
#Graph the GDP per capita per country, with a color association based on continent
def graphical_representation():
    keys = year_data.keys()
    values = year_data.values()
    for country in sorted_gdp:
        bar_color = continent_color_association(country[0])
        plt.bar(country[0],country[1],color=[bar_color])
    plt.xlabel('country')
    plt.ylabel('GDP/C adjusted for inflation to 2010 $USD')
    plt.title('GDP Per Capita in the year ' + str(user_input))
    plt.plot(0, 100, "orange", label="Africa")
    plt.plot(0, 100, "yellow", label="Asia")
    plt.plot(0, 100, "blue", label="Europe")
    plt.plot(0, 100, "green", label="North America")
    plt.plot(0, 100, "red", label="Oceania")
    plt.plot(0, 100, "pink", label="South America")
    plt.legend(loc="upper left")
    plt.xticks(color='w')
    plt.show()

    
print_introduction()
create_year_list()
read_year_data('income_per_capita.csv')
create_sorted_list()
continent_dictionary()
graphical_representation()


