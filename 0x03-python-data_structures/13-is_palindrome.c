#include "lists.h"

/**
 * reverse_linked_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Returns: Pointer to the new head of the reversed list.
 */
void reverse_linked_list(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 *
 * Returns: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *temp_ptr = *head;
	listint_t *reversed_ptr = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			reversed_ptr = slow_ptr->next;
			break;
		}
		if (!fast_ptr->next)
		{
			reversed_ptr = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}

	reverse_linked_list(&reversed_ptr);

	while (reversed_ptr && temp_ptr)
	{
		if (temp_ptr->n == reversed_ptr->n)
		{
			reversed_ptr = reversed_ptr->next;
			temp_ptr = temp_ptr->next;
		}
		else
			return (0);
	}

	if (!reversed_ptr)
		return 1;

    return (0);
}
