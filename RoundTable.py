#Source: Mr. James 
#Link to Quiz: https://goo.gl/forms/bHx4lCpiDDrVwWRv2

import time, random
from robobrowser import RoboBrowser

link = "https://docs.google.com/forms/d/e/1FAIpQLScWszqzzaXkkkiWa8qZELiJlUjJERgB78HuT6r74OezmEDdOg/viewform"

stopwatch1 = time.ctime()

names = ["Ashton", "Yun Ya", "Asher", "Parrish", "Amelia", "Maya", "Mary Allen", "Anna-Julia", "Will", "Amrita", "Robyn"]

br = RoboBrowser()

for q in range(5):
        name = names[random.randrange(0, (len(names) - 1))]
        br.open(link)
        form = br.get_form()
        form['entry.879014250'] = name  #Name
        form['entry.1389478305'] = "Shrek"  #Themes
        print("Submitted")
        br.submit_form(form)


stopwatch2 = time.ctime()
print("Start: " + stopwatch1 + ", End: " + stopwatch2)
total_time = int(stopwatch2[14:16])*60 + int(stopwatch2[17:19]) - int(stopwatch1[14:16])*60 - int(stopwatch1[17:19])
print("That was fun. In the past " + str(total_time) + " seconds I learned the following:")

