(cd ..;ls *.py)| perl -ape 's/$/\ttk/' > l1;ls *.py | perl -ane 'if (/^wx_(\S+)/) {print($1,"\twx","\n")}' > l2; cat l1 l2 | sort | perl -ape 'if (/tk$/) {print("\n")}'
