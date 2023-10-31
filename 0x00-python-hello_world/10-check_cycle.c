#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *s = list, *f = list;

    while (s && f && f->next)
    {
        s = s->next;
        f = f->next->next;

        if (s == f)
            return (1);
    }

    return (0);
}
