#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include "allocator.h"

header_t *free_list_head;

/* Function to get a free block from the free list, if one is available */
void *
get_free_block(size_t size)
{
    header_t *cur = free_list_head, *prev = free_list_head;
    header_t *free = NULL;

    while (cur) {
        /* Exact match may not be found */
        if (cur->h.size >= size) {
            free = cur;
            if (cur == free_list_head) {
                free_list_head = (header_t *)free_list_head->h.next;
            } else {
                prev->h.next = cur->h.next;
            }
            break;
        } else {
            prev = cur;
            cur = (header_t *)cur->h.next;
        }
    }

    return free;
}

void *
malloc2(size_t size)
{
    size_t total_size;
    void *block;
    header_t *header;

    if (size == 0) {
        return NULL;
    }

    /* Try to find from the free list */
    header = (header_t *)get_free_block(size);
    if (header != NULL) {
        block = (void *)(header + 1);
        return block;
    }

    /* Get from OS */
    total_size = size + sizeof(header_t);
    header = sbrk(total_size);

    if (header == (void *)-1) {
        /* Cannot grow the process, serious error!
         * However, we simply return NULL, taking action
         * is caller's responsibility
         */
        return NULL;
    }

    /* record the size */
    header->h.size = size;
    header->h.next = NULL;
    block =  (void *)(header + 1);

    return block;
}

void
put_free_block(header_t *header)
{
    /* Insert it at the head of the list */
    header->h.next = (struct header *)free_list_head;
    free_list_head = header;
}

void
free2(void *block)
{
    header_t *header = NULL;
    size_t total_size;
    void *program_break;

    if (block == NULL) {
        return;
    }

    program_break = sbrk(0);

    header = (header_t *)block - 1;
    total_size = header->h.size + sizeof (header_t);

    if ((char *)header + total_size == program_break) {
        /* This can be given back to the operating system */
        sbrk(-total_size);
    } else {
        /* put it in the free list */
        put_free_block(header);
    }

    return;
}

void *
calloc2(size_t n, size_t size)
{
    size_t total_size;
    void *block;

    if (!n || !size) {
        return NULL;
    }

    total_size = n * size;

    if (size != total_size/n) {
        return NULL;
    }

    block = malloc2(total_size);

    if (block) {
        memset(block, 0, total_size);
    }

    return block;
}

void *
realloc2(void *block, size_t size)
{
    header_t *header;
    size_t orig_size;
    void *new_block;

    if (!block || !size) {
        return NULL;
    }

    header = (header_t *)block - 1;
    orig_size = header->h.size;

    /* Since the block allocated need not be of exact same size,
     * it makes sense to check if the original block size can satisfy
     * the requested size
     */
    if (orig_size >= size) {
        return block;
    }

    new_block = malloc2(size);

    if (!new_block) {
        return NULL;
    }

    memcpy(new_block, block, orig_size);
    free2(block);

    return new_block;

}