# Reading the file
file = open('student_country_data.csv', 'r')

# Creating a dictionary that maps each country to a list of students from that country
country_to_students = {}

# Creating 2 dictionaries that map a country to the number of students from that country in one of the cohorts
cohort_1 = {}
cohort_2 = {}

# This loop populates our three dictionaries
for line in file:
    student_data_as_list = line.split(',')  # Getting individual data

    if country_to_students.get(student_data_as_list[1]) is None:  # When country is not in dictionary, add it
        country_to_students[student_data_as_list[1]] = [student_data_as_list[0].strip()]
    else:  # Country is in dictionary, add one more student to its corresponding list
        country_to_students[student_data_as_list[1]] += [student_data_as_list[0].strip()]

    # Adding every country to both cohort dictionaries
    cohort_1[student_data_as_list[1]] = 0
    cohort_2[student_data_as_list[1]] = 0

    # Depending on the cohort of the student, increment appropriate cohort
    if student_data_as_list[2].strip() == '1':
        cohort_1[student_data_as_list[1]] += 1
    else:
        cohort_2[student_data_as_list[1]] += 1
file.close()

# Function to get sole representatives
def get_sole_representatives():
    print('\nThe following students are the sole representatives of their country:')
    for country in country_to_students:
        if len(country_to_students[country]) == 1:  # If there is only one name in the list of students
            print(country_to_students[country][0] + ' from ' + country)


# Function to get number of students per country and per cohort
def get_students_per_cohort():
    country = input("\nWhat country's data do you want? ")  # Get the country from users

    # Print the number of students from the specified country in each cohort
    if cohort_1.get(country) is not None:
        print('In cohort 1, there are ' + str(cohort_1[country]) + ' students from ' + country)
    if cohort_2.get(country) is not None:
        print('In cohort 2, there are ' + str(cohort_2[country]) + ' students from ' + country)

    # In case the input is not a country in our dataset
    if cohort_1.get(country) is None and cohort_2.get(country) is None:
        print('We do not have that country here')


# Calling our functions
get_sole_representatives()
get_students_per_cohort()
