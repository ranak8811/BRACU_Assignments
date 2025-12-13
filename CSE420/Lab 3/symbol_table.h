#include "scope_table.h"


class symbol_table
{
private:
    scope_table *current_scope;
    int bucket_count;
    int current_scope_id;

public:
    symbol_table(int bucket_count) {
        this->bucket_count = bucket_count;
        this->current_scope_id = 1;
        current_scope = new scope_table(bucket_count, current_scope_id, nullptr);
    }
    ~symbol_table(){
        while(current_scope != nullptr) {
            exit_scope();
        }
    }
    symbol_info* lookup_in_current_scope(symbol_info* symbol) {
        if (current_scope) {
            return current_scope->lookup_in_scope(symbol); 
        }
        return nullptr; 
    }
    void enter_scope(){
        current_scope_id++;
        scope_table* scope_new = new scope_table(bucket_count, current_scope_id, current_scope);
        scope_new->set_parent(current_scope);
        current_scope = scope_new;
    }
    void exit_scope(){
        if (current_scope) {  
            auto parent_scope = current_scope->get_parent_scope();  
            delete current_scope;  
            current_scope = parent_scope;
        } else {
            cout << "No scope to exit." << endl;
        }
    }
    bool insert(symbol_info* symbol){
        if (current_scope) {
            return current_scope->insert_in_scope(symbol);
        } else {
            cout << "No current scope to insert symbol." << endl;
            return false;
        }
    }
    int get_current_id() {
        return current_scope ? current_scope->get_unique_id() : 0;
    }
    symbol_info* lookup(symbol_info* symbol){
        scope_table* temp= current_scope;
        while(temp != nullptr) {
            symbol_info* result = temp->lookup_in_scope(symbol);
            if (result != nullptr) 
            {
                return result;
            }
            temp = temp->get_parent_scope();
        }
        return nullptr;
    }
    void print_current_scope(std::ofstream outlog){
        if(current_scope != nullptr) {
            current_scope->print_scope_table(outlog);
        }
    }
    void print_all_scopes(std::ofstream& outlog){
             outlog<<"################################"<<endl<<endl;
             scope_table *temp = current_scope;
             while (temp != nullptr)
             {
                 temp->print_scope_table(outlog);
                 temp = temp->get_parent_scope();
             }
             outlog<<"################################"<<endl<<endl;
         }

    // you can add more methods if you need 
    
    scope_table* get_parent_scope() 
    {
        if(current_scope) 
        {
            return current_scope->get_parent_scope();
        }
        return nullptr;
    }

    scope_table* get_current_scope() 
    {
        return current_scope;
    }
};

// complete the methods of symbol_table class


// void symbol_table::print_all_scopes(ofstream& outlog)
// {
//     outlog<<"################################"<<endl<<endl;
//     scope_table *temp = current_scope;
//     while (temp != NULL)
//     {
//         temp->print_scope_table(outlog);
//         temp = temp->get_parent_scope();
//     }
//     outlog<<"################################"<<endl<<endl;
// }