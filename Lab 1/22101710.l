%option noyywrap

%{
#include<bits/stdc++.h>

#include"symbol_info.h"

#define YYSTYPE symbol_info*

#include "y.tab.h"

extern YYSTYPE yylval;

using namespace std;

void yyerror(char *);


string loglist;

extern int lines;

extern ofstream outlog;

%}

/* Regular Definitions */

delim	 [ \t\v\r]

/* write regular expressions for whitespace and newline */
ws		 [ \t\r\f]+

newline  [\n]

letter_	 [A-Za-z_]
digit	 [0-9]

/* write regular expressions for id, float and integers */
id		[a-zA-Z_][a-zA-Z0-9_]*

float   {digit}*"."{digit}+([E|e][+|-]?{digit}+)?

integers {digit}+




%%

{ws}		{ /* ignore whitespace */ }
{newline}	{ /* do necessary bookkeeping (line number tracking etc.) */ 
                lines = lines + 1;
            }


if          { 
                loglist="Line no "+to_string(lines)+": Token <IF> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return IF; }


else          { 
                loglist="Line no "+to_string(lines)+": Token <ELSE> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return ELSE; }


for          { 
                loglist="Line no "+to_string(lines)+": Token <FOR> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return FOR; }


while       { 
                loglist="Line no "+to_string(lines)+": Token <WHILE> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return WHILE; }


do       { 
                loglist="Line no "+to_string(lines)+": Token <DO> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return DO; }


break       { 
                loglist="Line no "+to_string(lines)+": Token <BREAK> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return BREAK; }


int       { 
                loglist="Line no "+to_string(lines)+": Token <INT> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return INT; }


float       { 
                loglist="Line no "+to_string(lines)+": Token <FLOAT> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return FLOAT; }


char       { 
                loglist="Line no "+to_string(lines)+": Token <CHAR> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return CHAR; }


double       { 
                loglist="Line no "+to_string(lines)+": Token <DOUBLE> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return DOUBLE; }


void       { 
                loglist="Line no "+to_string(lines)+": Token <VOID> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return VOID; }


return       { 
                loglist="Line no "+to_string(lines)+": Token <RETURN> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return RETURN; }


switch       { 
                loglist="Line no "+to_string(lines)+": Token <SWITCH> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return SWITCH; }


case       { 
                loglist="Line no "+to_string(lines)+": Token <CASE> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return CASE; }


default       { 
                loglist="Line no "+to_string(lines)+": Token <DEFAULT> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return DEFAULT; }


continue       { 
                loglist="Line no "+to_string(lines)+": Token <CONTINUE> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return CONTINUE; }





printf       { 
                loglist="Line no "+to_string(lines)+": Token <PRINTLN> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return PRINTLN; }


"+"|"-"	    {
                symbol_info *s = new symbol_info((string)yytext,"ADDOP");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <ADDOP> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return ADDOP;
		    }

","        { 
                loglist="Line no "+to_string(lines)+": Token <COMMA> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return COMMA; }


"*"|"/"|"%"        { 
                symbol_info *s = new symbol_info((string)yytext,"MULOP");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <MULOP> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return MULOP; }


"++"|"--"        { 
                symbol_info *s = new symbol_info((string)yytext,"INCOP");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <INCOP> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return INCOP; }


"="        { 
                symbol_info *s = new symbol_info((string)yytext,"ASSIGNOP");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <ASSIGNOP> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return ASSIGNOP; }


"<"|">"|"=="|"<="|">="|"!="        { 
                symbol_info *s = new symbol_info((string)yytext,"RELOP");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <RELOP> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return RELOP; }


"&&"|"||"        { 
                symbol_info *s = new symbol_info((string)yytext,"LOGICOP");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <LOGICOP> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return LOGICOP; }


"!"        { 
                symbol_info *s = new symbol_info((string)yytext,"NOT");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <NOT> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return NOT; }


"("        { 
                symbol_info *s = new symbol_info((string)yytext,"LPAREN");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <LPAREN> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return LPAREN; }


")"        { 
                symbol_info *s = new symbol_info((string)yytext,"RPAREN");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <RPAREN> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return RPAREN; }


"{"        { 
                symbol_info *s = new symbol_info((string)yytext,"LCURL");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <LCURL> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return LCURL; }


"}"        { 
                symbol_info *s = new symbol_info((string)yytext,"RCURL");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <RCURL> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return RCURL; }


"["        { 
                symbol_info *s = new symbol_info((string)yytext,"LTHIRD");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <LTHIRD> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return LTHIRD; }


"]"        { 
                symbol_info *s = new symbol_info((string)yytext,"RTHIRD");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <RTHIRD> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return RTHIRD; }





";"        { 
                symbol_info *s = new symbol_info((string)yytext,"SEMICOLON");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <SEMICOLON> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return SEMICOLON; }



goto       { 
                loglist="Line no "+to_string(lines)+": Token <GOTO> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist; 
                return GOTO; }

":"        { 
                symbol_info *s = new symbol_info((string)yytext,"COLON");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <COLON> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;               
                return COLON; }




{id}       {
                symbol_info *s = new symbol_info((string)yytext,"ID");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <ID> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return ID;
            }
            

{float}       {
                symbol_info *s = new symbol_info((string)yytext,"CONST_FLOAT");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <CONST_FLOAT> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return CONST_FLOAT;
            }


{integers}       {
                symbol_info *s = new symbol_info((string)yytext,"CONST_INT");
                yylval = (YYSTYPE)s;
                loglist="Line no "+to_string(lines)+": Token <CONST_INT> Lexeme "+yytext+" found"+"\n\n";
			    outlog<<loglist;
                return CONST_INT;
            }
