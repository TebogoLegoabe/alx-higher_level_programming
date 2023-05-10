#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: number to insert.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *previous_node = NULL;

	listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	while (current_node != NULL && current_node->n < number)
	{
	previous_node = current_node;
	current_node = current_node->next;
	}

	if (previous_node == NULL)
	{
	*head = new_node;
	}
	else
	{
	previous_node->next = new_node;
	}

	new_node->next = current_node;

	return (new_node);
}
}
