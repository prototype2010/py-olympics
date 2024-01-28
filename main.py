import parser
from database.Connection import Connection
from entities.factories import sports_factory,results_factory,games_factory, events_factory, athletes_factory, teams_factory


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser.parse()
    Connection().drop_all_existing()

    for result in results_factory.results_factory.register:
        result.save()
        print('saving result ' + result._db_id.__str__())

