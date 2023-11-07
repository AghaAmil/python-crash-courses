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
