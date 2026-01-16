# Explanation of Three-Address Code Generation (Task 2.3)

This document explains the implementation of the `generate_code` method for each AST node type, which is responsible for generating three-address code (TAC). This process is the final step of the compiler's front end, translating the high-level language constructs, now represented in the AST, into a low-level, machine-independent intermediate representation.

The `generate_code` method is a virtual function in the base `ASTNode` class and is overridden by each derived node class. It recursively traverses the AST, and at each node, it generates the corresponding TAC instructions. The method uses counters for creating unique temporary variables (`t0`, `t1`, ...) and labels (`L0`, `L1`, ...).

---

## 1. Arithmetic, Logical, and Relational Operations

These operations are primarily handled by `BinaryOpNode` for binary operations and `UnaryOpNode` for unary operations like logical NOT.

### `BinaryOpNode` (for +, -, *, /, &&, ||, <, >, ==, etc.)

#### Code
```cpp
// From ast.h
class BinaryOpNode : public ExprNode {
private:
    string op;
    ExprNode* left;
    ExprNode* right;
public:
    // ... constructor and destructor ...
    
    string generate_code(ofstream& outcode, map<string, string>& symbol_to_temp,
                        int& temp_count, int& label_count) const override {
        string left_temp = left->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        string right_temp = right->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        
        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = " << left_temp << " " << op << " " << right_temp << "\n";
        return result_temp;
    }
};
```

#### Explanation
The code generation for all binary operations (arithmetic, logical, and relational) follows the same pattern:
1.  **`left->generate_code(...)`**: It first recursively calls `generate_code` on its left child. This will generate the code for the left operand and return the name of the temporary variable holding its result (e.g., `t0`).
2.  **`right->generate_code(...)`**: It then does the same for the right child, getting the result in another temporary variable (e.g., `t1`).
3.  **`string result_temp = "t" + to_string(temp_count++);`**: A new temporary variable is created to store the result of the binary operation (e.g., `t2`).
4.  **`outcode << result_temp << " = " << left_temp << " " << op << " " << right_temp << "\n";`**: The final three-address instruction is generated. For example, if the operation is `+`, it will output `t2 = t0 + t1`. If it's `&&`, it will output `t2 = t0 && t1`.
5.  **`return result_temp;`**: The name of the temporary variable holding the result (`t2`) is returned, so parent nodes in the AST can use it in their own calculations.

### `UnaryOpNode` (for ! and unary -)

#### Code
```cpp
// From ast.h
class UnaryOpNode : public ExprNode {
private:
    string op;
    ExprNode* expr;
public:
    // ... constructor and destructor ...
    
    string generate_code(ofstream& outcode, map<string, string>& symbol_to_temp,
                        int& temp_count, int& label_count) const override {
        string expr_temp = expr->generate_code(outcode, symbol_to_temp, temp_count, label_count);
        string result_temp = "t" + to_string(temp_count++);
        outcode << result_temp << " = " << op << expr_temp << "\n";
        return result_temp;
    }
};
```

#### Explanation
The process for unary operations is similar but simpler:
1.  **`expr->generate_code(...)`**: It recursively calls `generate_code` on its child expression to get its result into a temporary variable (e.g., `t0`).
2.  **`string result_temp = "t" + to_string(temp_count++);`**: A new temporary variable is created for the result (e.g., `t1`).
3.  **`outcode << result_temp << " = " << op << expr_temp << "\n";`**: The TAC instruction is generated. For a logical NOT, this would be `t1 = !t0`.
4.  **`return result_temp;`**: The name of the result temporary is returned.

---
## 2. Assignment and Array Access

### `AssignNode`

#### Code
```cpp
// From ast.h
class AssignNode : public ExprNode {
private:
    VarNode* lhs;
    ExprNode* rhs;
public:
    // ... constructor and destructor ...
    
    string generate_code(ofstream& outcode, map<string, string>& symbol_to_temp,
                        int& temp_count, int& label_count) const override {
        string rhs_temp = rhs->generate_code(outcode, symbol_to_temp, temp_count, label_count);

        if(lhs->has_index()) {
            string index_temp = lhs->generate_index_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << lhs->get_name() << "[" << index_temp << "] = " << rhs_temp << "\n";
        } else {
            outcode << lhs->get_name() << " = " << rhs_temp << "\n";
        }
        return rhs_temp;
    }
};
```
#### Explanation
1.  **`rhs->generate_code(...)`**: It generates the code for the right-hand side expression first, getting the result into a temporary variable (e.g., `t0`).
2.  **`if(lhs->has_index())`**: It checks if the left-hand side is an array access.
3.  **Array Assignment**: If it is an array, it calls `generate_index_code` on the LHS `VarNode` to get the temporary for the index (e.g., `t1`). Then it generates the instruction `a[t1] = t0`.
4.  **Simple Assignment**: If it's a simple variable, it generates the instruction `a = t0`.
5.  The value of the assignment expression is the value of the right-hand side, so it returns `rhs_temp`.

### `VarNode` (Array Access)

When a `VarNode` is used in an expression (not as the LHS of an assignment), its `generate_code` method is called.

#### Code
```cpp
// From ast.h
class VarNode : public ExprNode {
private:
    string name;
    ExprNode* index; 
public:
    // ... constructor, destructor, etc. ...
    
    string generate_code(ofstream& outcode, map<string, string>& symbol_to_temp,
                        int& temp_count, int& label_count) const override {
        if (symbol_to_temp.find(name) != symbol_to_temp.end()) {
            return symbol_to_temp[name];
        }

        string result_temp = "t" + to_string(temp_count++);
        
        if (!has_index()) {
            outcode << result_temp << " = " << name << "\n";
        } else {
            string index_temp = generate_index_code(outcode, symbol_to_temp, temp_count, label_count);
            outcode << result_temp << " = " << name << "[" << index_temp << "]\n";
        }
        
        return result_temp;
    }
};
```
#### Explanation
1.  **`if (!has_index())`**: If it's a simple variable, it generates `t0 = a` to load the variable's value into a temporary.
2.  **`else`**: If it is an array access (`a[i]`):
    *   **`generate_index_code(...)`**: It first generates the code for the index expression, getting the result in a temporary (e.g., `t1`).
    *   **`outcode << result_temp << " = " << name << "[" << index_temp << "]\n";`**: It then generates the instruction to load the value from the array into a new temporary variable, for example: `t2 = a[t1]`.
3.  The method returns the name of the new temporary (`t0` or `t2`) that holds the value of the variable or array element.

---
## 3. Control Structures

Control structures are translated into TAC using labels and conditional (`if`) or unconditional (`goto`) jumps.

### `IfNode`

#### Code
```cpp
// From ast.h
class IfNode : public StmtNode {
private:
    ExprNode* condition;
    StmtNode* then_block;
    StmtNode* else_block;
public:
    // ... constructor and destructor ...
    
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
#### Explanation
1.  **Label Generation**: It generates unique labels for the `then` block, the `else` block, and the end of the statement.
2.  **Condition**: It generates the code for the condition, getting the result in `cond_temp`.
3.  **Conditional Jump**: It generates an `if ... goto` to jump to the `then` block if the condition is true.
4.  **Else Jump**: It generates a `goto` to the `else` block if the condition is false.
5.  **Then Block**: It emits the `then` label and recursively generates the code for the `then` statement block.
6.  **End Jump**: After the `then` block, it generates a `goto` to the `end` label to skip over the `else` block.
7.  **Else Block**: It emits the `else` label and generates the code for the `else` block (if it exists).
8.  **End Label**: It emits the `end` label.

### `WhileNode`

#### Code
```cpp
// From ast.h
class WhileNode : public StmtNode {
private:
    ExprNode* condition;
    StmtNode* body;
public:
    // ... constructor and destructor ...
    
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
1.  **Label Generation**: It generates labels for the start of the loop (condition check), the loop body, and the end of the loop.
2.  **Start Label**: It emits the `start` label.
3.  **Condition Check**: It generates the code for the condition.
4.  **Body Jump**: It uses `if ... goto` to jump to the `body` label if the condition is true.
5.  **End Jump**: It uses `goto` to jump to the `end` label if the condition is false.
6.  **Body Block**: It emits the `body` label, generates the code for the loop's body, and then generates a `goto` back to the `start` label to re-evaluate the condition.
7.  **End Label**: It emits the `end` label.

### `ForNode`

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
    // ... constructor and destructor ...
    
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
The `for` loop's code generation is a combination of sequential and loop logic:
1.  **Initialization**: It first generates the code for the `init` expression. This is done only once.
2.  **Loop Setup**: It then sets up a loop structure very similar to the `while` loop, with labels for the start (condition check), body, and end.
3.  **Body and Update**: Inside the loop body (after the `label_body` label), it generates the code for the `body` statements, and then generates the code for the `update` expression.
4.  **Loop Back**: Finally, it jumps back to the `start` label to re-evaluate the condition.

---
## 4. Function Calls and Returns

### `FuncCallNode`

#### Code
```cpp
// From ast.h
class FuncCallNode : public ExprNode {
private:
    string func_name;
    vector<ExprNode*> arguments;
public:
    // ... constructor and destructor ...
    
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
#### Explanation
1.  **Argument Evaluation**: It iterates through the list of `arguments` and recursively calls `generate_code` for each one to evaluate it. The temporary variables holding the results are stored in `arg_temps`.
2.  **Param Instructions**: It then generates a `param` instruction for each argument, effectively pushing them onto the stack for the function call (e.g., `param t0`, `param t1`).
3.  **Call Instruction**: It generates a `call` instruction, which includes the function name and the number of arguments. The return value of the function is assigned to a new temporary variable (e.g., `t2 = call my_func, 2`).
4.  **Return Value**: It returns the name of the temporary variable that holds the function's return value.

### `ReturnNode`

#### Code
```cpp
// From ast.h
class ReturnNode : public StmtNode {
private:
    ExprNode* expr;
public:
    // ... constructor and destructor ...
    
    string generate_code(...) const override {
        string expr_temp = expr ? expr->generate_code(...) : "";
        outcode << "return " << expr_temp << "\n";
        return expr_temp;
    }
};
```
#### Explanation
1.  **Expression Evaluation**: It generates the code for the return expression (if it exists), getting its value into a temporary variable, `expr_temp`. If there is no expression (as in `return;`), `expr_temp` will be empty.
2.  **Return Instruction**: It generates the `return` instruction, followed by the temporary variable holding the return value (e.g., `return t0`).

This concludes the detailed explanation of how three-address code is generated from the AST for each specified language feature.
