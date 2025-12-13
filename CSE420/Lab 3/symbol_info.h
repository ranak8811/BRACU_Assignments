#include<bits/stdc++.h>
using namespace std;

class symbol_info
{
private:
    string name;
    string type;

    // Write necessary attributes to store what type of symbol it is (variable/array/function)
    // Write necessary attributes to store the type/return type of the symbol (int/float/void/...)
    // Write necessary attributes to store the parameters of a function
    // Write necessary attributes to store the array size if the symbol is an array

    enum symbol_type
    {
        VARIABLE,
        FUNCTION,
        ARRAY
    };
    symbol_type symbol_type;
    int array_size;
    string data_type;
    vector<pair<string, string>> parameters;

public:
    symbol_info(string name, string type)
    {
        this->name = name;
        this->type = type;
        this->symbol_type = VARIABLE;
        this->array_size = 0;
    }
    string getname()
    {
        return name;
    }
    string get_type()
    {
        return type;
    }
    void set_parameters(const vector<pair<string, string>> &params) {
        parameters = params;
    }
    void set_name(string name)
    {
        this->name = name;
    }
    void set_type(string type)
    {
        this->type = type;
    }
   
    void set_array(int size)
    {
        symbol_type = ARRAY;
        array_size = size;
    }
    void set_as_function(string return_type, vector<pair<string, string>> parameter)
    {
        symbol_type = FUNCTION;
        parameters = parameter;
        data_type = return_type;
    }

    void set_datatype(string type)
    {
        data_type = type;
        if (symbol_type == VARIABLE)
        {
            symbol_type = VARIABLE;
        }
    }

    bool isArray()
    {
        return symbol_type == ARRAY;
    }
    bool isFunction()
    {
        return symbol_type == FUNCTION;
    }
    string get_datatype()
    {
        return data_type;
    }
    vector<pair<string, string>> get_parameters()
    {
        return parameters;
    }
    int get_array_size()
    {
        return array_size;
    }

    ~symbol_info()
    {
        // Write necessary code to deallocate memory, if necessary
    }
};