from tradedoubler_api_client import Tradedoubler
import pprint

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4, compact=True, sort_dicts=False)
    td = Tradedoubler('credentials.json')

    report = td.reporting().get_transactions(fromDate='20210601', toDate='20210610')

    report.filter_sales()
    report.csv(path='reports')

    for transaction in report.items:
        print(pp.pprint(transaction))
