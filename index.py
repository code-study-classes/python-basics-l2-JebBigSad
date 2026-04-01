# 1=====================
def update_profile(user_id, **kwargs):
    return {
        'updated_fields': kwargs,
        'id': user_id
    }

# 2=====================

def get_domains(emails):
    return [email.split('@')[1] for email in emails]

# 3===============

def filter_target_audience(users):
    return list(filter(lambda user: user['age'] >= 18 and user['is_premium'],uers))

# 4========================

def build_response(status_code, *errors, **payload):
    return {
        'status': status_code,
        'errors': errors,
        'data': payload
    }

# 5===================

def calculate_total_spent(transactions):
    total = 0
    for transaction in transactions:
        total += transaction['amount']
    return total
