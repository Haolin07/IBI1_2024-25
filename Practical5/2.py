#import the matplotlib
import matplotlib.pyplot as plt
#establish list to store population and locations
uk_countries = [57.11, 3.13, 1.91, 5.45]
countries = ['England', 'Wales', 'Northern Ireland', 'Scotland']
China_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
provinces = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
#sorted the population from high to low
sorted_uk = sorted(uk_countries, reverse=True)
sorted_China = sorted(China_provinces, reverse=True)
#print the sorted population
print(sorted_uk)
print(sorted_China)
#create plots 
plt.pie(uk_countries,labels = countries,autopct= '%1.2f%%')
plt.title('UK Population Sizes')
plt.show()
plt.pie(China_provinces,labels = provinces,autopct= '%1.2f%%')
plt.title('China Population Sizes')
plt.show()