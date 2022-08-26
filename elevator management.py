class ElevatorManager:
    def __init__(self):
        #contains currently requested floors with their cost
        self.cost_requested={}
        #contains requested floors
        self.current_requested=[]
        #current position of the Elevator:we assume it is initialy ground floor
        self.position=1
    def cost_floor(self,floor):
        # we assume it takes 10 sec to go from one floor to the other
        cost=(floor-self.position)*10
        return cost
    def request(self,floor):
        self.current_requested.append(floor)
    def serve(self,floor):
        self.position=floor
        self.current_requested.remove(floor)
        del self.cost_requested[floor]
        for floor in self.cost_requested:
           self.cost_requested[floor] =self.cost_requested[floor]-5

    def floor_selctor(self):
        while (self.current_requested!=[]):
            temp=[]


            for floor in self.current_requested:
                cost=self.cost_floor(floor)

                self.cost_requested[floor]=cost
                temp.append(self.cost_requested[floor])
            temp.sort()


            for floor in self.current_requested:
                if self.cost_requested[floor]==temp[0]:

                    self.serve(floor)
                    print(temp)
                    temp.remove(temp[0])
                    print(floor)
                    print(self.cost_requested)

                    break



        return self.position
elevate=ElevatorManager()
elevate.request(20)
elevate.request(4)
elevate.request(5)
elevate.request(1)
elevate.request(10)
elevate.request(6)
elevate.request(9)
elevate.request(12)
elevate.request(15)
print(elevate.floor_selctor())
