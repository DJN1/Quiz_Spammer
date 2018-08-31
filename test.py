#Source: Mr. James
#Link to Quiz: https://goo.gl/forms/bHx4lCpiDDrVwWRv2

import time, random
from robobrowser import RoboBrowser

link = "https://docs.google.com/forms/d/e/1FAIpQLSePjmkcdap9qWg8xXObw8iVfSUY8Ty3GH0HtAZLHVV2yPmUiA/viewform"

stopwatch1 = time.ctime()

names = ["Ashton", "Yun Ya", "Asher", "Parrish", "Amelia", "Maya", "Mary Allen", "Anna-Julia", "Will", "Amrita", "Robyn", "Henry"]

br = RoboBrowser()

for q in range(100):
        name = names[random.randrange(0, (len(names)))]
        br.open(link)
        form = br.get_form()
        form['entry.845984078'] = name  #Name
        form['entry.1777217720'] = "Shrek"  #Themes
        print("Submitted: " + str(q + 1))
        br.submit_form(form)


stopwatch2 = time.ctime()
print("Start: " + stopwatch1 + ", End: " + stopwatch2)
total_time = int(stopwatch2[14:16])*60 + int(stopwatch2[17:19]) - int(stopwatch1[14:16])*60 - int(stopwatch1[17:19])
print(str(total_time))

