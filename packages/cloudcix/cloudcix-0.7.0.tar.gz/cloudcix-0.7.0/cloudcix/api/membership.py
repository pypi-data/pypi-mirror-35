from cloudcix.client import Client


class Membership:
    """
    Membership is a CloudCIX Application that exposes a REST API capable of
    managing CloudCIX Members and relationships between those Members
    """
    _application_name = 'Membership'
    address = Client(
        application=_application_name,
        service_uri='Address/',
    )
    address_link = Client(
        application=_application_name,
        service_uri='Address/{address_id}/Link/',
    )
    country = Client(
        application=_application_name,
        service_uri='Country/',
    )
    currency = Client(
        application=_application_name,
        service_uri='Currency/',
    )
    department = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Department/',
    )
    language = Client(
        application=_application_name,
        service_uri='Language/',
    )
    member = Client(
        application=_application_name,
        service_uri='Member/',
    )
    member_link = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Link/',
    )
    notification = Client(
        application=_application_name,
        service_uri='Address/{address_id}/Notification/',
    )
    profile = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Profile/',
    )
    subdivision = Client(
        application=_application_name,
        service_uri='Country/{country_id}/Subdivision/',
    )
    team = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Team/',
    )
    territory = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Territory/',
    )
    timezone = Client(
        application=_application_name,
        service_uri='Timezone/',
    )
    transaction_type = Client(
        application=_application_name,
        service_uri='TransactionType/',
    )
    user = Client(
        application=_application_name,
        service_uri='User/',
    )
