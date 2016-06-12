## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.


![png](/img/advanced_python_plots/degree_hist.png)


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

![png](/img/advanced_python_plots/title_hist.png)


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>['bellamys@<i></i><i></i>mail.med.upenn.edu', 'warren@<i></i>upenn.edu', 'bryanma@<i></i>upenn.edu', 'jinboche@<i></i>upenn.edu', 'sellenbe@<i></i>upenn.edu', 'jellenbe@<i></i>mail.med.upenn.edu', 'ruifeng@<i></i>upenn.edu', 'bcfrench@<i></i>mail.med.upenn.edu', 'pgimotty@<i></i>upenn.edu', 'wguo@<i></i>mail.med.upenn.edu', 'hsu9@<i></i>mail.med.upenn.edu', 'rhubb@<i></i>mail.med.upenn.edu', 'whwang@<i></i>mail.med.upenn.edu', 'mjoffe@<i></i>mail.med.upenn.edu', 'jrlandis@<i></i>mail.med.upenn.edu', 'liy3@<i></i>email.chop.edu', 'mingyao@<i></i>mail.med.upenn.edu', 'hongzhe@<i></i>upenn.edu', 'rlocalio@<i></i>upenn.edu', 'nanditam@<i></i>mail.med.upenn.edu', 'knashawn@<i></i>mail.med.upenn.edu', 'propert@<i></i>mail.med.upenn.edu', 'mputt@<i></i>mail.med.upenn.edu', 'sratclif@<i></i>upenn.edu', 'michross@<i></i>upenn.edu', 'jaroy@<i></i>mail.med.upenn.edu', 'msammel@<i></i>cceb.med.upenn.edu', 'shawp@<i></i>upenn.edu', 'rshi@<i></i>mail.med.upenn.edu', 'hshou@<i></i>mail.med.upenn.edu', 'jshults@<i></i>mail.med.upenn.edu', 'alisaste@<i></i>mail.med.upenn.edu', 'atroxel@<i></i>mail.med.upenn.edu', 'rxiao@<i></i>mail.med.upenn.edu', 'sxie@<i></i>mail.med.upenn.edu', 'dxie@<i></i>upenn.edu', 'weiyang@<i></i>mail.med.upenn.edu']


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>['mail.med.upenn.edu' 'upenn.edu' 'email.chop.edu' 'cceb.med.upenn.edu']

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@<i></i>upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@<i></i>mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@<i></i>email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@<i></i>mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@<i></i>upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>{'Putt': [['PhD ScD', 'Professor', 'mputt@<i></i>mail.med.upenn.edu']], 'Feng': [['Ph.D', 'Assistant Professor', 'ruifeng@<i></i>upenn.edu']], 'Bilker': [['Ph.D.', 'Professor', 'warren@<i></i>upenn.edu']]}

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@<i></i>upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@<i></i>mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@<i></i>email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@<i></i>mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@<i></i>upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>{('Hongzhe', 'Li'): ['Ph.D', 'Professor', 'hongzhe@<i></i>upenn.edu'], ('Justine', 'Shults'): ['Ph.D.', 'Professor', 'jshults@<i></i>mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@<i></i>email.chop.edu']}

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>('Scarlett', 'Bellamy') ['Sc.D.', 'Associate Professor', 'bellamys@<i></i>mail.med.upenn.edu']

>('Warren', 'Bilker') ['Ph.D.', 'Professor', 'warren@<i></i>upenn.edu']

>('Matthew', 'Bryan') ['PhD', 'Assistant Professor', 'bryanma@<i></i>upenn.edu']

>('Jinbo', 'Chen') ['Ph.D.', 'Associate Professor', 'jinboche@<i></i>upenn.edu']

>('Jonas', 'Ellenberg') ['Ph.D.', 'Professor', 'jellenbe@<i></i>mail.med.upenn.edu']

>('Susan', 'Ellenberg') ['Ph.D.', 'Professor', 'sellenbe@<i></i>upenn.edu']

>('Rui', 'Feng') ['Ph.D', 'Assistant Professor', 'ruifeng@<i></i>upenn.edu']

>('Benjamin', 'French') ['PhD', 'Associate Professor', 'bcfrench@<i></i>mail.med.upenn.edu']

>('Phyllis', 'Gimotty') ['Ph.D', 'Professor', 'pgimotty@<i></i>upenn.edu']

>('Wensheng', 'Guo') ['Ph.D', 'Professor', 'wguo@<i></i>mail.med.upenn.edu']

>('Yenchih', 'Hsu') ['Ph.D.', 'Assistant Professor', 'hsu9@<i></i>mail.med.upenn.edu']

>('Rebecca', 'Hubbard') ['PhD', 'Associate Professor', 'rhubb@<i></i>mail.med.upenn.edu']

>('Wei-Ting', 'Hwang') ['Ph.D.', 'Associate Professor', 'whwang@<i></i>mail.med.upenn.edu']

>('Marshall', 'Joffe') ['MD MPH Ph.D', 'Professor', 'mjoffe@<i></i>mail.med.upenn.edu']

>('J.', 'Landis') ['B.S.Ed. M.S. Ph.D.', 'Professor', 'jrlandis@<i></i>mail.med.upenn.edu']

>('Yimei', 'Li') ['Ph.D.', 'Assistant Professor', 'liy3@<i></i>email.chop.edu']

>('Hongzhe', 'Li') ['Ph.D', 'Professor', 'hongzhe@<i></i>upenn.edu']

>('Mingyao', 'Li') ['Ph.D.', 'Associate Professor', 'mingyao@<i></i>mail.med.upenn.edu']

>('A.', 'Localio') ['JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@<i></i>upenn.edu']

>('Nandita', 'Mitra') ['Ph.D.', 'Associate Professor', 'nanditam@<i></i>mail.med.upenn.edu']

>('Knashawn', 'Morales') ['Sc.D.', 'Associate Professor', 'knashawn@<i></i>mail.med.upenn.edu']

>('Kathleen', 'Propert') ['Sc.D.', 'Professor', 'propert@<i></i>mail.med.upenn.edu']

>('Mary', 'Putt') ['PhD ScD', 'Professor', 'mputt@<i></i>mail.med.upenn.edu']

>('Sarah', 'Ratcliffe') ['Ph.D.', 'Associate Professor', 'sratclif@<i></i>upenn.edu']

>('Michelle', 'Ross') ['PhD', 'Assistant Professor', 'michross@<i></i>upenn.edu']

>('Jason', 'Roy') ['Ph.D.', 'Associate Professor', 'jaroy@<i></i>mail.med.upenn.edu']

>('Mary', 'Sammel') ['Sc.D.', 'Professor', 'msammel@<i></i>cceb.med.upenn.edu']

>('Pamela', 'Shaw') ['PhD', 'Assistant Professor', 'shawp@<i></i>upenn.edu']

>('Russell', 'Shinohara') ['0', 'Assistant Professor', 'rshi@<i></i>mail.med.upenn.edu']

>('Haochang', 'Shou') ['Ph.D.', 'Assistant Professor', 'hshou@<i></i>mail.med.upenn.edu']

>('Justine', 'Shults') ['Ph.D.', 'Professor', 'jshults@<i></i>mail.med.upenn.edu']

>('Alisa', 'Stephens') ['Ph.D.', 'Assistant Professor', 'alisaste@<i></i>mail.med.upenn.edu']

>('Andrea', 'Troxel') ['ScD', 'Professor', 'atroxel@<i></i>mail.med.upenn.edu']

>('Rui', 'Xiao') ['PhD', 'Assistant Professor', 'rxiao@<i></i>mail.med.upenn.edu']

>('Sharon', 'Xie') ['Ph.D.', 'Associate Professor', 'sxie@<i></i>mail.med.upenn.edu']

>('Dawei', 'Xie') ['PhD', 'Assistant Professor', 'dxie@<i></i>upenn.edu']

>('Wei', 'Yang') ['Ph.D.', 'Assistant Professor', 'weiyang@<i></i>mail.med.upenn.edu']

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

