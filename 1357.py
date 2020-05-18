class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.products=products
        self.discount=discount
        self.prices=prices
        self.count=0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill=0
        self.count=self.count+1
        if self.count==self.n:
            for i in range(0,len(product)):
                ind=self.products.index(product[i])
                p=self.prices[ind]
                bill=bill+(p * amount[i])
            bill=(bill-(self.discount*bill)/100)
            self.count=0
            return bill
        
        for i in range(0,len(product)):
            ind=self.products.index(product[i])
            p=self.prices[ind]
            bill=bill+(p * amount[i])
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
