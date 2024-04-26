# Sample3

## Sample Input

```
if (3<4) write "condition was true";
else write "condition was false";

if (true) {
	write "inside";
	write "second";
	write "if";
}

int a,b;

while(a<10) {
 write "a=",a;
 a=a+1;
}

a=0;

read b;

while(a<b) {
 write "a=",a,", b=",b;
 a=a+1;
}
```

## Generated instructions

```
push I 3
push I 4
lt
fjmp 0
push S "condition was true"
print 1
jmp 1
label 0
push S "condition was false"
print 1
label 1
push B true
fjmp 2
push S "inside"
print 1
push S "second"
print 1
push S "if"
print 1
jmp 3
label 2
label 3
push I 0
save a
push I 0
save b
label 4
load a 
push I 10
lt
fjmp 5
push S "a="
load a 
print 2
load a 
push I 1
add
save a
load a
pop
jmp 4
label 5
push I 0
save a
load a
pop
read I
save b
label 6
load a 
load b 
lt
fjmp 7
push S "a="
load a 
push S ", b="
load b 
print 4
load a 
push I 1
add
save a
load a
pop
jmp 6
label 7
```