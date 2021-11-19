fname = "Adimike"
sname = "Sylvia"
full_name = fname+' '+ sname
print(full_name)


name = 'Sylvia'
age = '49'
city = 'Lagos'

statement = 'My name is '+name+', i am '+str(age)+' years old and i live in '+city
print(statement)

name = 'Obasanjo'
country = 'Nigeria'
year = 1999
name2 = 'Yaradua'
year2 = 2007

sentence = name+ ' was the president in ' +country+ ' in the year ' +str(year)+ ' and handed over to ' +name2+ ' in ' +str(year2)
print(sentence)

result = '{} was the president of {} in the year {} and handed over to {} in {}'.format(name,country,year,name2,year2)
print(result)

Statement = f'{name} was the president of {country} in the year {year} and handed over to {name2} in {year2}'
print(Statement)

output = name+ ' was the president of '
output += country+ ' in the year '
output += str(age)+ ' and handed over to '
output += name2+ ' in '
output += str(year2)
print(output)