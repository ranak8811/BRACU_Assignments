#include<bits/stdc++.h>

#include <iostream>
#include <string>
#include <vector>
#include <list>


using namespace std;

class symbol_info
{
private:
    string name;
    string type;
    
    // Write necessary attributes to store what type of symbol it is (variable/array/function)
    symbol_info *next;
    bool is_array;
    bool is_function;

    // Write necessary attributes to store the type/return type of the symbol (int/float/void/...)
    string data_type;
    string return_type;

    // Write necessary attributes to store the parameters of a function
    vector< pair <string, string> > parameters;

    // Write necessary attributes to store the array size if the symbol is an array
    int array_size;

public:

    symbol_info()
    {
        next = NULL;
        is_array = false;
        array_size = 0;
        is_function = false;
    }

    symbol_info(string name, string type)
    {
        this->name = name;
        this->type = type;
        next = NULL;
        is_array = false;
        array_size = 0;
        is_function = false;
    }
    
    // for variables
    symbol_info(string name, string type, string data_type)
    {
        this->name = name;
        this->type = type;
        this->data_type = data_type;
        next = NULL;
        is_array = false;
        array_size = 0;
        is_function = false;
    }
    
    
    // for array
    symbol_info(string name, string type, string data_type, int array_size)
    {
        this->name = name;
        this->type = type;
        this->data_type = data_type;
        this->array_size = array_size;
        next = NULL;
        is_function = false;
    }
    
    // for function
    symbol_info(string name, string type, string return_type, vector< pair <string, string> > parameters)
    {
        this->name = name;
        this->type = type;
        this->return_type = return_type;
        this->parameters = parameters;
        next = NULL;
        array_size = 0;
        is_array = false;
    }

    string get_name()
    {
        return name;
    }
    string get_type()
    {
        return type;
    }
    void set_name(string name)
    {
        this->name = name;
    }
    void set_type(string type)
    {
        this->type = type;
    }
    // Write necessary functions to set and get the attributes

    symbol_info *get_next()
    {
        return next;
    }
    void set_next(symbol_info *next)
    {
        this->next = next;
    }

    bool get_is_array()
    {
        return is_array;
    }
    void set_is_array(bool is_array)
    {
        this->is_array = is_array;
    }

    int get_array_size()
    {
        return array_size;
    }
    void set_array_size(int array_size)
    {
        this->array_size = array_size;
        this->is_array = true;
    }

    bool get_is_function()
    {
        return is_function;
    }
    void set_is_function(string return_type, vector< pair <string, string> > parameters)
    {
        this->is_function = true;
        this->return_type = return_type;
        this->parameters = parameters;
    }

    string get_data_type()
    {
        return data_type;
    }
    void set_data_type(string data_type)
    {
        this->data_type = data_type;
    }

    string get_return_type()
    {
        return return_type;
    }
    void set_return_type(string return_type)
    {
        this->return_type = return_type;
    }

    vector< pair <string, string> > get_parameters()
    {
        return parameters;
    }
    void set_parameters(vector< pair <string, string> > parameters)
    {
        this->parameters = parameters;
    }

    ~symbol_info()
    {
        // Write necessary code to deallocate memory, if necessary
        if (next)
        {
            delete next;
        }
    }
};