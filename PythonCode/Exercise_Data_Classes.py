from dataclasses import dataclass, field

@dataclass
class Order:
    def __gt__(self, other):
        return self.OrderID > other.OrderID

    def __ge__(self, other):
        return self.OrderID >= other.OrderID

    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: str
    ExpectedDeliveryDate: str
    CustomerPurchaseOrderNumber: int
    IsUndersupplyBackordered: int
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: str
    LastEditedBy: int
    LastEditedWhen: str