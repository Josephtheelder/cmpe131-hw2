test_str="A few months ago, I decided to deaccession an assortment of my things by whatever means feasible: selling, donating, recycling, giving them away, losing them on the subway, or reserving a spot for them on the next Mars Explorer.  gathered my unwanteds and piled them in the living room. A fraction of what was in that jumble: seven antique glass cake stands that belonged a  mother; a dormitory’s worth new sheet sets and blankets for a bed size that is not mine; a set of Lenox china that my grandmother gave to my mother, who gave it to me, and was never used; clothes galore; a Viking stove grate that arrived cracked, and which I saved because I planned to weld it into a sculpture someday, after I learned how to weld; several rolls of Trump toilet paper I wrongly thought were amusing a few years ago. I wish I could have added my boyfriend’s too large Le Corbusier lounger. (There are Web sites, such as NeverLikedItAnyway.com, that will buy your ex’s leavings, ranging from engagement rings to “Rick and Morty” socks.)"
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 

for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, "")
 

l=test_str.split()

dict1={}
for i in l:                           
  if i not in dict1:
    dict1[i]=1
  dict1[i]+=1

marklist = sorted(dict1.items(), key=lambda x:x[1],reverse=True)  
sortdict = dict(marklist)

j=0
for i in sortdict.keys():
  if j==5:
    break
  print(str(i)+": "+str(sortdict[i]))     
  j+=1
