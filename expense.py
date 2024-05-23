class Expense:
    def __init__(self,name,category,amount,paymode) -> None:
        self.name=name
        self.category=category
        self.amount=amount
        self.paymode=paymode

# This repr class helps to print out the values in string format 
    def __repr__(self):
        return f"<Expense: {self.name},{self.category}, ${self.amount:.2f},{self.paymode} >"
    

    