# Напишете програма, която изчислява колко часа ще са необходими на един архитект, за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.

architect = input()
project_num = int(input())
project_time = project_num * 3
print(f"The architect {architect} will need {project_time} hours to complete {project_num} project/s.")
