'''
Part III - Dictionary

Q6. Create a dictionary in the below format:
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
Print the first 3 key and value pairs of the dictionary:
'''

'''
Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
Print the first 3 key and value pairs of the dictionary:
'''
import csv
import re
from collections import defaultdict


#Q6, Q7
faculty_dict = defaultdict(list)
professor_dict = defaultdict(list)

with open('faculty.csv','r') as f:
  reader = csv.reader(f)
  reader.next() # skip header row
  for row in reader:
    name = row[0]
    match = re.search(r'(.*)\s([\w.-]+)$',name)
    first = match.group(1)
    last = match.group(2)

    degree = row[1]

    title = row[2]
    proper_title = re.search(r'[\w\s]*Professor',title).group()

    email = row[3]

    faculty_dict[last].append([degree, proper_title, email])
    professor_dict[(first, last)] = [degree, proper_title, email]


'''
Q8. It looks like the current dictionary is printing by first name. Sort by last name and print the first 3 key and value pairs.
'''
# print by last name order
sorted_keys = sorted(professor_dict.keys(), key = lambda x:x[-1])
for key in sorted_keys:
  print key, professor_dict[key]

