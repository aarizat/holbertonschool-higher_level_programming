#include "lists.h"
/**
 * check_cycle - Check if a single linked list has a cycle
 * @list: head of the linked list
 *
 * Return: 1 if the linked list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *n;
	listint_t *c;

	if (!list || !list->next)
		return (0);
	c = list;
	while (c != NULL)
	{
		n = c->next;
		while (n != NULL)
		{
			if (c == n->next)
				return (1);
			n = n->next;
		}
		c = c->next;
	}
	return (0);
}
