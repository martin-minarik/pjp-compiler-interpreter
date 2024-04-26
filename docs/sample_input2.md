# Sample2

## Sample Input

```
write "<Relational operators>";
write "1<5: ", 1 < 5;
write "1>3.5: ", 1 > 3.5;
write "aa==aa: ", "aa"=="aa";
write "aa==ab: ", "aa"=="ab";
write "aa!=ab: ", "aa"!="ab";
write "";
write "<Logic operators>";
write "false and true (false):", false && true;
write "false or true (true):", false || true;
write "not 1==2 (true):", !(1==2);
write "true or false and true (true):", true || false && true;
```

## Generated instructions

```
push S "<Relational operators>"
print 1
push S "1<5: "
push I 1
push I 5
lt
print 2
push S "1>3.5: "
push I 1
itof
push F 3.5
gt
print 2
push S "aa==aa: "
push S "aa"
push S "aa"
eq
print 2
push S "aa==ab: "
push S "aa"
push S "ab"
eq
print 2
push S "aa!=ab: "
push S "aa"
push S "ab"
eq
not
print 2
push S ""
print 1
push S "<Logic operators>"
print 1
push S "false and true (false):"
push B false
push B true
and
print 2
push S "false or true (true):"
push B false
push B true
or
print 2
push S "not 1==2 (true):"
push I 1
push I 2
eq
not
print 2
push S "true or false and true (true):"
push B true
push B false
push B true
and
or
print 2
```