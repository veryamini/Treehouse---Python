TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def calculate_price(num_tickets):
    return (TICKET_PRICE * num_tickets) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name:  ")
    try:
        number_of_tickets = int(input("How many tickets would you like, {}?  ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("We're sorry, there are only {} tickets available!".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We ran into an issue. {}. Try again...".format(err))
        # print("({})".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)
        print("The total due is ${}".format(amount_due))
        prompt = input("Do you want to procced to buy the tickets, {}?  Y/N  ".format(name))
        if prompt.lower() == "y":
            # TODO: Gather credit card information and process it
            print("The tickets have been SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyways, {}!".format(name))
    
        
    
print("Sorry, all the tickets have been sold out!")