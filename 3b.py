from difflib import SequenceMatcher
s1=input("enter the first string")
s2=input("enter the second string")
s3=input("enter the third string")
print(SequenceMatcher (None,s1,s2,s3).ratio())
