#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half = NULL;
    listint_t *prev_slow = *head;
    listint_t *mid = NULL;
    int result = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            mid = slow;
            slow = slow->next;
        }

        second_half = reverse(&slow);
        result = compareLists(*head, second_half);

        reverse(&second_half);

        if (mid != NULL)
        {
            prev_slow->next = mid;
            mid->next = second_half;
        }
        else
            prev_slow->next = second_half;
    }

    return result;
}

/**
 * reverse - reverses a linked list
 * @head_ref: pointer to the head of the linked list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse(listint_t **head_ref)
{
    listint_t *prev = NULL;
    listint_t *current = *head_ref;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head_ref = prev;
    return *head_ref;
}

/**
 * compareLists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compareLists(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1;
    listint_t *temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n == temp2->n)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else
            return 0;
    }

    if (temp1 == NULL && temp2 == NULL)
        return 1;

    return 0;
}
