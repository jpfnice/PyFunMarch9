import math
# Creation:

name="Julia" # len() for in [] [:]
name='Julia'
line='a long string .....\
end of string'
print(line)

line='''a long string .....

end of string'''

print(line)
line="""a long string .....

end of string"""

print(line)
text="line1\nline2\n\tline3" # \f \b \a
print(text)

f1="/var/log/messages" # linux or MacOs

f1="c:\temp\new.txt" # windows syntax
print(f1)
f1="c:\\temp\\new.txt" # windows syntax
print(f1)
f1= r"c:\temp\new.txt" # a raw
print(f1)
f1="c:/temp/new.txt" # windows syntax
print(f1)
nb=12*3.4

f1= f"nb {nb} nb**2 {nb**2} sqrt(nb) {math.sqrt(nb)}"
print(f1)

f1= f"nb {nb} nb**2 {nb**2:.3f} sqrt(nb) {math.sqrt(nb):.3f}"
print(f1)

f1=str(34.5*67.7)
print(f1, type(f1))
