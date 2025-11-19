#include "symbol_info.h"
#include <list>
#include <fstream>
#include <string>
#include <iomanip>

extern ofstream outlog;
class scope_table
{
private:
    int bucket_count;
    int unique_id;
    scope_table *parent_scope = NULL;
    vector<list<symbol_info *>> table;

    int hash_function(string name)
    {
        // write your hash function here
        int total = 0;
        for (char character : name)
        {
            total += character;
        }
        return total % bucket_count;
    }

public:
    // default constructor    
scope_table()
    {
        bucket_count = 10;
        unique_id = 1;
        table.resize(bucket_count);
        outlog << "New ScopeTable with ID " << unique_id << " created" << endl << endl;
    }
    
    // parameterized constructor
    scope_table(int bucket_count, int unique_id, scope_table *parent_scope)
    {
        this->bucket_count = bucket_count;
        this->unique_id = unique_id;
        this->parent_scope = parent_scope;
        table.resize(bucket_count);
        outlog << "New ScopeTable with ID " << unique_id << " created" << endl << endl;
    }

    // get parent scope
    scope_table *get_parent_scope()
    {
        return parent_scope;
    }

    // get for unique id
    int get_unique_id()
    {
        return unique_id;
    }

    // symbol table operations: lookup
    symbol_info *lookup_in_scope(symbol_info* symbol)
    {
        int index = hash_function(symbol->get_name());

        // linear probing: search in the appropriate bucket
        for (symbol_info *current : table[index])
        {
            if (current->get_name() == symbol->get_name())
            {
                return current;
            }
        }
        return NULL;
    }

    // symbol table operations: insert
    bool insert_in_scope(symbol_info* symbol)
    {
        // check if the symbol already exists in the current scope
        if (lookup_in_scope(symbol) != NULL)
        {
            return false;
        }

        // insert the symbol in the appropriate bucket
        int index = hash_function(symbol->get_name());
        table[index].push_back(symbol);
        return true;
    }

    // symbol table operations: delete
    bool delete_from_scope(symbol_info* symbol)
    {
        int index = hash_function(symbol->get_name());

        // search & remove from the appropriate bucket
        auto &bucket = table[index];
        for (auto it = bucket.begin(); it != bucket.end(); ++it)
        {
            if ((*it)->get_name() == symbol->get_name())
            {
                bucket.erase(it);
                return true;
            }
        }
        return false;
    }

    // print scope table
    void print_scope_table(ofstream& outlog)
    {
        outlog << "ScopeTable # " << unique_id << endl;

        for (int i = 0; i < bucket_count; i++)
        {
            if (!table[i].empty())
            {
                outlog << i << " --> " << endl;

                for (auto current : table[i])
                {
                    // print symbol information
                    outlog << "< " << current->get_name() << " : " << current->get_type() << " >" << endl;

                    // handle different types of symbols
                    if (current->get_is_function())
                    {
                        outlog << "Function Definition" << endl;
                        outlog << "Return Type: " << current->get_return_type() << endl;
                        vector<pair<string, string>> params = current->get_parameters();
                        outlog << "Number of Parameters: " << params.size() << endl;
                        outlog << "Parameter Details: ";
                        for (int j = 0; j < params.size(); j++)
                        {
                            outlog << params[j].first << " " << params[j].second;
                            if (j < params.size() - 1)
                                outlog << ", ";
                        }
                        outlog << endl;
                    }
                    else if (current->get_is_array())
                    {
                        outlog << "Array" << endl;
                        outlog << "Type: " << current->get_data_type() << endl;
                        outlog << "Size: " << current->get_array_size() << endl;
                    }
                    else
                    {
                        outlog << "Variable" << endl;
                        outlog << "Type: " << current->get_data_type() << endl;
                    }
                }
            }
        outlog << endl; 

        }
};

    // destructor
    ~scope_table()
    {
        outlog << "Scopetable with ID " << unique_id << " removed" << endl << endl;

        for (auto &bucket : table)
        {
            for (auto &symbol : bucket)
            {
                delete symbol;
            }
            bucket.clear();
        }

        table.clear();
    }

};
