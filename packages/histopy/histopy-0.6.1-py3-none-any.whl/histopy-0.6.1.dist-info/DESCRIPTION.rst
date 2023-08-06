# Histopy

BASH-style history for the Python3 interactive interpreter.

Daniel W. Paley, 2018.  
Contact: dwpaley@gmail.com  
Github: https://github.com/dwpaley/histopy  


Quickstart: 
* >>> import histopy as hp
* >>> hp.history_full()     # like $ history
* >>> hp.history()          # history of current session
* >>> hp.recall(n)          # like $ !n

Known issues:
* recall_range(n1, n2) doesn't attempt to handle any exceptions. Would be nice
to prompt e.g. "recall_range stopped with exception ... on line ... Continue 
on line ...?"


