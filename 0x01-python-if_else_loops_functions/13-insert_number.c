#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * insert_node - function to insert node in sorted list
 * @head: double pointer of listint_t type
 * @number: int
 * Return: adress of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *node_new, *current;

	node_new = malloc(sizeof(listint_t));

	if (node_new == NULL)
	{
		return (NULL);
	}
	node_new->n = number;
	node_new->next = NULL;

	if (*head == NULL)
	{
		*head = node_new;
		node_new->next = NULL;
		return (node_new);
	}
	
	current = *head;	

	while (current->next != NULL)
	{
		if (number < current->n)
		{
			node_new->next = current;
			*head = node_new;
			return (node_new);
		}
		if (number <= current->next->n)
		{
			node_new->next = current->next;
			current->next = node_new;
			return (node_new);
		}
		current = current->next;
	}

	node_new->next = NULL;
	current->next = node_new;

	return (node_new);
}
