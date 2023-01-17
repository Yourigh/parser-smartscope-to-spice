#parse export from smartscope fo format fo PWL in SPICE simulation.
#data need to be in the same folder as script with the name "source.csv"
import csv
print('start')
with open('pwl.txt', 'wb') as csvout:
    spamwriter = csv.writer(csvout, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    i = 0
    timestep = 0
    timestepnow = 0
    timestepnowstr = 'a'
    valA = 0
    #valB = 0
    with open('source.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            i = i + 1
            #print(', '.join(row))
            if i==2:
                print('Timescale [s]:',row[3])
                timestep = float(row[3])
            if i>2:
                valA = row[5]
                #valB = row[6] #use this value for channel B
                timestepnowstr = repr(timestepnow)
                spamwriter.writerow([timestepnowstr]+[valA]) #change here to B if channel B should be used. Also possible to add both A and B. 
                timestepnow = timestep + timestepnow
                #print ".", #indicate working, "," ensures no new line, slows down script
print('done')
print('Written lines:',i-2)