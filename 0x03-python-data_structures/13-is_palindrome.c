#include "main.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int array[1000]; /* Assuming the list has at most 1000 nodes */
	int size = 0, i;

	/* Store values of each node in an array */
	while (current != NULL)
	{
		array[size++] = current->n;
		current = current->next;
	}

	/* Compare values from both ends of the array inward */
	for (i = 0; i < size / 2; i++)
	{
		if (array[i] != array[size - 1 - i])
			return (0); /* Not a palindrome */
	}
	return (1); /* Palindrome */
}

