%{

#include"symbol_info.h"

using namespace std;

#define YYSTYPE symbol_info*

int yyparse(void);
int yylex(void);

void yyerror(const char* s);

extern FILE *yyin;


ofstream outlog;

int lines = 1;

// declare any other variables or functions needed here

void generateLogGrammarRule(const string& rule, const string& source_rule, const string& source_text) {
    outlog << "At line no: " << lines << " " << rule << " : " << source_rule << " " << endl;
    outlog << endl;
    if (!source_text.empty()) {
        outlog << source_text << endl;
        outlog << endl;
    }
}


%}

%token IF ELSE FOR WHILE DO BREAK CONTINUE RETURN INT FLOAT CHAR VOID DOUBLE SWITCH CASE DEFAULT PRINTLN ADDOP MULOP INCOP DECOP RELOP ASSIGNOP LOGICOP NOT LPAREN RPAREN LCURL RCURL LTHIRD RTHIRD SEMICOLON COMMA GOTO COLON ID CONST_INT CONST_FLOAT

%nonassoc LOWER_THAN_ELSE
%nonassoc ELSE

%%

start : program
	{
		generateLogGrammarRule("start", "program", "");
		$$ = $1;
	}
	;

program : program unit
	{
		string source_text = $1->getname() + "\n" + $2->getname();
		$$ = new symbol_info(source_text, "program");
		generateLogGrammarRule("program", "program unit", source_text);
	}
	| unit
	{
		string source_text = $1->getname();
		$$ = new symbol_info(source_text, "program");
		generateLogGrammarRule("program", "unit", source_text);
	}
	;

unit : var_declaration
	{
		string source_text = $1->getname();
		$$ = new symbol_info(source_text, "unit");
		generateLogGrammarRule("unit", "var_declaration", source_text);		
	}
	| func_definition
	{
		string source_text = $1->getname();
		$$ = new symbol_info(source_text, "unit");
		generateLogGrammarRule("unit", "func_definition", source_text);		
	}
	;


parameter_list : parameter_list COMMA type_specifier ID
	{
		string source_text = $1->getname() + "," + $3->getname() + " " + $4->getname();
		$$ = new symbol_info(source_text, "param_list");
		generateLogGrammarRule("parameter_list", "parameter_list COMMA type_specifier ID", source_text);
	}
	| parameter_list COMMA type_specifier
	{
		string source_text = $1->getname() + "," + $3->getname();
		$$ = new symbol_info(source_text, "param_list");
		generateLogGrammarRule("parameter_list", "parameter_list COMMA type_specifier", source_text);
	}
	| type_specifier ID
	{
		string source_text = $1->getname() + " " + $2->getname();
		$$ = new symbol_info(source_text, "param_list");
		generateLogGrammarRule("parameter_list", "type_specifier ID", source_text);
	}
	| type_specifier
	{
		string source_text = $1->getname();
		$$ = new symbol_info(source_text, "param_list");
		generateLogGrammarRule("parameter_list", "type_specifier", source_text);
	}
	;

func_definition : type_specifier ID LPAREN parameter_list RPAREN compound_statement
	{	
		string source_text = $1->getname() + " " + $2->getname() + "(" + $4->getname() + ")\n" + $6->getname();
		$$ = new symbol_info(source_text, "func_def");
		generateLogGrammarRule("func_definition", "type_specifier ID LPAREN parameter_list RPAREN compound_statement", source_text);
	}
	| type_specifier ID LPAREN RPAREN compound_statement
	{
		
		string source_text = $1->getname() + " " + $2->getname() + "()\n" + $5->getname();
		$$ = new symbol_info(source_text, "func_def");
		generateLogGrammarRule("func_definition", "type_specifier ID LPAREN RPAREN compound_statement", source_text);	
	}
	;

compound_statement : LCURL statements RCURL
    {
        string sourceText = "{\n" + $2->getname() + "\n}";
        $$ = new symbol_info(sourceText, "compound_stmt");
        generateLogGrammarRule("compound_statement", "LCURL statements RCURL", sourceText);
    }
    | LCURL RCURL
    {
        string sourceText = "{\n}";
        $$ = new symbol_info(sourceText, "compound_stmt");
        generateLogGrammarRule("compound_statement", "LCURL RCURL", sourceText);
    }
    ;

var_declaration : type_specifier declaration_list SEMICOLON
    {
        string sourceText = $1->getname() + " " + $2->getname() + ";";
        $$ = new symbol_info(sourceText, "var_decl");
        generateLogGrammarRule("var_declaration", "type_specifier declaration_list SEMICOLON", sourceText);
    }
    ;

type_specifier : INT
    {
        string sourceText = "int";
        $$ = new symbol_info(sourceText, "type_spec");
        generateLogGrammarRule("type_specifier", "INT", sourceText);
    }
    | FLOAT
    {
        string sourceText = "float";
        $$ = new symbol_info(sourceText, "type_spec");
        generateLogGrammarRule("type_specifier", "FLOAT", sourceText);
    }
    | VOID
    {
        string sourceText = "void";
        $$ = new symbol_info(sourceText, "type_spec");
        generateLogGrammarRule("type_specifier", "VOID", sourceText);
    }
    ;

declaration_list : declaration_list COMMA ID
    {
        string sourceText = $1->getname() + "," + $3->getname();
        $$ = new symbol_info(sourceText, "decl_list");
        generateLogGrammarRule("declaration_list", "declaration_list COMMA ID", sourceText);
    }
    | declaration_list COMMA ID LTHIRD CONST_INT RTHIRD
    {
        string sourceText = $1->getname() + "," + $3->getname() + "[" + $5->getname() + "]";
        $$ = new symbol_info(sourceText, "decl_list");
        generateLogGrammarRule("declaration_list", "declaration_list COMMA ID LTHIRD CONST_INT RTHIRD", sourceText);
    }
    | ID
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "decl_list");
        generateLogGrammarRule("declaration_list", "ID", sourceText);
    }
    | ID LTHIRD CONST_INT RTHIRD
    {
        string sourceText = $1->getname() + "[" + $3->getname() + "]";
        $$ = new symbol_info(sourceText, "decl_list");
        generateLogGrammarRule("declaration_list", "ID LTHIRD CONST_INT RTHIRD", sourceText);
    }
    ;

statements : statement
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "stmts");
        generateLogGrammarRule("statements", "statement", sourceText);
    }
	| statements statement
    {
        string sourceText = $1->getname() + "\n" + $2->getname();
        $$ = new symbol_info(sourceText, "stmts");
        generateLogGrammarRule("statements", "statements statement", sourceText);
    }
    ;

statement : var_declaration
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "var_declaration", sourceText);
    }
    | expression_statement
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "expression_statement", sourceText);
    }
    | compound_statement
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "compound_statement", sourceText);
    }
    | FOR LPAREN expression_statement expression_statement expression RPAREN statement
    {
        string sourceText = "for(" + $3->getname() + $4->getname() + $5->getname() + ")\n" + $7->getname();
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "FOR LPAREN expression_statement expression_statement expression RPAREN statement", sourceText);
    }
    | IF LPAREN expression RPAREN statement %prec LOWER_THAN_ELSE
    {
        string sourceText = "if(" + $3->getname() + ")\n" + $5->getname();
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "IF LPAREN expression RPAREN statement", sourceText);
    }
    | IF LPAREN expression RPAREN statement ELSE statement
    {
        
        string elseStmt = $7->getname();
        size_t ifPos = elseStmt.find("if");
        
        string sourceText;
        if (ifPos == 0) 
        {
            
            sourceText = "if(" + $3->getname() + ")\n" + $5->getname() + "\nelse\n" + elseStmt;
        } 
        else 
        {
            
            sourceText = "if(" + $3->getname() + ")\n" + $5->getname() + "\nelse\n" + elseStmt;
        }
        
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "IF LPAREN expression RPAREN statement ELSE statement", sourceText);
    }
    | WHILE LPAREN expression RPAREN statement
    {
        string sourceText = "while(" + $3->getname() + ")\n" + $5->getname();
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "WHILE LPAREN expression RPAREN statement", sourceText);
    }
    | PRINTLN LPAREN ID RPAREN SEMICOLON
    {
        string sourceText = "printf(" + $3->getname() + ");";
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "PRINTLN LPAREN ID RPAREN SEMICOLON", sourceText);
    }
    | RETURN expression SEMICOLON
    {
        string sourceText = "return " + $2->getname() + ";";
        $$ = new symbol_info(sourceText, "stmt");
        generateLogGrammarRule("statement", "RETURN expression SEMICOLON", sourceText);
    }
    ;


expression_statement : SEMICOLON
    {
        string sourceText = ";";
        $$ = new symbol_info(sourceText, "expr_stmt");
        generateLogGrammarRule("expression_statement", "SEMICOLON", sourceText);
    }
    | expression SEMICOLON
    {
        string sourceText = $1->getname() + ";";
        $$ = new symbol_info(sourceText, "expr_stmt");
        generateLogGrammarRule("expression_statement", "expression SEMICOLON", sourceText);
    }
    ;

expression : logic_expression
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "expr");
        generateLogGrammarRule("expression", "logic_expression", sourceText);
    }
    | variable ASSIGNOP logic_expression
    {
        string sourceText = $1->getname() + "=" + $3->getname();
        $$ = new symbol_info(sourceText, "expr");
        generateLogGrammarRule("expression", "variable ASSIGNOP logic_expression", sourceText);
    }
    ;

logic_expression : rel_expression
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "logic_expr");
        generateLogGrammarRule("logic_expression", "rel_expression", sourceText);
    }
    | rel_expression LOGICOP rel_expression
    {
        string sourceText = $1->getname() + $2->getname() + $3->getname();
        $$ = new symbol_info(sourceText, "logic_expr");
        generateLogGrammarRule("logic_expression", "rel_expression LOGICOP rel_expression", sourceText);
    }
    ;

rel_expression : simple_expression
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "rel_expr");
        generateLogGrammarRule("rel_expression", "simple_expression", sourceText);
    }
    | simple_expression RELOP simple_expression
    {
        string sourceText = $1->getname() + $2->getname() + $3->getname();
        $$ = new symbol_info(sourceText, "rel_expr");
        generateLogGrammarRule("rel_expression", "simple_expression RELOP simple_expression", sourceText);
    }
    ;

simple_expression : term
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "simple_expr");
        generateLogGrammarRule("simple_expression", "term", sourceText);
    }
    | simple_expression ADDOP term
    {
        string sourceText = $1->getname() + $2->getname() + $3->getname();
        $$ = new symbol_info(sourceText, "simple_expr");
        generateLogGrammarRule("simple_expression", "simple_expression ADDOP term", sourceText);
    }
    ;

term : unary_expression
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "term");
        generateLogGrammarRule("term", "unary_expression", sourceText);
    }
    | term MULOP unary_expression
    {
        string sourceText = $1->getname() + $2->getname() + $3->getname();
        $$ = new symbol_info(sourceText, "term");
        generateLogGrammarRule("term", "term MULOP unary_expression", sourceText);
    }
    ;

unary_expression : factor
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "unary_expr");
        generateLogGrammarRule("unary_expression", "factor", sourceText);
    }
    | ADDOP unary_expression
    {
        string sourceText = $1->getname() + $2->getname();
        $$ = new symbol_info(sourceText, "unary_expr");
        generateLogGrammarRule("unary_expression", "ADDOP unary_expression", sourceText);
    }
    | NOT unary_expression
    {
        string sourceText = "!" + $2->getname();
        $$ = new symbol_info(sourceText, "unary_expr");
        generateLogGrammarRule("unary_expression", "NOT unary_expression", sourceText);
    }
    ;


factor : variable
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "variable", sourceText);
    }
    | ID LPAREN argument_list RPAREN
    {
        string sourceText = $1->getname() + "(" + $3->getname() + ")";
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "ID LPAREN argument_list RPAREN", sourceText);
    }
    | LPAREN expression RPAREN
    {
        string sourceText = "(" + $2->getname() + ")";
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "LPAREN expression RPAREN", sourceText);
    }
    | CONST_INT
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "CONST_INT", sourceText);
    }
    | CONST_FLOAT
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "CONST_FLOAT", sourceText);
    }
    | variable INCOP
    {
        string sourceText = $1->getname() + "++";
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "variable INCOP", sourceText);
    }
    | variable DECOP
    {
        string sourceText = $1->getname() + "--";
        $$ = new symbol_info(sourceText, "factor");
        generateLogGrammarRule("factor", "variable DECOP", sourceText);
    }
    ;

argument_list : arguments
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "arg_list");
        generateLogGrammarRule("argument_list", "arguments", sourceText);
    }
    |
    {
        string sourceText = "";
        $$ = new symbol_info(sourceText, "arg_list");
        generateLogGrammarRule("argument_list", "", sourceText);
    }
    ;

arguments : arguments COMMA logic_expression
    {
        string sourceText = $1->getname() + "," + $3->getname();
        $$ = new symbol_info(sourceText, "args");
        generateLogGrammarRule("arguments", "arguments COMMA logic_expression", sourceText);
    }
    | logic_expression
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "args");
        generateLogGrammarRule("arguments", "logic_expression", sourceText);
    }
    ;

variable : ID
    {
        string sourceText = $1->getname();
        $$ = new symbol_info(sourceText, "var");
        generateLogGrammarRule("variable", "ID", sourceText);
    }
    | ID LTHIRD expression RTHIRD
    {
        string sourceText = $1->getname() + "[" + $3->getname() + "]";
        $$ = new symbol_info(sourceText, "var");
        generateLogGrammarRule("variable", "ID LTHIRD expression RTHIRD", sourceText);
    }
    ;


%%

void yyerror(const char *s) {
    cerr << "Error: " << s << endl;
}

int main(int argc, char *argv[])
{
	if(argc != 2) 
	{
        // check if filename given
        cout << "Usage: " << argv[0] << " <input_file>" << endl;
        return 0;		
	}
	yyin = fopen(argv[1], "r");
	outlog.open("output_log.txt", ios::trunc);
	
	if(yyin == NULL)
	{
		cout<<"Couldn't open file"<<endl;
		return 0;
	}
    
	yyparse();
	
	//print number of lines
    outlog << "\nTotal lines: " << lines << endl;

	outlog.close();
	
	fclose(yyin);
	
	return 0;
}
