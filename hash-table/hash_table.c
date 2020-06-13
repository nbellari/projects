#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

#include "hash_table.h"

#define HT_DEFAULT_BUCKET_SIZE  512

/* A hash table entry is a collection of key and value */
typedef struct ht_entry {
    char *key;
    char *value;
    struct ht_entry *next, *prev; /* Doubly linked list for ease of addition/removal */
} ht_entry_t;

/* A hash table is one that stores the key-value pairs */
typedef struct {
    long  ht_n_buckets;
    long  ht_count;
    ht_entry_t **ht_buckets; 
} htable_t;

/* These functions do not care about buckets, just calculates the hash
 * and returns the same.
 * Two hashes are used here:
 * 
 *  -sdbm hash
 *  -djb hash, apparently, the best hash known ever for strings
 */

/* Second hash function to the rescue, in case first one results in a collision */
static unsigned long
hash_csum2(char *str)
{
    unsigned long hash = 0;
    char c;

    while (str && *str != '\0') {
        /* hash = c + hash*65599 */
        hash = c + (hash << 16) + (hash << 6) - hash;
        str++;
    }

    return hash;
}

static long
hash2_bucket(char *str, long n_buckets)
{
    return hash_csum2(str) % n_buckets;
}

/* First hash function */
static unsigned long
hash_csum(char *str)
{
    unsigned long csum = 5381;
    char c;

    while (str && *str != '\0') {
        c = *str++;
        csum = ((csum << 5) + csum) ^ c;
    }

    return csum;
}

static long
hash1_bucket(char *str, long n_buckets)
{
    return hash_csum(str) % n_buckets;
}

static ht_entry_t *
ht_entry_create(char *key, char *value)
{
    ht_entry_t *entry;

    entry = calloc(1, sizeof(ht_entry_t));

    /* We dont assume the pointers passed by the user are 
     * going to be alive until this entry is removed
     */
    entry->key = strdup(key);
    entry->value = strdup(value);

    return entry;
}

static void
ht_entry_delete(ht_entry_t *entry)
{
    if (!entry) {
        return;
    }

    /* key and value are defined by us */
    free(entry->key);
    free(entry->value);
    free(entry);

    return;
}

static void
ht_entry_flush_all(htable_t *table)
{
    int         i;
    ht_entry_t  *entry, *next;

    for (i=0; i<table->ht_n_buckets; i++) {
        if (table->ht_buckets[i]) {
            entry = table->ht_buckets[i];
            /* Delete all the entries in the bucket */
            while (entry) {
                next = entry->next;
                ht_entry_delete(entry);
                entry = next;               
            }
        }
    }

}

/* This function encodes the logic of hash table type -
 * i.e. encodes how the hash table handles collisions
 */
static long
hash_table_get_bucket(htable_t *table, char *key, uint8_t new)
{
    long     i, idx;
    long     hash1_idx, hash2_idx;
    
    hash1_idx = hash1_bucket(key, table->ht_n_buckets);
    hash2_idx = hash2_bucket(key, table->ht_n_buckets);

    for (i=0; i<table->ht_n_buckets; i++) {
        /* (h1 + i*h2) % buckets */
        idx = (hash1_idx + i * hash2_idx) % table->ht_n_buckets;
        
        /* If the slot is empty, the loop terminates */
        if (!table->ht_buckets[idx]) {
            if (new)
                return idx;
            else
                return -1;
        } else if (strcmp(table->ht_buckets[idx]->key, key) == 0) {
            if (!new) {
                return idx;
            }
        }
        /* continue, otherwise */
    }

    /* If we reach here, it means the string did not get mapped to
     * any bucket. Not sure, if this is a valid case
     */
    assert(0);
}

static void
hash_table_insert(void *hash_table, char *key, char *value)
{
    long            idx;
    ht_entry_t      *entry = NULL;
    htable_t        *table = (htable_t *)hash_table;

    /* This does not return without a valid index */
    idx = hash_table_get_bucket(hash_table, key, 1/*new*/);
    entry = ht_entry_create(key, value);

    table->ht_buckets[idx] = entry;
}

static ht_entry_t *
hash_table_entry_get(htable_t *table, char *key)
{
    long idx;

    idx = hash_table_get_bucket(table, key, 0/*new*/);
    if (idx < 0) {
        return NULL;
    } else {
        return table->ht_buckets[idx];
    }
}

void *
hash_table_create(long n_buckets)
{
    htable_t *table;

    if (!n_buckets) {
        n_buckets = HT_DEFAULT_BUCKET_SIZE;
    }

    table = calloc(1, sizeof(htable_t));
    if (table == NULL) {
        /* Memory allocation failure - serious */
        return NULL;
    }

    table->ht_buckets = calloc(n_buckets, sizeof(ht_entry_t *));
    if (table->ht_buckets == NULL) {
        /* Memory allocation failure - serious */
        free(table);
        return NULL;
    }

    table->ht_n_buckets = n_buckets;

    return table;
}

void
hash_table_destroy(void *hash_table)
{
    htable_t    *table = (htable_t *)hash_table;

    if (!table) {
        return;
    }

    /* Loop through all the elements, free all the elements
     * and then destroy the hash table
     */
    ht_entry_flush_all(table);

    /* Free the buckets */
    free(table->ht_buckets);

    /* Free the table */
    free(table);

    return;
}

char *
hash_table_search(void *hash_table, char *key)
{
    htable_t *table = (htable_t *)hash_table;
    ht_entry_t  *entry = hash_table_entry_get(table, key);

    if (entry) {
        return entry->value;
    }

    return NULL;
}

void
hash_table_add(void *hash_table, char *key, char *value)
{
    htable_t    *table = (htable_t *)hash_table;
    ht_entry_t  *entry = hash_table_entry_get(table, key);

    if (entry) {
        /* Entry already present, overwrite the value */
        free(entry->value);
        entry->value = strdup(value);
    } else {
        /* Entry does not exist, add it */
        hash_table_insert(hash_table, key, value);
    }
}

void
hash_table_delete(void *hash_table, char *key)
{
    htable_t    *table = (htable_t *)hash_table;
    long        idx = hash_table_get_bucket(table, key, 0/*new*/);
    ht_entry_t  *entry;

    if (idx < 0) {
        /* nothing to do */
        return;
    }

    entry = table->ht_buckets[idx];
    table->ht_buckets[idx] = NULL;
    ht_entry_delete(entry);
    return;
}