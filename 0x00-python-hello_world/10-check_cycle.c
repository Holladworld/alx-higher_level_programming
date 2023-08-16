#include "lists.h"
/**
 * check_cycle - checks for linked list containing circle
 * @list: linked list
 * Return: 1 if the list has 0, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ccheck = list;
	listint_t *ccfast = list;


	while (ccheck && ccfast && ccfast->next)
	{
		ccheck = ccheck->next;
		ccfast = ccfast->next->next;

		if (ccheck == ccfast)
			return (1);
	}
	if (list == NULL)
		return (0);
	return (0);
}
