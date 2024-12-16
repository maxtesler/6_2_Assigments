from decorators.task1 import is_admin

@is_admin
def show_customer_receipt(user_type: str):
    return 1+1

show_customer_receipt(user_type='admin')
