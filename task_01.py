#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 Synthesizing task 1"""


def sum_orders(customers, orders):
    """This function combines data functions.
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
                      3: {'customer_id': 2, 'total': 10},
                      4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                         3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
             'email': 'email@one.com',
             'orders': 2,
             'total': 20}
        3: {'name': 'Person Two',
            'email': 'email@two.com',
            'orders': 1,
            'total': 15}}
    """
    dictionary = {}
    orders = orders.values()
    for order in orders:
        key = order['customer_id']
        val1 = customers[key]['name']
        val2 = customers[key]['email']
        if key not in dictionary.iterkeys():
            val3 = 1
            val4 = order['total']
        else:
            val3 = dictionary[key]['orders'] + 1
            val4 = dictionary[key]['total'] + order['total']
        information = dict(name=val1, email=val2, orders=val3, total=val4)
        order_customer_info = {key: information}
        dictionary.update(order_customer_info)

    return dictionary
