#include "scope_table.h"

class symbol_table
{
private:
    scope_table *current_scope;
    int bucket_count;
    int current_scope_id;

public:

    // constructor
    symbol_table(int bucket_count)
    {
        this->bucket_count = bucket_count;
        this->current_scope_id = 1;
        current_scope = new scope_table(bucket_count, current_scope_id, NULL);
    }

    // destructor
    ~symbol_table()
    {
        // delete scope tables
        while (current_scope != NULL) {
            scope_table *temp = current_scope;
            current_scope = current_scope->get_parent_scope();
            delete temp;
        }
    }

    // enter in the current scope
    void enter_scope()
    {
        current_scope_id += 1;
        scope_table *new_scope = new scope_table(bucket_count, current_scope_id, current_scope);
        current_scope = new_scope;
    }

    // exit from the current scope
    void exit_scope()
    {
        if (current_scope == NULL)
        {
            return;
        }

        // store parent before deleting current scope
        scope_table *parent = current_scope->get_parent_scope();
        delete current_scope;
        current_scope = parent;
    }
        
    // insert a symbol
    bool insert(symbol_info* symbol)
    {
        if (current_scope == NULL)
        {
            return false;
        }
        return current_scope->insert_in_scope(symbol);
    }

    // lookup a symbol
    symbol_info* lookup(symbol_info* symbol)
    {
        scope_table *temp = current_scope;
        while (temp != NULL)
        {
            symbol_info *result = temp->lookup_in_scope(symbol);
            if (result != NULL)
            {
                return result;
            }
            temp = temp->get_parent_scope();
        }
        return NULL;
    }

    // print the only current scope
    void print_current_scope()
    {
        if (current_scope != NULL)
        {
            outlog << endl << "################################" << endl << endl;

            // print all scopes from current to root
            scope_table *temp = current_scope;
            while (temp != NULL)
            {
                temp->print_scope_table(outlog);
                temp = temp->get_parent_scope();
            }

            outlog << "################################" << endl << endl;
        }     
    }

    // print all scopes
    void print_all_scopes(ofstream& outlog)
    {
        outlog << "Symbol Table" << endl << endl;
        outlog << "################################" << endl << endl;

        // print all scopes from current to root
        scope_table *temp = current_scope;
        while (temp != NULL)
        {
            temp->print_scope_table(outlog);
            temp = temp->get_parent_scope();
        }

        outlog << "################################" << endl;
    }

    // you can add more methods if you need 

    // helper method to get current scope id
    int get_current_scope_id()
    {
        return current_scope_id;
    }

    // helper method to check if we are in the global scope
    bool is_global_scope()
    {
        return current_scope_id != NULL && current_scope->get_parent_scope() == NULL;
    }

    // add lookup current scope function
    symbol_info* lookup_current_scope(symbol_info* symbol)
    {
        if (current_scope == NULL)
        {
            return NULL;
        }
        return current_scope->lookup_in_scope(symbol);
    }
};