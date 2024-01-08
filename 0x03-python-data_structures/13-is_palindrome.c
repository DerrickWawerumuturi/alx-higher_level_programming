#include "lists.h"

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: double pointer to head
 * Return: int
 */

int is_palindrome(listint_t **head)
{
	listint_t *kich = *head;
	int i = 0, len;
	int a, b;
	int *mylist;
	int reversedList[100];

	if (*head == NULL)
	{
		return (1);
	}
	mylist = malloc(sizeof(int *));
	if (mylist == NULL)
	{
		return (0);
	}

	while (kich->next != NULL)
	{
		mylist[i] = kich->n;
		i++;
		kich = kich->next;
	}
	mylist[i] = kich->n;
	len = i + 1;

	for (a = len - 1, b = 0; a >= 0; a--, b++)
	{
		reversedList[b] = mylist[a];
	}
	for (a = 0; a < len; a++)
	{
		if (mylist[a] != reversedList[a])
		{
			return (0);
		}
	}
	return (1);
}

