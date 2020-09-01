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
	listint_t *back, *front, *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (number < (*head)->n)
	{
		new->next = *head, *head = new;
		return (new);
	}
	else if (number > (*head)->n && !(*head)->next)
	{
		(*head)->next = new, new->next = NULL;
		return (new);
	}
	back = *head, front = (*head)->next;
	while (front != NULL)
	{
		if (number > back->n && number < front->n)
		{
			back->next = new, new->next = front;
			return (new);
		}
		if (front->next == NULL)
		{
			front->next = new, new->next = NULL;
			return (new);
		}
		back = back->next, front = front->next;
	}
	return (NULL);
}
