class Employees: 
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last


class Supervisors(Employees):
    def __init__(self, name, last,password) -> None:
        ##Llama al constructor padre 
        super().__init__(name, last)
        self.password = password 

class Chefs(Employees):

    def leave_request(self,days): 
        return "May i take a leave for" + str(days) + "  days" 
    
adrian = Employees("Adrian","A") 

emily = Chefs("Adrian","A")
print(emily.leave_request(3))