
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
