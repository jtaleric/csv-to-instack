import csv
import json
import sys
import getopt
from collections import defaultdict

def main(argv):
    inputfile = None

    try:
        opts, args = getopt.getopt(argv,"c",["csv="])
    except :
        print " -csv <inputfile>"
        sys.exit(2)

    for opt, arg in opts:
       if opt == '-h':
           print ' - <inputfile>'
           sys.exit()
       elif opt in ("-c", "--csv"):
           inputfile = arg

    print "Opening %s" % inputfile
    csvFile =  open(inputfile)
    data = list(csv.reader(csvFile))
   
#   ['# mac', ' ipmi-addr', ' user', ' pass']
    
    jdata = defaultdict(list) 
    for value in data:
        jdata['nodes'].append({'pm_password' : value[3], 
        'pm_type' : value[4], 
        'mac' : [value[0]], 
        'cpu' : "foo", 
        'memory' : "foo", 
        'disk' : "foo", 
        'arch' : "foo", 
        'pm_user' : value[1], 
        'pm_addr' : value[2]})

    print json.dumps(jdata,indent=4, sort_keys=True) 

if __name__ == "__main__":
    main(sys.argv[1:])
