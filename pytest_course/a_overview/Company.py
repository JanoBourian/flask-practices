class Company: 
    
    def __init__(self, name:str, stock_symbol:str) -> None:
        self.name = name
        self.stock_symbol = stock_symbol
    
    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"