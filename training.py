"""
new = [110, 150, 5] 
old = [100, 200,0]

def main():
    print(percent_change(old, new))



def percent_change(old,new):
    percentage_change = []
    for i in range(len(old)):
        if old[i] == 0:
            percentage_change.append(None)
        else:
            percentage_change.append((new[i]-old[i]) / old[i] * 100)

    return percentage_change

main()

"""

"""
def main():
    print(position_size(10000, 1, 50, 48))   # 50.0
    print(position_size(5000, 2, 100, 95))   # 20.0
    print(position_size(1000, 1, 10, 10))    # None

def position_size(balance, risk_pct, entry, stop):
    if entry == stop:
        return None
    
    risk_amount = balance * risk_pct / 100# if price comes to stop price we gonna lose how much money?
    unit_risk = abs(entry - stop)

    return risk_amount/unit_risk




main()
    
    


def main():
    print(classify_return(7))
    print(classify_return(5))
    print(classify_return(0))
    print(classify_return(-5))
    print(classify_return(-5.1))


def classify_return(r):
    if r < -5:
        return "strong_up"
    elif -5<=r<0: 
        return "up"
    elif r==0:
        return "flat"
    elif 0<r<=5:
        return "down"
    else:
        return "strong_down"


main()




def main():
    print(is_leap_year(2023))
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))

def is_leap_year(year):

    if year%4== 0 and year%100 != 0 or year % 400 == 0:
        return "leap year"
    else:
        return "not leap year"
    



main()








def main():
    print(count_up_days(prices = [100, 102, 101, 105, 105, 107]))
    print(count_up_days([5]))

def count_up_days(prices):
    count_up_day = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            count_up_day+=1
        else:
            continue
    
    return count_up_day
main()



def main():
    print(running_max(prices=[3, 1, 4, 1, 5, 9, 2, 6]))

def running_max(prices):
    current_max = prices[0]
    currents_max = []
    for prices in prices:
        if current_max >= prices:
            prices = current_max
            currents_max.append(prices)
        elif current_max < prices:
            current_max = prices
            currents_max.append(prices)
            
    return currents_max
main()




def main():
    print(moving_average([1, 2, 3, 4, 5, 6], 3))
    print(moving_average([1, 2], 3))


def moving_average(prices,window):
    moving_averages = []
    for i in range(len(prices) - window + 1):
        window_total = 0
        for j in range(i, i + window):
            window_total += prices[j]
        moving_averages.append(window_total / 3)


    return moving_averages


main()





def main():
    print(doubling_time(2))
    print(doubling_time(100))


def doubling_time(rate_pct):
    balance = 1
    steps = 0 
    while balance < 2:
        balance=balance*(1+rate_pct/100)
        steps +=1
        

    return steps

main()





def main():
    print(longest_losing_streak(prices=[10, 9, 8, 9, 8, 7, 6, 7]))
    print(longest_losing_streak(prices=[1,2,3]))

def longest_losing_streak(prices):
    current_streak = 0
    longest_streak = 0
    for i in range(1,len(prices)):
        if prices[i]<prices[i-1]:
            current_streak +=1
            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 0
    return longest_streak


main()
"""
