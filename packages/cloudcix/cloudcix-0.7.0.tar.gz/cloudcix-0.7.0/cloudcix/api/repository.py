from cloudcix.client import Client


class Repository:
    """
    The Repository Application is a software system that manages
    CloudCIX Software Projects

    Projects in the Repository are grouped by the owning Member
    """
    _application_name = 'SupportFramework'

    application = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Application/',
    )
    dto = Client(
        application=_application_name,
        service_uri='DTO/',
    )
    dto_parameter = Client(
        application=_application_name,
        service_uri='DTO/{dto_id}/Parameter/',
    )
    exception_code = Client(
        application=_application_name,
        service_uri='ExceptionCode/',
    )
    language_exception_code = Client(
        application=_application_name,
        service_uri='ExceptionCode/{exception_code}/Language/',
    )
    member = Client(
        application=_application_name,
        service_uri='Member/',
    )
    method = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Application/{application_id}/Service/{service_id}/Method/',
    )
    method_parameter = Client(
        application=_application_name,
        service_uri=(
            'Member/{member_id}/Application/{application_id}/Service/{service_id}/Method/{method_id}/Parameter/'
        ),
    )
    service = Client(
        application=_application_name,
        service_uri='Member/{member_id}/Application/{application_id}/Service/',
    )
