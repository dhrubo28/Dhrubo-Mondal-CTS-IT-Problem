# Citations
# [1] https://docs.python.org/3/library/csv.html
# [2] https://realpython.com/python-csv/
# [3] https://www.kite.com/python/answers/how-to-skip-the-first-line-of-a-csv-file-in-python
# [4] https://docs.python.org/3/howto/sorting.html
# [5] https://docs.python.org/3/library/operator.html
# [6] https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
# [7] https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
# [8] https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# not implemented (lines 13, 159-164) - https://docs.python.org/3/library/collections.html

import csv
from typing import Counter
from tabulate import tabulate
import operator
import matplotlib.pyplot as plt

def main():
    
    pres_name = ""
    birth_date = ""
    death_date = ""
    
    birth_year = 0
    lived_years = 0
    death_year = 0
    lived_months = 0
    lived_days = 0
    
    pres_info = []
    pres_info2 = []
    lived_days_list = []
    measures_table_info = []
    
    mean = 0
    weighted_mean = 0
    median = 0 
    mode = 0 
    max = 0 
    min = 0 
    standard_deviation = 0
    total_lived_days = 0
    fir_part = 0
    
    # [1, 2] input data from CSV file
    with open('U.S. Presidents Birth and Death Information - Sheet1.csv') as presidents:
        
        input = csv.reader(presidents)
        
        # [3] skip the first row
        next(input)
        
        for info in input:
            pres_name = info[0]
            birth_date = info[1]
            death_date = info[3]
            
            # 1. get year of birth

            # get the index of the comma in birth date to get the year after the comma
            find_comma = birth_date.find(',')
            
            # since every date has a comman, this check is to ensure that we get the date ?
            if find_comma != -1:
                
                birth_year2 = birth_date[find_comma + 1:].strip()
                birth_year = int(birth_year2)
                
            # 2. get years lived 

            # get president and former presidents that are living
            if death_date == "":
                 
                lived_years = 2021 - birth_year
                                                    

            # get years lived of dead former president
            else:
                        
                # get the death year 
                find_comma2 = death_date.find(',')
                                                
                if find_comma2 != -1 and find_comma2 < 10:
                    
                    death_year2 = death_date[find_comma2 + 1:].strip()
                    death_year = int(death_year2)
                    
                    # death_year was giving some former presidents who with year less than 100 so check to remove it
                    if death_year > 100: 
                            
                        lived_years = death_year - birth_year

            # 3. get months lived of presidents 
            lived_months = lived_years * 12

            # 4. get days lived of presidents 
            lived_days = ((lived_months - 5) * 31) + ((lived_months - 8) * 30) + ((lived_months - 11) * 29)
            lived_days_list.append(lived_days)

            # 5. make the two tables of the top 10 shortest and longest lived president

            # info and data for the tables
            pres_info = [(pres_name, birth_year, lived_years, lived_months, lived_days)]
                    
            for i in pres_info:
                        
                pres_info2.append(i)
            
            # [4, 5] sort the days lived of presidents in shortest order
            sort_shortest_lived = sorted(pres_info2, key=operator.itemgetter(4))
            
            # get top 10 days lived of presidents in shortest order
            top10_shortest_lived = sort_shortest_lived[:10]

            # [6, 7] header for the tables
            header = ["President Name", " Year of Birth", "Years Lived", " Months Lived", "Days Lived"]
           
            # [6, 7] table of the top 10 days lived of presidents in shortest order
            top10_shortest_lived_table = tabulate(top10_shortest_lived, headers=header, tablefmt="fancy_grid")
            # print(top10_shortest_lived_table)

             # [4, 5] sort the days lived of presidents in longest order
            sort_longest_lived = sorted(pres_info2, key=operator.itemgetter(4), reverse=True)
            
            # get top 10 days lived in longest order
            top10_longest_lived = sort_longest_lived[:10]
            
            # [6, 7] table of the top 10 days lived of presidents in longest order
            top10_longest_lived_table = tabulate(top10_longest_lived, headers=header, tablefmt="fancy_grid")
            # print(top10_longest_lived_table)

            # 6. calculate the measurements 

            for i in range(0, len(lived_days_list)):

                # find mean of the days lived of presidents 
                total_lived_days = lived_days_list[i] + total_lived_days
                mean = total_lived_days / len(lived_days_list)
                
                # find weighted mean of the days lived of presidents 
                weighted_mean = (1 * total_lived_days) / total_lived_days 
                max = lived_days_list[i]
                
                # find median of the days lived of presidents 
                lived_days_list.sort()
                
                # if even numbers in list 
                if len(lived_days_list) % 2 == 0:
                   
                    sec_middle_num = (int) (len(lived_days_list) / 2 / 2)
                    fir_middle_num = (int) ((len(lived_days_list) / 2) - 1)
                    median = (int) ((lived_days_list[sec_middle_num] + lived_days_list[fir_middle_num]) / 2)
                
                # if odd numbers in list     
                else:

                    median = lived_days_list[(int)(len(lived_days_list) / 2)]
                
                # find mode of the days lived of presidents
                # for j in range(0, len(lived_days_list)):
                    # if Counter(lived_days_list[j]) > 1:
                        # mode = max(Counter(lived_days_list[j]))
                    # else:
                        # mode = 0 
                
                # president with the highest number of days lived
                max = lived_days_list[0]
                
                if lived_days_list[i] > max:
                    max = lived_days_list[i]
               
                # president with the lowest number of days lived
                min = lived_days_list[0]
                
                if lived_days_list[i] < min:
                    min = lived_days_list[i]
                
                # find the standard deviations of the number of days lived of presidents combined 
                fir_part = pow((lived_days_list[i] - mean), 2) + fir_part
                standard_deviation = fir_part / (int) (len(lived_days_list))
               
                # 7. make the table of the measurements 

                measures = [(mean, weighted_mean, mode, max, min, standard_deviation)]
                
                for i in measures:
                        
                    measures_table_info.append(i)

                # [6, 7] header for measurement table of days lived of presidents
                header2 = ["Mean", "Weighted Mean", "Median", "Mode", "Maximum", 
                            "Minimum", "Standard Deviation"]
                
                # [6, 7] measurement table of days lived of presidents
                measures_table = tabulate(measures_table_info, headers=header2, tablefmt="fancy_grid")
                # print(measures_table)
                
                # 8. make the plots of each measurement 

                # [8] plot for mean of days lived
                plt.plot(lived_days, mean)
                plt.xlabel("Days Lived")
                plt.ylabel("Mean of Days Lived")
                plt.show()
                
                # [8] plot for weighted mean of days lived
                plt.plot(lived_days, weighted_mean)
                plt.xlabel("Days Lived")
                plt.ylabel("Weighted Mean")
                plt.show()

                # [8] plot for median of days lived
                plt.plot(lived_days, median)
                plt.xlabel("Days Lived")
                plt.ylabel("Median of Days Lived")
                plt.show()

                # [8] plot for mode of days lived
                plt.plot(lived_days, mode)
                plt.xlabel("Days Lived")
                plt.ylabel("Mode of Days Lived")
                plt.show()

                # [8] plot for president with the highest number of days lived 
                plt.plot(lived_days, max)
                plt.xlabel("Days Lived")
                plt.ylabel("Highest Day Lived by a President")
                plt.show()

                # [8] plot for president with the lowest number of days lived 
                plt.plot(lived_days, min)
                plt.xlabel("Days Lived")
                plt.ylabel("Lowest Day Lived by a President")
                plt.show()

                # [8] plot for standard deviation of days lived
                plt.plot(lived_days, standard_deviation)
                plt.xlabel("Days Lived")
                plt.ylabel("Standard Deviation of Days Lived")
                plt.show()

if __name__ == "__main__":
    main()
