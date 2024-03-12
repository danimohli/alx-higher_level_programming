#include "lists.h"
/**
 * insert_node - insert node
 * @head: head pointer
 * @number: place of insertion
 * Return: address of node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL); /* Memory allocation failed */

	node->n = number;
	node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		/* Insert at the beginning of the list */
		node->next = *head;
		*head = node;
		return (node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	/* Insert in the middle or at the end of the list */
	node->next = current->next;
	current->next = node;

	return (node);
}
