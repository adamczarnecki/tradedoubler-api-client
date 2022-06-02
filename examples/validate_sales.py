from tradedoubler_api_client import Tradedoubler
import pprint


def check_transaction(transaction):
    # some logis
    if transaction == 'good':
        return True, 0
    elif transaction == 'not good':
        return False, 10
    else:
        return 'do logic here'


def other_logic(faild_update):
    error = faild_update['error']['message']
    if error == 'fixable':
        return 'we cad do it!'
    return 'i dunno, bro'


if __name__ == '__main__':

    pp = pprint.PrettyPrinter(indent=4)
    td = Tradedoubler('credentials.json')

    pending_sales = td.pending_sales()
    list_pendint_sales = td.pending_sales().get_all()
    list_pendint_sales.csv(path='csv')
    list_pendint_sales.json(path='json')

    sales_to_updates = []

    for transaction in list_pendint_sales.items():
        validation, reason = check_transaction(transaction)
        if validation:
            sales_to_updates.append(pending_sales.prep_approve(transaction))
        else:
            sales_to_updates.append(pending_sales.prep_deny(transaction, reason=reason))

    update_report = pending_sales.update_sales(sales_to_updates)
    update_report.csv(path='update_reports')        # report with fails by default
    update_report.json(path='jsons', status='all')  # other status "success"

    fails = update_report.fails

    for faild_update in fails:
        if transaction.status == -1:
            next_steps = other_logic(faild_update)
            print(next_steps)

    success = update_report.success

    for succeeded_update in success:
        print(f'Yeeee {succeeded_update["transactionId"]}, no idea why')
