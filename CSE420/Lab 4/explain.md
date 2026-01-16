# Explanation of Abstract Syntax Tree (AST) Implementation

This document explains the implementation of the Abstract Syntax Tree (AST) for the C subset as per Task 2.1. The AST is built during the parsing phase and then traversed to generate three-address code. The implementation is divided into several parts, each representing a different type of node in the AST.

## 2.1.2 ExprNode Classes

`ExprNode` is a base class for all expression nodes in the AST. It inherits from `ASTNode` and represents expressions that have a value.

### `ExprNode`

#### Code

```cpp
// From ast.h
class ExprNode : public ASTNode {
protected:
    string node_type;
public:
    ExprNode(string type) : node_type(type) {}
    virtual string get_type() const { return node_type; }
};
```

#### Explanation

- **`class ExprNode : public ASTNode`**: This declares the `ExprNode` class, which inherits publicly from `ASTNode`.
- **`protected: string node_type;`**: This stores the data type of the expression (e.g., "int", "float").
- **`ExprNode(string type) : node_type(type) {}`**: The constructor initializes the `node_type`.
- **`virtual string get_type() const`**: A virtual function to get the type of the expression.

---

### `VarNode`

`VarNode` represents a variable reference in the code. It can also handle array indexing.

#### Code

```cpp
// From ast.h
class VarNode : public ExprNode {
private:
    string name;
    ExprNode* index;

public:
    VarNode(string name, string type, ExprNode* idx = nullptr)
        : ExprNode(type), name(name), index(idx) {}
    
    ~VarNode() { if(index) delete index; }
    
    bool has_index() const { return index != nullptr; }
    
    string generate_index_code(...) const {
        if (!index) return "";
        return index->generate_code(...);
    }
    
    string generate_code(...) const override {
        if (symbol_to_temp.find(name) != symbol_to_temp.end()) {
            return symbol_to_temp[name];
        }

        string result_temp = "t" + to_string(temp_count++);
        
        if (!has_index()) {
            outcode << result_temp << " = " << name << "\n";
        } else {
            string index_temp = generate_index_code(...);
            outcode << result_temp << " = " << name << "[" << index_temp << "]\n";
        }
        
        return result_temp;
    }
    
    string get_name() const { return name; }
};
```

```yacc
// From 22101710.y
variable : id_name
    {
        // ... (error checking) ...
        // Create AST node for variable
		VarNode* varNode = new VarNode($1->getname(), $$->getvartype());
		$$->set_ast_node(varNode);
	 }
	 | id_name LTHIRD expression RTHIRD 
	 {
	 	// ... (error checking) ...
		// Create AST node for array access
		VarNode* varNode = new VarNode($1->getname(), $$->getvartype(), (ExprNode*)$3->get_ast_node());
		$$->set_ast_node(varNode);
	 }
```

#### Explanation

- **`class VarNode : public ExprNode`**: `VarNode` inherits from `ExprNode`.
- **`string name;`**: Stores the name of the variable.
- **`ExprNode* index;`**: A pointer to an `ExprNode` representing the array index (if it's an array access).
- **`VarNode(string name, string type, ExprNode* idx = nullptr)`**: The constructor initializes the variable's name, type, and optional index.
- **`generate_code(...)`**:
    1. It first checks if the variable is already associated with a temporary variable.
    2. If not, it creates a new temporary variable (e.g., `t0`).
    3. If it's a simple variable, it generates code like `t0 = x`.
    4. If it's an array access, it first generates the code for the index expression and then generates code like `t0 = x[t1]`.
    5. It returns the name of the temporary variable holding the value.
- **In `22101710.y`**: `VarNode` objects are created in the `variable` grammar rule. When a simple `ID` is encountered, a `VarNode` is created. When an array access like `ID[expression]` is parsed, a `VarNode` is created with the `index` pointer pointing to the AST node of the `expression`.

---

### `ConstNode`

`ConstNode` represents a constant value (integer or float).

#### Code

```cpp
// From ast.h
class ConstNode : public ExprNode {
private:
    string value;

public:
    ConstNode(string val, string type) : ExprNode(type), value(val) {}
    
    string generate_code(...) const override {
        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = " << value << "\n";
        return result_temp;
    }
};
```

```yacc
// From 22101710.y
factor	: ...
	| CONST_INT 
	{
		// ...
		// Create AST node for integer constant
		ConstNode* intNode = new ConstNode($1->getname(), "int");
		$$->set_ast_node(intNode);
	}
	| CONST_FLOAT
	{
		// ...
		// Create AST node for float constant
		ConstNode* floatNode = new ConstNode($1->getname(), "float");
		$$->set_ast_node(floatNode);
	}
```

#### Explanation

- **`class ConstNode : public ExprNode`**: `ConstNode` inherits from `ExprNode`.
- **`string value;`**: Stores the string representation of the constant value.
- **`ConstNode(string val, string type)`**: The constructor initializes the value and type.
- **`generate_code(...)`**: This method generates three-address code to assign the constant value to a new temporary variable. For example, `t0 = 5`.
- **In `22101710.y`**: `ConstNode` objects are created in the `factor` grammar rule when a `CONST_INT` or `CONST_FLOAT` token is parsed.

---

### `BinaryOpNode`

`BinaryOpNode` represents a binary operation (e.g., +, -, *, /, <, &&).

#### Code

```cpp
// From ast.h
class BinaryOpNode : public ExprNode {
private:
    string op;
    ExprNode* left;
    ExprNode* right;

public:
    BinaryOpNode(string op, ExprNode* left, ExprNode* right, string result_type)
        : ExprNode(result_type), op(op), left(left), right(right) {}
    
    ~BinaryOpNode() {
        delete left;
        delete right;
    }
    
    string generate_code(...) const override {
        string left_temp = left->generate_code(...);
        string right_temp = right->generate_code(...);
        
        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = " << left_temp << " " << op << " " << right_temp << "\n";
        return result_temp;
    }
};
```

```yacc
// From 22101710.y
simple_expression : simple_expression ADDOP term 
    {
        // ...
        // Create AST node for addition/subtraction
        BinaryOpNode* addopNode = new BinaryOpNode(
            $2->getname(),
            (ExprNode*)$1->get_ast_node(),
            (ExprNode*)$3->get_ast_node(),
            $$->getvartype()
        );
        $$->set_ast_node(addopNode);
    }
```

#### Explanation

- **`class BinaryOpNode : public ExprNode`**: Inherits from `ExprNode`.
- **`string op; ExprNode* left; ExprNode* right;`**: Stores the operator and pointers to the left and right operand expressions.
- **`generate_code(...)`**:
    1. It recursively calls `generate_code()` on the left and right children to get the temporary variables holding their results (e.g., `t0` and `t1`).
    2. It creates a new temporary variable (`t2`).
    3. It generates the code for the binary operation, like `t2 = t0 + t1`.
    4. It returns the name of the result temporary variable (`t2`).
- **In `22101710.y`**: `BinaryOpNode`s are created in rules for binary operations like `simple_expression`, `term`, `rel_expression`, and `logic_expression`. The left and right operands' AST nodes are passed to the `BinaryOpNode` constructor.

---

### `UnaryOpNode`

`UnaryOpNode` represents a unary operation (e.g., -, !).

#### Code

```cpp
// From ast.h
class UnaryOpNode : public ExprNode {
private:
    string op;
    ExprNode* expr;

public:
    UnaryOpNode(string op, ExprNode* expr, string result_type)
        : ExprNode(result_type), op(op), expr(expr) {}
    
    ~UnaryOpNode() { delete expr; }
    
    string generate_code(...) const override {
        string expr_temp = expr->generate_code(...);
        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = " << op << expr_temp << "\n";
        return result_temp;
    }
};
```

```yacc
// From 22101710.y
unary_expression : ADDOP unary_expression
    {
        // ...
        // Create AST node for unary plus/minus
        UnaryOpNode* unaryNode = new UnaryOpNode(
            $1->getname(),
            (ExprNode*)$2->get_ast_node(),
            $$->getvartype()
        );
        $$->set_ast_node(unaryNode);
    }
```

#### Explanation

- **`class UnaryOpNode : public ExprNode`**: Inherits from `ExprNode`.
- **`string op; ExprNode* expr;`**: Stores the operator and a pointer to the operand expression.
- **`generate_code(...)`**:
    1. It recursively calls `generate_code()` on its child expression to get the temporary variable for the operand's value (`t0`).
    2. It creates a new temporary variable (`t1`).
    3. It generates the code for the unary operation, like `t1 = -t0`.
    4. It returns the name of the result temporary variable (`t1`).
- **In `22101710.y`**: `UnaryOpNode`s are created in the `unary_expression` rule for unary minus and logical NOT.

---

### `AssignNode`

`AssignNode` represents an assignment operation.

#### Code

```cpp
// From ast.h
class AssignNode : public ExprNode {
private:
    VarNode* lhs;
    ExprNode* rhs;

public:
    AssignNode(VarNode* lhs, ExprNode* rhs, string result_type)
        : ExprNode(result_type), lhs(lhs), rhs(rhs) {}
    
    ~AssignNode() {
        delete lhs;
        delete rhs;
    }
    
    string generate_code(...) const override {
        string rhs_temp = rhs->generate_code(...);

        if(lhs->has_index()) {
            string index_temp = lhs->generate_index_code(...);
            outcode << lhs->get_name() << "[" << index_temp << "] = " << rhs_temp << "\n";
        } else {
            outcode << lhs->get_name() << " = " << rhs_temp << "\n";
        }
        return rhs_temp;
    }
};
```

```yacc
// From 22101710.y
expression : variable ASSIGNOP logic_expression
    {
        // ...
        // Create AST node for assignment
        AssignNode* assignNode = new AssignNode(
            (VarNode*)$1->get_ast_node(),
            (ExprNode*)$3->get_ast_node(),
            $$->getvartype()
        );
        $$->set_ast_node(assignNode);
    }
```

#### Explanation

- **`class AssignNode : public ExprNode`**: Inherits from `ExprNode`.
- **`VarNode* lhs; ExprNode* rhs;`**: Stores pointers to the left-hand side (a `VarNode`) and the right-hand side (an `ExprNode`).
- **`generate_code(...)`**:
    1. It generates the code for the right-hand side expression to get its value into a temporary variable (`t0`).
    2. It then generates the assignment code.
    3. If the LHS is a simple variable, it generates `x = t0`.
    4. If the LHS is an array element, it generates code for the index and then `x[t1] = t0`.
- **In `22101710.y`**: An `AssignNode` is created in the `expression` rule for assignment. The `VarNode` from the `variable` rule and the `ExprNode` from the `logic_expression` are used as its children.

---

### `FuncCallNode`

`FuncCallNode` represents a function call.

#### Code

```cpp
// From ast.h
class FuncCallNode : public ExprNode {
private:
    string func_name;
    vector<ExprNode*> arguments;

public:
    FuncCallNode(string name, string result_type)
        : ExprNode(result_type), func_name(name) {}
    
    ~FuncCallNode() {
        for (auto arg : arguments) {
            delete arg;
        }
    }
    
    void add_argument(ExprNode* arg) {
        if (arg) arguments.push_back(arg);
    }
    
    string generate_code(...) const override {
        vector<string> arg_temps;
        
        for (auto arg : arguments) {
            string arg_temp = arg->generate_code(...);
            arg_temps.push_back(arg_temp);
        }

        for (size_t i = 0; i < arg_temps.size(); i++) {
            outcode << "param " << arg_temps[i] << "\n";
        }

        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = call " << func_name << ", " << arg_temps.size() << "\n";
        return result_temp;
    }
};
```

```yacc
// From 22101710.y
factor : id_name LPAREN argument_list RPAREN
    {
        // ...
        // Create function call node
	    FuncCallNode* funcCall = new FuncCallNode($1->getname(), $$->getvartype());
	
	    if ($3->get_ast_node()) {
	        ArgumentsNode* argsNode = dynamic_cast<ArgumentsNode*>($3->get_ast_node());
	        if (argsNode) {
	            for (auto arg : argsNode->get_arguments()) {
	                funcCall->add_argument(arg);
	            }
	        }
	    }
	
	    $$->set_ast_node(funcCall);
    }
```

#### Explanation

- **`class FuncCallNode : public ExprNode`**: Inherits from `ExprNode`.
- **`string func_name; vector<ExprNode*> arguments;`**: Stores the function name and a vector of `ExprNode` pointers for the arguments.
- **`generate_code(...)`**:
    1. It iterates through each argument expression, recursively calling `generate_code()` to evaluate them and get their temporary variable names.
    2. It then generates `param` instructions for each argument (e.g., `param t0`, `param t1`).
    3. It creates a new temporary variable for the return value (`t2`).
    4. It generates the `call` instruction, like `t2 = call my_func, 2`.
    5. It returns the name of the temporary variable holding the return value.
- **In `22101710.y`**: A `FuncCallNode` is created in the `factor` rule for a function call. It parses the arguments (using an intermediate `ArgumentsNode`) and adds them to the `FuncCallNode`.

## 2.1.3 StmtNode Classes

`StmtNode` is the base class for all statement nodes in the AST. It inherits from `ASTNode`.

### `StmtNode`

#### Code
```cpp
// From ast.h
class StmtNode : public ASTNode {
public:
    virtual string generate_code(...) const = 0;
};
```

#### Explanation
- **`class StmtNode : public ASTNode`**: This declares the `StmtNode` class, which inherits publicly from `ASTNode`. It serves as an abstract base class for all statement types.
- **`virtual string generate_code(...) const = 0;`**: Like in `ASTNode`, this is a pure virtual function that requires derived statement nodes to implement their own code generation logic.

---

### `ExprStmtNode`
`ExprStmtNode` represents a statement that consists of a single expression, like `x = y + 1;` or `my_func();`.

#### Code
```cpp
// From ast.h
class ExprStmtNode : public StmtNode {
private:
    ExprNode* expr;
public:
    ExprStmtNode(ExprNode* e) : expr(e) {}
    ~ExprStmtNode() { if(expr) delete expr; }
    
    string generate_code(...) const override {
        if (expr) {
            return expr->generate_code(...);
        }
        return "";
    }
};
```
```yacc
// From 22101710.y
expression_statement : expression SEMICOLON 
    {
        // ...
        // Create expression statement from expression
        ExprStmtNode* exprStmt = new ExprStmtNode((ExprNode*)$1->get_ast_node());
        $$->set_ast_node(exprStmt);
    }
```

#### Explanation
- **`class ExprStmtNode : public StmtNode`**: Inherits from `StmtNode`.
- **`ExprNode* expr;`**: A pointer to the `ExprNode` that this statement wraps.
- **`generate_code(...)`**: It simply calls the `generate_code()` method of the contained expression. The result of the expression is often unused (e.g., in a function call statement), but the code is generated nonetheless.
- **In `22101710.y`**: An `ExprStmtNode` is created in the `expression_statement` rule, wrapping the AST node of the parsed `expression`.

---

### `BlockNode`
`BlockNode` represents a compound statement or a block of code enclosed in curly braces `{}`.

#### Code
```cpp
// From ast.h
class BlockNode : public StmtNode {
private:
    vector<StmtNode*> statements;
public:
    ~BlockNode() {
        for (auto stmt : statements) {
            delete stmt;
        }
    }
    
    void add_statement(StmtNode* stmt) {
        if (stmt) statements.push_back(stmt);
    }
    
    string generate_code(...) const override {
        string result;
        for (auto stmt : statements) {
            result = stmt->generate_code(...);
        }
        return result;
    }
};
```
```yacc
// From 22101710.y
statements : statements statement
    {
        // ...
        // Update block with new statement
        BlockNode* block = (BlockNode*)$1->get_ast_node();
        if($2->get_ast_node()) {
            block->add_statement((StmtNode*)$2->get_ast_node());
        }
        $$->set_ast_node(block);
    }
```

#### Explanation
- **`class BlockNode : public StmtNode`**: Inherits from `StmtNode`.
- **`vector<StmtNode*> statements;`**: A vector to hold a sequence of `StmtNode` pointers, representing the statements within the block.
- **`add_statement(StmtNode* stmt)`**: A helper method to add a statement to the block.
- **`generate_code(...)`**: It iterates through its list of statements and calls `generate_code()` on each one in sequence.
- **In `22101710.y`**: `BlockNode`s are built up in the `statements` rule. As more statements are parsed, they are added to the `BlockNode` of the preceding statements.

---

### `DeclNode`
`DeclNode` represents a variable declaration.

#### Code
```cpp
// From ast.h
class DeclNode : public StmtNode {
private:
    string type;
    vector<pair<string, int>> vars;

public:
    DeclNode(string t) : type(t) {}
    
    void add_var(string name, int array_size = 0) {
        vars.push_back(make_pair(name, array_size));
    }
    
    string generate_code(...) const override {
        for (const auto& var : vars) {
            if (var.second == 0) {
                outcode << "// Declaration: " << type << " " << var.first << "\n";
            } else {
                outcode << "// Declaration: " << type << " " << var.first << "[" << var.second << "]\n";
            }
        }
        return "";
    }
};
```
```yacc
// From 22101710.y
var_declaration : type_specifier declaration_list SEMICOLON
    {
        // ...
        // Create AST node for variable declaration
        DeclNode* declNode = new DeclNode($1->getname());
        
        // Parse the varlist to add variables to the declaration node
        // ...
        
        $$->set_ast_node(declNode);
    }
```

#### Explanation
- **`class DeclNode : public StmtNode`**: Inherits from `StmtNode`.
- **`string type; vector<pair<string, int>> vars;`**: Stores the data type and a list of variables being declared (with their names and array sizes, if applicable).
- **`generate_code(...)`**: For this implementation, the `DeclNode`'s code generation simply writes a comment to the output file indicating the declaration. No actual executable three-address code is generated for a declaration itself.
- **In `22101710.y`**: A `DeclNode` is created for a `var_declaration`. The `declaration_list` is parsed to add each variable to the `DeclNode`.

---

### `IfNode`

`IfNode` represents an if-else statement.

#### Code

```cpp
// From ast.h
class IfNode : public StmtNode {
private:
    ExprNode* condition;
    StmtNode* then_block;
    StmtNode* else_block;

public:
    IfNode(ExprNode* cond, StmtNode* then_stmt, StmtNode* else_stmt = nullptr)
        : condition(cond), then_block(then_stmt), else_block(else_stmt) {}
    
    string generate_code(...) const override {
        string label_then = "L" + to_string(label_count++);
        string label_else = "L" + to_string(label_count++);
        string label_end = "L" + to_string(label_count++);

        string cond_temp = condition->generate_code(...);
        
        outcode << "if " << cond_temp << " goto " << label_then << "\n";
        outcode << "goto " << label_else << "\n";
                            
        outcode << label_then << ":\n";
        if (then_block) {
            then_block->generate_code(...);
        }

        outcode << "goto " << label_end << "\n";

        outcode << label_else << ":\n";
        if (else_block) {
            else_block->generate_code(...);
        }

        outcode << label_end << ":\n";
        return "";
    }
};
```

```yacc
// From 22101710.y
statement : IF LPAREN expression RPAREN statement ELSE statement
    {
        // ...
        // Create AST node for if-else statement
        IfNode* ifNode = new IfNode(
            (ExprNode*)$3->get_ast_node(),
            (StmtNode*)$5->get_ast_node(),
            (StmtNode*)$7->get_ast_node()
        );
        $$->set_ast_node(ifNode);
    }
```

#### Explanation
- **`generate_code(...)`**:
    1. It generates three new labels: one for the `then` block (`L1`), one for the `else` block (`L2`), and one for the end of the statement (`L3`).
    2. It generates the code for the `condition` expression, getting the result in a temporary variable (`t0`).
    3. It generates a conditional jump: `if t0 goto L1`.
    4. It generates an unconditional jump to the `else` block: `goto L2`.
    5. It emits the `then` label (`L1:`), generates the code for the `then_block`, and then an unconditional jump to the end: `goto L3`.
    6. It emits the `else` label (`L2:`) and generates the code for the `else_block` (if it exists).
    7. Finally, it emits the end label (`L3:`).

---

### `WhileNode`

`WhileNode` represents a while loop.

#### Code

```cpp
// From ast.h
class WhileNode : public StmtNode {
private:
    ExprNode* condition;
    StmtNode* body;
public:
    WhileNode(ExprNode* cond, StmtNode* body_stmt)
        : condition(cond), body(body_stmt) {}
    
    string generate_code(...) const override {
        string label_start = "L" + to_string(label_count++);
        string label_body = "L" + to_string(label_count++);
        string label_end = "L" + to_string(label_count++);

        outcode << label_start << ":\n";

        string cond_temp = condition->generate_code(...);
        outcode << "if " << cond_temp << " goto " << label_body << "\n";
        outcode << "goto " << label_end << "\n";

        outcode << label_body << ":\n";
        if (body) {
            body->generate_code(...);
        }
        
        outcode << "goto " << label_start << "\n";

        outcode << label_end << ":\n";
        return "";
    }
};
```

#### Explanation
- **`generate_code(...)`**:
    1. It generates three labels: for the start of the loop (`L1`), the loop body (`L2`), and the end of the loop (`L3`).
    2. It emits the `start` label (`L1:`).
    3. It generates the code for the `condition` and a conditional jump to the body: `if t0 goto L2`.
    4. It generates an unconditional jump to the end if the condition is false: `goto L3`.
    5. It emits the `body` label (`L2:`), generates the code for the loop's `body`, and then jumps back to the start: `goto L1`.
    6. It emits the `end` label (`L3:`).

---

### `ForNode`

`ForNode` represents a for loop.

#### Code

```cpp
// From ast.h
class ForNode : public StmtNode {
private:
    ExprNode* init;
    ExprNode* condition;
    ExprNode* update;
    StmtNode* body;
public:
    ForNode(ExprNode* init_expr, ExprNode* cond_expr, ExprNode* update_expr, StmtNode* body_stmt)
        : init(init_expr), condition(cond_expr), update(update_expr), body(body_stmt) {}
    
    string generate_code(...) const override {
        if (init) {
            init->generate_code(...);
        }

        string label_start = "L" + to_string(label_count++);
        string label_body = "L" + to_string(label_count++);
        string label_end = "L" + to_string(label_count++);

        outcode << label_start << ":\n";
        if (condition) {
            string cond_result = condition->generate_code(...);
            outcode << "if " << cond_result << " goto " << label_body << "\n";
            outcode << "goto " << label_end << "\n";
        }

        outcode << label_body << ":\n";
        if (body) {
            body->generate_code(...);
        }
        
        if (update) {
            update->generate_code(...);
        }

        outcode << "goto " << label_start << "\n";

        outcode << label_end << ":\n";
        return "";
    }
};
```

#### Explanation
- **`generate_code(...)`**: The logic is very similar to a `while` loop, but with extra steps for the initialization and update expressions.
    1. It generates code for the `init` expression first.
    2. It sets up labels for the loop check, body, and end.
    3. In the loop check section, it evaluates the `condition` and jumps to the body or the end.
    4. In the body section, it generates the code for the `body` statement, and then generates the code for the `update` expression.
    5. It then jumps back to the loop check.

---

### `ReturnNode`

`ReturnNode` represents a return statement.

#### Code

```cpp
// From ast.h
class ReturnNode : public StmtNode {
private:
    ExprNode* expr;
public:
    ReturnNode(ExprNode* e) : expr(e) {}
    ~ReturnNode() { if (expr) delete expr; }
    
    string generate_code(...) const override {
        string expr_temp = expr ? expr->generate_code(...) : "";
        outcode << "return " << expr_temp << "\n";
        return expr_temp;
    }
};
```

#### Explanation
- **`generate_code(...)`**:
    1. It generates the code for the return `expr` (if one exists) and gets the result in a temporary variable (`t0`).
    2. It generates a `return` instruction, either with the temporary variable (`return t0`) or without one (`return`) for a void function.
## 2.1.4 ProgramNode

`ProgramNode` is the root of the AST, representing the entire program.

### Code

```cpp
// From ast.h
class ProgramNode : public ASTNode {
private:
    vector<ASTNode*> units;

public:
    ~ProgramNode() {
        for (auto unit : units) {
            delete unit;
        }
    }
    
    void add_unit(ASTNode* unit) {
        if (unit) units.push_back(unit);
    }
    
    string generate_code(...) const override {
        for (auto unit : units) {
            unit->generate_code(...);
            outcode << "\n";
        }
        return "";
    }
};
```

```yacc
// From 22101710.y
program : program unit
    {
        // ...
        ProgramNode* prog;
        if($1->get_ast_node()) {
            prog = (ProgramNode*)$1->get_ast_node();
        } else {
            prog = new ProgramNode();
        }
        
        if($2->get_ast_node()) {
            prog->add_unit($2->get_ast_node());
        }
        
        $$->set_ast_node(prog);
    }
```

### Explanation
- **`class ProgramNode : public ASTNode`**: Inherits from `ASTNode`.
- **`vector<ASTNode*> units;`**: A vector to store pointers to the top-level declaration and function definition nodes.
- **`add_unit(ASTNode* unit)`**: Adds a top-level unit (like a global variable declaration or a function definition) to the program.
- **`generate_code(...)`**: This is the entry point for code generation. It simply iterates through all the units (functions and global declarations) and calls their respective `generate_code()` methods.
- **In `22101710.y`**: The `program` rule builds up the `ProgramNode` by adding each `unit` (a variable declaration or function definition) to it. The final `ProgramNode` is set as the AST root.

This concludes the explanation of the AST implementation for Task 2.1.

