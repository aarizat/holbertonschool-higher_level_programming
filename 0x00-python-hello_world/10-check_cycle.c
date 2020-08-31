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

	if (list == NULL)
		return (0);
	n = list->next;
	while (list != NULL)
	{
		while (n != NULL)
		{
			if (n->next == NULL)
				return (0);
			if (list == n->next)
				return (1);
			n = n->next;
		}
		list = list->next;
	}
	return (0);
}
