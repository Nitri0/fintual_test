
from enum import Enum

from domain.stock import Stock

"""
    clase que define una transaccion de compra o venta
"""
class Operation:
    type: OperationType
    stock: Stock
    quantity: int
