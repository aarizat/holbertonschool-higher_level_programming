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
	back = *head;
	front = (*head)->next;
	while (front != NULL)
	{
		if (number >= back->n && number < front->n)
		{
			back->next = new;
			new->next = front;
			return (new);
		}
		back = back->next;
		front = front->next;
	}
	new->next = front;
	back->next = new;
	return (new);
}
