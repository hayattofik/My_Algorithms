class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #initialize the number of returned values
        preLi = [0] * n

        for start,end ,seats in bookings:
        
            
            preLi[start-1]+=seats
           
            if end < n:
                # this is done to avoid adding the seats 2x
                preLi[end]-=seats
        #this is done because it is inclusive
        for i in range(1,len(preLi)):
            preLi[i]+=preLi[i-1]
        return preLi