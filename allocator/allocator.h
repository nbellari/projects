#ifndef __ALLOCATOR_H__

#define __ALLOCATOR_H__

/* Lets keep it simple, and grow as needed */
struct header {
    size_t size; /* size of the allocated memory, excluding the header */
    struct header *next; /* Points to the next element in the free list */
};

typedef union {
    struct header h;
    char _align[16]; /* This chunk of memory (header) will be aligned to 16 bytes */
} header_t;

#define ALLOCATOR_HEADER_SIZE   sizeof(header_t);

/* Free list */
extern header_t *free_list_head;

#endif