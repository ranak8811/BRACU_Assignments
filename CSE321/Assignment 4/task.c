#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 5
#define MAX_RESOURCES 5
#define MAX_NAME_LEN 20

#define MAX_ENTRIES_ACL 20
#define MAX_ENTRIES_CBAC 20

typedef enum { 
    NO_PERM = 0,
    READ = 1,
    WRITE = 2,
    EXECUTE = 4,
    ALL_PERM = READ | WRITE | EXECUTE
} Permission;

// User and Resource Definitions
typedef struct {
    char name[MAX_NAME_LEN];
} User;

typedef struct {
    char name[MAX_NAME_LEN];
} Resource;

// ACL Entry
typedef struct {
    char username[MAX_NAME_LEN];
    int permissions;
} ACLEntry;

typedef struct {
    char resource_name[MAX_NAME_LEN];
    ACLEntry entries[MAX_ENTRIES_ACL];
    int count;
} ACLControlledResource;

// Capability Entry
typedef struct {
    char name[MAX_NAME_LEN];
    int permissions;
} Capability;

typedef struct {
    User person;
    Capability capabilities[MAX_ENTRIES_CBAC];
    int count;
} CapabilityUser;

// Utility Functions
const char *printPermissions(int perm) {
    switch(perm) {
        case READ:
            return "READ";
        case WRITE:
            return "WRITE";
        case EXECUTE:
            return "EXECUTE";
        case ALL_PERM:
            return "ALL_PERM";
        case NO_PERM:
        default:
            return "NO_PERM";
    }
}

int hasPermission(int userPerm, int requiredPerm) {
    return (userPerm & requiredPerm) ? 1 : 0;
}

// ACL System
void checkACLAccess(ACLControlledResource *res, const char *userName, int perm) {
    int found = 0;
    int granted = 0;
    char result[10];
    
    for (int i = 0; i < res->count; i++) {
        if (strcmp(res->entries[i].username, userName) == 0) {  // Fixed variable name
            found = 1;
            granted = hasPermission(res->entries[i].permissions, perm);
            break;
        }
    }
    
    if (granted) {
        strcpy(result, "GRANTED");
    } else {
        strcpy(result, "DENIED");
    }
    
    if (found) {
        printf("ACL Check: User %s requests %s on %s: Access %s\n", 
               userName, printPermissions(perm), res->resource_name, result);
    } else {
        printf("ACL Check: User %s has NO entry for resource %s: Access DENIED\n", 
               userName, res->resource_name);
    }
}

// Capability System
void checkCapabilityAccess(CapabilityUser *user, const char *resourceName, int perm) {
    int found = 0;
    int granted = 0;
    char result[10];
    
    for (int i = 0; i < user->count; i++) {
        if (strcmp(user->capabilities[i].name, resourceName) == 0) {
            found = 1;
            granted = hasPermission(user->capabilities[i].permissions, perm);
            break;
        }
    }
    
    if (granted) {
        strcpy(result, "GRANTED");
    } else {
        strcpy(result, "DENIED");
    }
    
    if (found) {
        printf("Capability Check: User %s requests %s on %s: Access %s\n", 
               user->person.name, printPermissions(perm), resourceName, result);
    } else {
        printf("Capability Check: User %s has NO capability for %s: Access DENIED\n", 
               user->person.name, resourceName);
    }
}

int main() {
    // Sample users and resources - fixed array sizes
    User users[MAX_USERS] = {{"Alice"}, {"Bob"}, {"Charlie"}, {"Anwar"}, {"Rana"}};
    Resource resources[MAX_RESOURCES] = {{"File1"}, {"File2"}, {"File3"}, {"File4"}, {"File5"}};

    // ACL Setup
    ACLControlledResource aclResources[MAX_RESOURCES] = {
        {"File1", {{"Alice", READ | WRITE}, {"Bob", READ}, {"Rana", ALL_PERM}}, 3},
        {"File2", {{"Bob", ALL_PERM}, {"Charlie", READ | EXECUTE}, {"Rana", ALL_PERM}}, 3},
        {"File3", {{"Alice", WRITE}, {"Charlie", READ}, {"Rana", ALL_PERM}}, 3},
        {"File4", {{"Anwar", READ | EXECUTE}, {"Rana", ALL_PERM}}, 2},
        {"File5", {{"Bob", READ}, {"Rana", ALL_PERM}}, 2}
    };

    // Capability Setup
    CapabilityUser capabilityUsers[MAX_USERS] = {
        {{"Alice"}, {{"File1", READ | WRITE}, {"File3", WRITE}}, 2},
        {{"Bob"}, {{"File1", READ}, {"File2", ALL_PERM}, {"File5", READ}}, 3},
        {{"Charlie"}, {{"File2", READ | EXECUTE}, {"File3", READ}}, 2},
        {{"Anwar"}, {{"File4", READ | EXECUTE}}, 1},
        {{"Rana"}, {{"File1", ALL_PERM}, {"File2", ALL_PERM}, {"File3", ALL_PERM}, {"File4", ALL_PERM}, {"File5", ALL_PERM}}, 5}
    };   

    // Test ACL
    checkACLAccess(&aclResources[4], "Alice", READ);
    checkACLAccess(&aclResources[3], "Bob", WRITE);
    checkACLAccess(&aclResources[2], "Charlie", EXECUTE);
    checkACLAccess(&aclResources[1], "Anwar", WRITE);
    checkACLAccess(&aclResources[0], "Rana", READ);

    // Test Capability
    checkCapabilityAccess(&capabilityUsers[0], "File5", READ);
    checkCapabilityAccess(&capabilityUsers[1], "File4", WRITE);
    checkCapabilityAccess(&capabilityUsers[2], "File3", READ);
    checkCapabilityAccess(&capabilityUsers[2], "File2", WRITE);
    checkCapabilityAccess(&capabilityUsers[4], "File1", READ);

    return 0;
}
