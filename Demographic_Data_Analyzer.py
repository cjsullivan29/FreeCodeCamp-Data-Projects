import pandas as pd

df = pd.read_csv('adult.data.csv')


#question 1 code
race_count = df['race'].value_counts()


#queston 2 code
average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)


#question 3 code
bachelors_count = len(df.loc[df['education'] == 'Bachelors'])
total_count = len(df['education'])

percent_bachelors = round(bachelors_count / total_count * 100, 1)


##question 4 code

    # higher edu
higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_edu_over_50 = higher_edu[higher_edu['salary'] == '>50K']

percent_higher = round((len(higher_edu_over_50) /len(higher_edu)) *100, 1)

    #lower edu
#lower_edu = df.loc[(df['education'] != 'Bachelors') | (df['education'] != 'Masters') | (df['education'] != 'Doctorate')]
lower_edu  = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_edu_over_50 = lower_edu[lower_edu['salary'] == '>50K']

percent_lower = round((len(lower_edu_over_50) / len(lower_edu)) * 100, 1)





##question 5 code

    # min hours worked
min_hours_per_week = df['hours-per-week'].min()

    # percentage of rich that work min hours
num_min_workers = df[df['hours-per-week'] == min_hours_per_week]
rich_count = len(num_min_workers[num_min_workers['salary'] == '>50K'])

percentage_rich = round((rich_count / len(num_min_workers)) * 100, 1)


##question 6 code

    #country with highest percentage of over 50K salaries

country_count = df['native-country'].value_counts()
rich_country_count = df[df['salary'] == '>50K']['native-country'].value_counts()


highest_earning_country = (rich_country_count / country_count * 100).idxmax()
highers_earning_country_percentage = round((rich_country_count / country_count * 100), 1).max()



##question 7 code

    #find the most popular occupation that makes over 50K

india_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
occupation_count = india_salary['occupation'].value_counts()

top_job = occupation_count.idxmax()

