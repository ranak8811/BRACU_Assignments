#include "symbol_info.h"

class scope_table
{
private:
    int bucket_count;
    int unique_id;
    scope_table *parent_scope = NULL;
    vector<list<symbol_info *>> table;

    int hash_function(string name)
    {
        int hash = 0;
        for (char c: name)
        {
            hash = (hash*31 + c) % bucket_count;  
        }
        return hash;

    }

public:
    scope_table();
    scope_table(int bucket_count, int unique_id, scope_table *parent_scope){
        this->bucket_count = bucket_count;
        this->unique_id = unique_id;
        this->parent_scope = parent_scope;
        table.resize(bucket_count);
    }
    scope_table *get_parent_scope(){
        return parent_scope;
    }
    void set_parent(scope_table* parent) {
        parent_scope = parent;
    }
    int get_unique_id(){
        return unique_id;
    }
    symbol_info *lookup_in_scope(symbol_info* symbol){
        int index = hash_function(symbol->getname());
        for (symbol_info* s : table[index]){
            if (s->getname() == symbol->getname()){
                return s;
            }
        }
        return nullptr;
    }
    bool insert_in_scope(symbol_info* symbol){
        int index = hash_function(symbol->getname());
        if (lookup_in_scope(symbol) == nullptr){
            table[index].push_back(symbol);
            return true;
        }
        return false;
    }
    bool delete_from_scope(symbol_info* symbol){
        int index = hash_function(symbol->getname());
        for (symbol_info* s : table[index]){
            if (s->getname() == symbol->getname()){
                table[index].remove(s);
                return true;
            }
        }
        return false;
    }
    void print_scope_table(ofstream& outlog){
        outlog << "ScopeTable # " << unique_id << endl;
        for(int i=0; i<bucket_count; i++){
            if (table[i].empty()){
                continue;
            }
            else {
                outlog << i << " --> " <<endl;
                for(symbol_info* s : table[i]){
                    outlog << "<" << s->getname() << " : " << s->get_type() << "> " <<endl;
                    if (s->isArray()){
                        outlog << "Array" <<endl;
                        outlog << "Type: "<< s->get_datatype() <<endl;
                        outlog << "Size: "<< s->get_array_size() <<endl;
                    }
                    else if (s->isFunction()){
                        outlog << "Function Definition" <<endl;
                        outlog << "Return Type: "<< s->get_datatype() <<endl;
                        outlog << "Number of Parameters: " << s->get_parameters().size() <<endl;
                        outlog << "Parameter Details: ";
                        auto params = s->get_parameters();
                        for (int i=0; i<params.size(); i++){
                            outlog << params[i].first << " " << params[i].second;
                            if (i != params.size()-1){
                                outlog << ", ";
                            }
                        }
                    }
                    else{
                        outlog<< "Variable" <<endl;
                        outlog << "Type: "<< s->get_datatype() <<endl;
                    }
                    outlog <<endl<<endl;
            }
        }
        }
    }
    ~scope_table() {
        for(auto& bucket : table) {
            for(auto symbol : bucket) {
                delete symbol;
            }
            bucket.clear();
        }
        table.clear();
    }

   
};

