from tax_law_uk_2019_2020 import uk_law as law

class new_allowance:
    
    def __init__(self,gross):
        
        self.gross = gross
        
    def calculate(self):
        
        a = law.tax_b
        
        tf_ch = law.acv
        
        ratio = law.acv_ratio
        
        if self.gross > tf_ch:
            if self.gross < (tf_ch + 2*a[1]):
        
                tf_amount = self.gross - tf_ch
        
                tf_reduction = tf_amount/ratio
        
                a[1] = a[1] - tf_reduction
            else:
                a[1] = 0
        
        return(a[1])


