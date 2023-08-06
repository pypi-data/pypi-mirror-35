from cloudcix.client import Client


class Membership:
    """
    Membership is a CloudCIX Application that exposes a REST API capable of managing CloudCIX Members and relationships
    between those Members
    """
    _application_name = 'Membership'
    address = Client(
        _application_name,
        'Address/',
    )
    address_link = Client(
        _application_name,
        'Address/{address_id}/Link/',
    )
    country = Client(
        _application_name,
        'Country/',
    )
    currency = Client(
        _application_name,
        'Currency/',
    )
    department = Client(
        _application_name,
        'Member/{member_id}/Department/',
    )
    language = Client(
        _application_name,
        'Language/',
    )
    member = Client(
        _application_name,
        'Member/',
    )
    member_link = Client(
        _application_name,
        'Member/{member_id}/Link/',
    )
    notification = Client(
        _application_name,
        'Address/{address_id}/Notification/',
    )
    profile = Client(
        _application_name,
        'Member/{member_id}/Profile/',
    )
    subdivision = Client(
        _application_name,
        'Country/{country_id}/Subdivision/',
    )
    team = Client(
        _application_name,
        'Member/{member_id}/Team/',
    )
    territory = Client(
        _application_name,
        'Member/{member_id}/Territory/',
    )
    timezone = Client(
        _application_name,
        'Timezone/',
    )
    transaction_type = Client(
        _application_name,
        'TransactionType/',
    )
    user = Client(
        _application_name,
        'User/',
    )
