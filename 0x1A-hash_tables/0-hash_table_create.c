#include "hash_tables.h"
/**
 * hash_table_create - Creates a hash table
 * @size: The size of the array
 * Return: A pointer to the newly created hash table, or NULL if something
 * went wrong
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *h_table = NULL;
	unsigned long int x;

	/* Allocate memory for the hash table */
	h_table = malloc(sizeof(hash_table_t));
	if (h_table == NULL)
		return (NULL);

	/* Allocate memory for the array of hash nodes */
	h_table->array = malloc(sizeof(hash_node_t *) * size);
	if (h_table->array == NULL)
	{
		free(h_table);
		return (NULL);
	}

	/* Initialize each element of the array to NULL */
	for (x = 0; x < size; x++)
		h_table->array[x] = NULL;

	h_table->size = size;
	return (h_table);
}
