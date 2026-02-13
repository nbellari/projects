#include <stdio.h>
#include "hash_table.h"

int
main(int argc, char **argv)
{
    void *hash_table;

    hash_table = hash_table_create(0);
    hash_table_add(hash_table, "name", "nagp");
    printf("Look up key (%s), result: %s\n",
                "name", hash_table_search(hash_table, "name"));
    hash_table_delete(hash_table, "name");
    hash_table_destroy(hash_table);

    return 0;
}