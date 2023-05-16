#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 0 if the linked list is not a palindrome, else 1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	size_t size = 0;
	listint_t *current = *head;

	while (current != NULL)
	{
		size++;
		current = current->next;
	}

	current = *head;
	size_t middle = size / 2;

	for (size_t i = 0; i < middle - 1; i++)
		current = current->next;

	if (size % 2 == 0 && current->n != current->next->n)
		return (0);

	current = current->next->next;
	listint_t *reversed = reverse_listint(&current);
	listint_t *mid = reversed;

	current = *head;

	while (reversed != NULL)
	{
		if (current->n != reversed->n)
			return (0);
		current = current->next;
		reversed = reversed->next;
	}

	reverse_listint(&mid);

	return (1);
}
