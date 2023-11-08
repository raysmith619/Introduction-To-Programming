#fstring_ex1.py 05-Nov-2019
# F-string example

runners =   {
                "tom" : {   "count" : 5,
                            "time" : 3.8
                        },

                "joe" : {   "count" : 7,
                            "time" : 5.728
                        },

                "mary" :{   "count" : 10,
                            "time" : 7.62
                        }
            }

print(f"{'name':10} {'count':5}"
      + f"{'time':>5}")  # Heading
for rname in runners:
    info = runners[rname]
    print(f"{rname:10} {info['count']:5d}"
          + f" {info['time']:5.3f}")
                    
           

