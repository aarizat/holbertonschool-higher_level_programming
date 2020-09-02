#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the linked list.
 * @number: integer number to insert in the linked list.
 *
 * Return: Address memory of the node inserted.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	curr = *head;
	while (curr->next != NULL)
	{
		if (number >= curr->n && curr->next->n >= number)
		{
			new->next = curr->next;
			curr->next = new;
			return (new);
		}
		curr = curr->next;
	}
	new->next = curr->next;
	curr->next = new;
	return (new);
}
