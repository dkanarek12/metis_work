'''
Part I - Regular Expressions

Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor

Q3. Search for email addresses and put them in a list. Print the list of email addresses.

Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.
'''
import csv
import re
from collections import defaultdict

degrees, titles, emails = [], [], []
with open('faculty.csv','r') as f:
  reader = csv.reader(f)
  reader.next() # skip header row
  for row in reader:
    degrees.append(row[1].lower().replace('.',''))
    titles.append(row[2].lower())
    emails.append(row[3].lower())

# Q1.
degree_dict = defaultdict(int)

all_degrees = ' '.join(degrees).split()
for degree in all_degrees:
  if degree.isalpha():
    degree_dict[degree] += 1
print degree_dict

# Q2.
title_dict = defaultdict(int)
for title in titles:
  proper_title = re.search(r'[\w\s]*professor',title).group()
  title_dict[proper_title] += 1
print title_dict

# Q3.
print emails

# Q4.
domain_dict = defaultdict(int)
for email in emails:
  domain = re.search(r'@(.*)',email).group(1)
  domain_dict[domain] += 1
print domain_dict, len(domain_dict), domain_dict.keys()


'''
Q5. Write email addresses from Part I to csv file
Your file, emails.csv, will look like this:

bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
'''
with open('email.csv','wb') as f:
  writer = csv.writer(f)
  for email in emails:
    writer.writerow([email])

