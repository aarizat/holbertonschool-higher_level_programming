#include "lists.h"
/**
 * check_cycle - Check if a single linked list has a cycle
 * @list: head of the linked list
 *
 * Return: 1 if the linked list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tor;
	listint_t *con;

	if (!list || !list->next)
		return (0);
	tor = list;
	con = tor->next->next;
	while (con != NULL && con->next)
	{
		if (tor == con)
			return (1);
		tor = tor->next;
		con = con->next->next;
	}
	return (0);
}
