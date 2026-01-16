# Explanation of AST Construction During Parsing (Task 2.2)

This document explains how the Abstract Syntax Tree (AST) is constructed during the parsing phase, as described in Task 2.2. The parser, defined in `22101710.y`, is modified to create and connect AST nodes for each grammar rule. This process builds the complete AST, which is then used for semantic analysis and code generation.

The core idea is to associate an AST node with each grammar symbol (`YYSTYPE`, which is a `symbol_info*`). The `symbol_info` struct is extended to hold a pointer to an `ASTNode`. As the parser reduces a grammar rule, it creates a new AST node and attaches it to the `symbol_info` of the non-terminal on the left-hand side of the rule.

---

## Passing AST Nodes

In many cases, a grammar rule simply passes the AST node of a child symbol up to the parent. This is common in rules that don't introduce new semantics but are used for structuring the grammar.

### Code
```yacc
// From 22101710.y
expression : logic_expression
    {
        // ...
        $$ = new symbol_info($1->getname(),"expr");
        $$->setvartype($1->getvartype());
        $$->set_ast_node($1->get_ast_node());
    }
```

### Explanation
- **`expression : logic_expression`**: This rule states that a `logic_expression` is a form of `expression`.
- **`$$->set_ast_node($1->get_ast_node());`**: Here, the AST node from the `logic_expression` (`$1`) is retrieved using `get_ast_node()` and then set as the AST node for the `expression` (`$$`). The node is simply passed up the parse tree without modification.

---

## Creating Expression Nodes

More complex rules create new AST nodes to represent the operation.

### `AssignNode`

#### Code
```yacc
// From 22101710.y
expression : variable ASSIGNOP logic_expression
    {
        // ... (type checking) ...
        
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
- **`expression : variable ASSIGNOP logic_expression`**: This rule handles assignment.
- **`new AssignNode(...)`**: A new `AssignNode` is created.
- **`(VarNode*)$1->get_ast_node()`**: The AST node for the `variable` on the left-hand side (`$1`) is retrieved and cast to a `VarNode*`. This becomes the left child of the `AssignNode`.
- **`(ExprNode*)$3->get_ast_node()`**: The AST node for the `logic_expression` on the right-hand side (`$3`) is retrieved and cast to an `ExprNode*`. This becomes the right child of the `AssignNode`.
- **`$$->set_ast_node(assignNode)`**: The newly created `assignNode` is set as the AST node for the `expression` (`$$`).

### `BinaryOpNode`

#### Code
```yacc
// From 22101710.y
simple_expression : simple_expression ADDOP term 
    {
        // ... (type checking) ...
        
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
- **`simple_expression : simple_expression ADDOP term`**: This rule handles addition and subtraction.
- **`new BinaryOpNode(...)`**: A `BinaryOpNode` is created to represent the operation.
- **`$2->getname()`**: The operator (e.g., "+", "-") is retrieved from the `ADDOP` token (`$2`).
- **`(ExprNode*)$1->get_ast_node()`**: The AST node of the left `simple_expression` (`$1`) is set as the left operand.
- **`(ExprNode*)$3->get_ast_node()`**: The AST node of the `term` (`$3`) is set as the right operand.
- **`$$->set_ast_node(addopNode)`**: The new `addopNode` is set as the node for the parent `simple_expression`. This is how left-recursive rules correctly build a left-leaning tree.

---

## Creating Statement Nodes

Statement rules are handled similarly, creating nodes for control flow, blocks, and declarations.

### `IfNode`

#### Code
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
- **`statement : IF ... ELSE ...`**: This rule parses an if-else statement.
- **`new IfNode(...)`**: An `IfNode` is created.
- **`(ExprNode*)$3->get_ast_node()`**: The node for the condition `expression` (`$3`) is passed as the condition.
- **`(StmtNode*)$5->get_ast_node()`**: The node for the `then` part's `statement` (`$5`) is passed as the "then" block.
- **`(StmtNode*)$7->get_ast_node()`**: The node for the `else` part's `statement` (`$7`) is passed as the "else" block.
- **`$$->set_ast_node(ifNode)`**: The new `ifNode` is associated with the parent `statement` (`$$`).

### `BlockNode`

#### Code
```yacc
// From 22101710.y
statements : statement
    {
        // ...
        // Create block for statements
        BlockNode* block = new BlockNode();
        if($1->get_ast_node()) {
            block->add_statement((StmtNode*)$1->get_ast_node());
        }
        $$->set_ast_node(block);
    }
    | statements statement
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
- The `statements` rules work together to create a `BlockNode` that contains a list of statements.
- **`statements : statement`**: When the first statement is found, a new `BlockNode` is created, and the statement's AST node is added to it.
- **`statements : statements statement`**: For subsequent statements, the existing `BlockNode` from the left-hand `statements` (`$1`) is retrieved. The new `statement`'s AST node (`$2`) is then added to this existing block. This builds up the list of statements within the block.

---

## The Program Root (`ProgramNode`)

The entire program is rooted by a `ProgramNode`, which holds all top-level declarations and function definitions.

### Code
```yacc
// From 22101710.y
program : program unit
    {
        // ...
        // Create/update AST node for program
        ProgramNode* prog;
        if($1->get_ast_node()) {
            prog = (ProgramNode*)$1->get_ast_node();
        } else {
            prog = new ProgramNode();
        }
        
        // Add the unit to the program
        if($2->get_ast_node()) {
            prog->add_unit($2->get_ast_node());
        }
        
        $$->set_ast_node(prog);
    }
    | unit
    {
        // ...
        // Create AST node for program with a single unit
        ProgramNode* prog = new ProgramNode();
        if($1->get_ast_node()) {
            prog->add_unit($1->get_ast_node());
        }
        $$->set_ast_node(prog);
    }
```
### Explanation
- Similar to the `BlockNode`, the `program` rule gathers all the top-level `unit`s (global variable declarations or function definitions).
- It retrieves the `ProgramNode` from the preceding `program` symbol, adds the new `unit`'s AST node to it, and passes the updated `ProgramNode` up the tree.
- The `start` rule ultimately gets the final, complete `ProgramNode` and assigns it to the global `ast_root` pointer.

This bottom-up construction process, where each grammar rule reduction creates or aggregates AST nodes, results in a complete Abstract Syntax Tree representing the entire source code file once parsing is complete.
