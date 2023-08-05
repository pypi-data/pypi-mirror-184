import numpy as np
from typing import List, Tuple
from datetime import datetime, timedelta
class asset:
    def __init__(self, name: str, value: float, category =None):
        self.name = name
        self.category = category
        self.value = value
    
    def __repr__(self):
        return f"Asset({self.name}, {self.category}, {self.value})"
    
    def total_value(assets):
        """Calculates the total value of a list of assets."""
        total = 0
        for asset in assets:
            total += asset.value
        return total
    
    def generate_report(assets):
        """Generates a report with information about a list of assets."""
        report = "ASSET REPORT\n"
        for i in assets:
            report += f"{i.name} ({i.category}): ${i.value}\n"
        report += f"Total value: ${asset.total_value(assets)}"
        return report
    def makemoney(self):
        a = np.random.uniform(-1, 1)
        self.value *= (1+a)
        if a >0:
            print(self.name,"is making big money",self.value)
        else:
            print(self.name,"is losing money",self.value)
class bankdeposit(asset):
    def __init__(self, name: str, value: float, interest_rate: float, category =None):
        super().__init__(name, category, value)
        self.interest_rate = interest_rate

    def get_interest_earned(self, start_date: str, end_date: str) -> float:
        return (end_date - start_date).days * self.interest_rate * self.value
class realestate(asset):
    def __init__(self, name, value, address, category =None):
        super().__init__(name, category, value)
        self.address = address
    
    def __str__(self):
        return f"RealEstate(name='{self.name}', value={self.value}, address='{self.address}')"
#金融资产的交易性金融资产是指具有流动性和可转移性的金融资产，如股票、债券、期货和外汇等。
class stock(asset):
    def __init__(self, name, category, value, symbol, market):
        super().__init__(name, category, value)
        self.symbol = symbol
        self.market = market
    def sell(self, amount):
        if amount > self.value:
            raise ValueError("Cannot sell more than the current value of the asset.")
        self.value -= amount
    
    def buy(self, amount):
        self.value += amount
    
    def __str__(self):
        return f"Stock(name='{self.name}', value={self.value}, symbol='{self.symbol}', market='{self.market}')"
class assetdepreciation:
    def __init__(self, cost, salvage_value, life):
        self.cost = cost
        self.salvage_value = salvage_value
        self.life = life

    def straight_line_depreciation(self):
        annual_depreciation = (self.cost - self.salvage_value) / self.life
        return annual_depreciation
class assetamortization(assetdepreciation):
    def __init__(self, cost, salvage_value, life, rate):
        super().__init__(cost, salvage_value, life)
        self.rate = rate

    def get_amortization_schedule(self):
        schedule = []
        annual_depreciation = self.straight_line_depreciation()
        for year in range(1, self.life + 1):
            amortization = self.cost * self.rate
            depreciation = annual_depreciation
            self.cost -= (amortization + depreciation)
            schedule.append((year, amortization, depreciation))
        return schedule
class assetbubble:
    def is_asset_bubble(self, price: float) -> bool:
        return price > 100
class transaction:
    def __init__(self, item: str, cost: float, quantity: int):
        self.item = item
        self.cost = cost
        self.quantity = quantity

class costaccounting:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: transaction):
        self.transactions.append(transaction)

    def get_cost(self, item: str) -> float:
        cost = 0
        for transaction in self.transactions:
            if transaction.item == item:
                cost += transaction.cost * transaction.quantity
        return cost
class investment:
    def __init__(self, date: str, value: float):
        self.date = date
        self.value = value

class equityinvestmentaccounting:
    def __init__(self):
        self.investments = []

    def add_investment(self, investment: investment):
        self.investments.append(investment)

    def get_value(self, date: str) -> float:
        value = 0
        for investment in self.investments:
            if investment.date <= date:
                value += investment.value
        return value

    def get_return(self, start_date: str, end_date: str) -> float:
        start_value = self.get_value(start_date)
        end_value = self.get_value(end_date)
        return (end_value - start_value) / start_value
class financialasset(asset):
     def __init__(self, name, value, date: str,category="financialasset"):
         super().__init__(name, value,category)
         self.date = date
         self.accumulated_impairment = 0
    
     def calculate_impairment(self):
            # 假设减值准备的计算方式为财务资产的净值减去其市场价值
            net_value = self.value  # 假设财务资产的净值为其当前价值
            market_value = 100  # 假设财务资产的市场价值为 100
            impairment = net_value - market_value
            if impairment > 0:
                self.accumulated_impairment += impairment
        
     def __str__(self):
            return f"{self.name}: {self.value} (Accumulated Impairment: {self.accumulated_impairment})"
#计提减值准备是指企业在报告期内根据财务报表计算，为了体现财务资产减值而发生的费用。减值准备通常是在财务资产出现损失时进行计提。
class financialassetaccounting:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset: financialasset):
        self.assets.append(asset)

    def get_value(self, date: str) -> float:
        value = 0
class fairvaluefinancialasset(financialasset):
    def update_value(self, value: float):
        self.value = value
class DividendReceivable(financialasset):
    def __init__(self, name, value, date,category,company, amount):
         super().__init__(self, name, value, date,category)
         self.company = company
         self.amount = amount

a = asset("股票",500)
a.makemoney()