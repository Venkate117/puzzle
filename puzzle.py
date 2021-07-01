import json

class Data:        
    def finder(self,values, i, Sum, temp):
        if i >= len(values): return 1 if Sum == 0 else 0
        if (i, Sum) not in temp:  
            count = self.finder(values, i + 1, Sum, temp)
            count += self.finder(values, i + 1, Sum - values[i], temp)
            temp[(i, Sum)] = count 
        return temp[(i, Sum)] 
    
    def getter(self,values, Sum, temp):
        subset = []
        for i, x in enumerate(values):
            if self.finder(values, i + 1, Sum - x, temp) > 0:
                subset.append(x)
                Sum -= x
        return subset
       
    def findCombination(self,input):
        target_price=input.get('target-price')
        dishes=input.get('dishes')[0]
        values=[]
        for key in dishes.keys(): 
            values.append(dishes.get(key))   
        temp = dict()
        if self.finder(values, 0, target_price, temp) == 0: 
            print(f'There is no correct combination that adds up to '+str(target_price))
        else: 
            results=self.getter(values, target_price, temp)
            print("Possible combinations for target price ($"+str(target_price)+") are: \n")
            for key in dishes.keys():
                if dishes.get(key) in results:
                    print(key+" $"+str(dishes.get(key))+"\n")
                     

if __name__ == '__main__':            
    # Open the JSON file
    dataFile = open('input.json',"r")

    input = json.load(dataFile)

    rawInput=input.get('data')
    data=Data()
    data.findCombination(rawInput)

    # Close the file
    dataFile.close()
