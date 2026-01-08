from dataclasses import dataclass
from enum import Enum

from domain.operation_type import OperationType
from domain.stock import Stock

"""
    clase que define una transaccion de compra o venta
"""


@dataclass(frozen=True)
class Operation:
    type: OperationType
    stock: Stock
    quantity: int
