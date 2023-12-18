'''Create a program using maths and f-Strings that tells us how many years/days/months/weeks we have left, if we live until 90 years old.'''

#Answer:

#create a veriable 'c_age' to take current age of the person.
c_age=int(input("Enter your Age: "))

#we know that, maximum age we can live is 90 years.
#so, substract current age from max age and store in variable 'r_year'(remaining years
r_year=90-c_age

#we know that, 1 year has 52 weeks.
#so, multiply r_year with 52, to find 'r_week'(remaining weeks).
r_weeks=r_year*52

#we know that, 1 year has 12 months.
#so, multiply r_year with 12, to find 'r_month'(remaining months).
r_month=r_year*12

#we know that, 1 year has 365 days.
#so, multiply r_year with 365, to find 'r_day'(remaining days).
r_day=r_year*365

#done. Now print the remaining years/days/months/weeks we have left, using f-Strings.
#in the below code: '\t' is tab to make space, and '\n' is tag for next line.
print(f'You only have:\n{r_year} years\tor\n{r_day} days\tor\n{r_month} months\tor\n{r_weeks} weeks.')

#----------------------------------------------------------------------------------------#
