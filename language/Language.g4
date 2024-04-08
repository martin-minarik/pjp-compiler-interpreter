grammar Language;

// Lexer rules

fragment CHARACTER: [a-zA-Z];
INT_LITERAL: [1-9][0-9]* | '0';
FLOAT_LITERAL: [0-9]+ '.' [0-9]+;
BOOL_LITERAL: 'true' | 'false';
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
STRING_LITERAL: '"' (~["\\\r\n])* '"';
IDENTIFIER: CHARACTER (CHARACTER | [0-9])*;
WS: [ \t\r\n]+ -> skip;      // skip spaces, tabs, and newlines

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
MOD : '%';
CONCAT: '.';
EQUAL: '==';
NOTEQUAL: '!=';
AND: '&&';
OR: '||';
GT: '>';
LT: '<';

// Parser rules
program: (statement)+ EOF;

statement: ';'
         | declaration
         | expression ';'
         | read_statement
         | write_statement
         | block
         | conditional
         | while_loop
         | SINGLE_LINE_COMMENT;


declaration: type_keyword IDENTIFIER (',' IDENTIFIER)* ';';

read_statement: 'read' IDENTIFIER (',' IDENTIFIER)* ';';

write_statement: 'write' expression (',' expression)* ';';

block: '{' statement* '}';

conditional: 'if' '(' expression ')' statement ( 'else' statement )?;

while_loop: 'while' '(' expression ')' statement;

expression: prefix='-' expression # unaryMinus
          | prefix='!' expression # logicalNot
          | expression op=(MUL | DIV | MOD) expression # mulDivMod
          | expression op=(ADD | SUB | CONCAT) expression # addSubConcat
          | expression op=(LT | GT) expression # lesserGreater
          | expression op=(EQUAL | NOTEQUAL) expression # equalNotEqual
          | expression op=AND expression # logicalAnd
          | expression op=OR expression # logicalOr
          | INT_LITERAL # intLiteral
          | FLOAT_LITERAL # floatLiteral
          | BOOL_LITERAL # boolLiteral
          | STRING_LITERAL # stringLiteral
          | IDENTIFIER # id
          | '(' expression ')' # parentheses
          | <assoc=right> IDENTIFIER '=' expression # assignment
          ;

type_keyword: 'int' | 'float' | 'bool' | 'string';

