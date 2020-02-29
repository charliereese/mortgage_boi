class Mortgage:
    
    def __init__(self, principal, apr, n=25, **kwargs):
        self.principal = principal
        self.apr = apr # annual percentage rate
        self.n = 25 # years
        
        self.months = self.n * 12
        self.ear = ((1 + apr / 2) ** 2) - 1 # effective annual rate: compounds semi-annually
        self.emr = ((1 + self.ear) ** (1 / 12)) - 1 # effective monthly rate

    @property
    def monthly_payment(self):
        numerator = (
            self.principal * (
                self.emr * (1 + self.emr) ** self.months        
            )
        )
        denominator = ((1 + self.emr) ** self.months) - 1 

        return numerator / denominator

    @property
    def payments(self):
        payments = []
        
        for i in range(self.months):
            if i == 0:
                balance_start = self.principal
            else: 
                balance_start = payments[i - 1]['balance_end']
            
            interest = balance_start * self.emr
            principal = self.monthly_payment - interest
            obj = {
                'balance_start': balance_start,
                'balance_end': balance_start - principal,
                'interest': interest,
                'principal': principal,
            }
            
            payments.append(obj)
        
        return tuple(payments)
