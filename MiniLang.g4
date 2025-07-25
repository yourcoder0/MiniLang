grammar MiniLang;

program: statement*;

statement
    : varDecl
    | assignStmt
    | exprStmt
    | ifStmt
    | whileStmt
    | functionDecl
    | printStmt
    ;

varDecl: 'int' ID '=' expr ';';
assignStmt: ID '=' expr ';';
exprStmt: expr ';';

ifStmt: 'if' '(' expr ')' '{' statement* '}' ;
whileStmt: 'while' '(' expr ')' '{' statement* '}' ;
printStmt: 'print' '(' expr ')' ';' ;

functionDecl: 'func' ID '(' ')' '{' statement* 'return' expr ';' '}' ;
funcCall: ID '(' ')' ;

expr
    : expr op=('==' | '!=' | '<' | '>' | '<=' | '>=') expr   # compExpr
    | expr op=('+'|'-') expr                                 # addExpr
    | expr op=('*'|'/') expr                                 # mulExpr
    | funcCall                                               # functionCall
    | '(' expr ')'                                           # parens
    | ID                                                     # variable
    | NUMBER                                                 # number
    | STRING                                                 # string
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
STRING: '"' .*? '"';

LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
