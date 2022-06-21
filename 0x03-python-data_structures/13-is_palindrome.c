#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *back;
	listint_t *temp;
	int count;

	if (!head || !*head)
		return (1);

	current = *head;
	back = NULL;
	count = 0;

}
