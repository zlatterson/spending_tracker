from datetime import datetime
from operator import attrgetter

# from controllers.item_controller import transaction

class Transaction:
    def __init__(self,merchant,user,item,cost,time=None,id=None):
        self.merchant = merchant
        self.user = user
        self.item = item
        self.cost = cost
        self.time = time
        self.id = id
    
    def sort_by_user(transactions,userid):
        user_transactions = []
        for transaction in transactions:
            if transaction.user.id == userid:
                user_transactions.append(transaction)
        return user_transactions

    def sort_by_time(transactions):
        sorted_list = sorted(transactions, key=attrgetter('time'),reverse=True)
        return sorted_list

    def sort_by_month(transactions,year,month):
        # Filter by year
        by_year=[]
        for transaction in transactions:
            if transaction.time[0:4] == year:
                by_year.append(transaction)
                #  finds only those with the same year
        by_month=[]
        for transaction in by_year:
            if transaction.time[5:7] == month:
                by_month.append(transaction)
        return by_month

    def find_monthly_expendature(month_transactions):
        amount = 0
        for transaction in month_transactions:
            amount += transaction.item.cost
        return amount

    # Two functions with two varaibles, one will return None. To bypass pure HTML restrictions

    def green_text(month_cur,month_max):
        value = ""
        if month_cur < month_max:
            value = "£"+str(month_cur)+"/"
        return value


    def red_text(month_cur,month_max):
        value = ""
        if month_cur > month_max:
            value = "£"+str(month_cur)+"/"
        return value


    def find_tag_total(tags):
        tags_total = 0
        for tag in tags:
            tags_total += tag.times_used
        return tags_total


    def change_transaction_object_tag_into_percentage(transactions,tag_total):
        for transaction in transactions:
            transaction.item.tag.times_used = round(transaction.item.tag.times_used / tag_total * 100)
        return transactions
