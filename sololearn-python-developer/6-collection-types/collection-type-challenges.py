"""
You are working on a recruitment platform, which should match the available jobs and the candidates based on their
skills. The skills required for the job, and the candidate's skills are stored in sets. Complete the program to
output the matched skill.

Note: Display the result as string

"""

skills = {'Python', 'HTML', 'CSS', 'SQL', 'C++', 'Java', 'Scala', 'C#'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

matched_skills = skills & job_skills
print(matched_skills)

matched_skills_str = ''

for i in matched_skills:
    matched_skills_str += i

print(matched_skills_str)

"""
Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u. 

Sample Input
awesome

Sample Output 
['w', 's', 'm'] 
"""

# That how noobs do it:

# input_word = input('Enter your preferred word: ')
# output = [i for i in input_word if i != 'a' if i != 'e' if i != 'i' if i != 'o' if i != 'u']
# print(output)

input_word = input('Enter your preferred word: ')
vowels = ['a', 'e', 'i', 'o', 'u']

output_word = [i for i in input_word if i not in vowels]
print(output_word)
