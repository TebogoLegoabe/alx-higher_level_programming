#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tail = list;

	if (!list)
		return (0);

	while (head && tail && tail->next)
	{
		head = head->next;
		tail = tail->next->next;
		if (head == tail)
			return (1);
	}

	return (0);
}
