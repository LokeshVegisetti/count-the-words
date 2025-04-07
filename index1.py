
words="Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured object-oriented and functional programming. It is often described as a  language due to its comprehensive standard library Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python , released in 2008, was a major revision not"
now=words.split()
print("number of words:-" , len(now))
if len(now)>100:
    print("Valid")

else:
    print("invalid")


cap="HeloLofjsBNK"
upper=0
lower=0
for i in cap:
    if 65<ord(i)<91:
        upper+=1
    else:
        lower+=1

print("number of Uppercase letters", upper)
print("number of Lowercase letters", lower)
