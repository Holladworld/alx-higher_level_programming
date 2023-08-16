#include "lists.h"
/**
 * check_cycle - checks for linked list containing circle
 * @list: linked list
 * Return: 1 if the list has 0, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ccheck = list->next;

	while (ccheck != NULL)
	{
		if (ccheck == list)
			return (1);
		ccheck = ccheck->next;
	}
	if (list == NULL)
		return (0);
	return (0);
}
