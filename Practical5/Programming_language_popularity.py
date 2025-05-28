##import the matplotlib
import matplotlib.pyplot as plt
##establish a dictionary to store the languages and percentage
language = {"JavaScript" :62.3, "HTML" :52.9, "Python" :51, "SQL" :51, "TypeScript" :38.5}
##print the dictionary
print([language])
##creat a bar plot 
plt.bar(language.keys(), language.values())
##set the title , x label and y label
plt.title("Programming language popularity")
plt.xlabel("languages")
plt.ylabel("percentage")
##output the plot
plt.show()
##change the language to see the popularity
selected_language = 'HTML'
##display the value of the key
print(language[selected_language])