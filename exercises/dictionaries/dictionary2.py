#dictionary2.py 03Oct2021  crs, from slide 3
#
#Dictionary  - Group of values - Access by key
trades_d = { 
    "painter" : "tom",
    "landscaper" : "joe",
    "plumber" : "kate"
    }
print("landscaper:", trades_d["landscaper"])
print("\nTrades Folks")
print("painter:", trades_d["painter"])
for trade in trades_d:
    print(trade,":", trades_d[trade])
    
print("\nUsing items()")
for trade, who in trades_d.items():
    print(trade, who)

print("\nadding dictionary member")
trades_d["programmer"] = "ray"
for trade, who in trades_d.items():
    print(trade, ": ", who, sep="")
    
print("\nTesting for dictionary membership")
if "programmer" in trades_d:
    print("We have a programmer", end=":")
    print(trades_d["programmer"])

