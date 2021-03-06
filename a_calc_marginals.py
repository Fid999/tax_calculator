from tax_law_uk_2019_2020 import uk_law as law

#Income Tax Calculator
class marginal_calc:
    
    def __init__(self,value,list_type):
        
        self.value = value
        self.list_type = list_type
    
    def calculate(self):
        
        threshold_list = []
        percentage_list = []
        
        if self.list_type == 0:
            threshold_list = law.tax_b
            percentage_list = law.tax_pc
        elif self.list_type == 2:
            threshold_list = law.law_list[self.list_type]
            percentage_list = law.law_list[self.list_type + 1]
        elif self.list_type == 4:
            threshold_list = law.law_list[self.list_type]
            percentage_list = law.law_list[self.list_type + 1]
        elif self.list_type == 6:
            threshold_list = law.law_list[self.list_type]
            percentage_list = law.law_list[self.list_type + 1]
        elif self.list_type == 8:
            threshold_list = law.law_list[self.list_type]
            percentage_list = law.law_list[self.list_type + 1]
        elif self.list_type == 10:
            threshold_list = law.law_list[self.list_type]
            percentage_list = law.law_list[self.list_type + 1]
        elif self.list_type == 12:
            threshold_list = law.law_list[self.list_type]
            percentage_list = law.law_list[self.list_type + 1]
        else:
            return("Error: Insert Correct Threshold List Value")
        
        bracket = threshold_list
        percentage = percentage_list
            
        bracket.append(self.value)

        bracket = [num for num in bracket if num <= self.value]
        
        bracket = list(set(bracket)) 
        
        bracket.sort()
        
        
        lst = []
        
        index = 0
        while index < len(bracket):
            a = index
            if index > 0:
                b = (bracket[a]-bracket[a-1] )* percentage[a-1]
                lst.append(b)
                
            index = index + 1
        return(sum(lst))