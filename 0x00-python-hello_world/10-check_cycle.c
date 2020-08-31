#include "lists.h"
/**
 * check_cycle - Check if a single linked list has a cycle
 * @list: head of the linked list
 *
 * Return: 1 if the linked list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;
	listint_t *n;

	curr = list;
	n = curr->next;
	while (curr != NULL)
	{
		while (n != NULL)
		{
			if (curr == n->next)
				return (1);
			n = n->next;
		}
		curr = curr->next;
	}
	return (0);
}
