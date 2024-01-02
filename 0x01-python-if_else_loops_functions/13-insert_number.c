#include "lists.h"

/**
 * insert_node - inserts number to linked lists(sorted)
 * @head: double pointer to head
 * @number: number to  be inserted
 * Return: address of new node (success) or NULL(fail)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	while (current->next != NULL)
	{
		/*insert at beginning*/
		if (number < current->n)
		{
			new_node->next = *head;
			*head = new_node;
			new_node->n = number;
			return (new_node);
		}
		/*duplicate numbers*/
		else if (number == current->n)
		{
			new_node->n = number;
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		/*insert at middle*/
		if ((number > current->n) && (current->next->n > number))
		{
			new_node->next = current->next;
			new_node->n = number;
			current->next = new_node;
			return (*head);
		}
		current = current->next;
	}
	if (number > current->n)
	{
		current->next = new_node;
		new_node->n = number;
		new_node->next = NULL;
		return (new_node);
	}

	return (NULL);
}
