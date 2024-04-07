grammar Language;

// Lexer rules

fragment CHARACTER: [a-zA-Z];
INT_LITERAL: [1-9][0-9]* | '0';
FLOAT_LITERAL: [0-9]+ '.' [0-9]+;
BOOL_LITERAL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;      // skip spaces, tabs, and newlines
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
STRING_LITERAL: '"' (~["\\\r\n])* '"';
TYPE: 'int' | 'float' | 'bool' | 'string';
IDENTIFIER: CHARACTER (CHARACTER | [0-9])*;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
MOD : '%';
CONCAT: '.';


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


declaration: TYPE IDENTIFIER (',' IDENTIFIER)* ';';

read_statement: 'read' IDENTIFIER (',' IDENTIFIER)* ';';

write_statement: 'write' expression (',' expression)* ';';

block: '{' statement* '}';

conditional: 'if' '(' expression ')' statement ( 'else' statement )?;

while_loop: 'while' '(' expression ')' statement;

expression: prefix='-' expression
          | prefix='!' expression
          | expression op=(MUL | DIV | MOD) expression
          | expression op=(ADD | SUB | CONCAT) expression
          | expression op=('<' | '>') expression
          | expression op=('==' | '!=') expression
          | expression op='&&' expression
          | expression op='||' expression
          | '(' expression ')'
          | assignment
          | IDENTIFIER
          | literal;

assignment: IDENTIFIER '=' expression;

literal: FLOAT_LITERAL | INT_LITERAL | BOOL_LITERAL | STRING_LITERAL;