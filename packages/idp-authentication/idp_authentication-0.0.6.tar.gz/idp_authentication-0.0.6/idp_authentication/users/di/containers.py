from dependency_injector import containers, providers

from idp_authentication.users.adapters import unit_of_work
from idp_authentication.users.adapters.orm import start_mappers
from idp_authentication.users.domain import use_cases


class UsersModuleUseCasesDIContainer(containers.DeclarativeContainer):
    """Dependency injection container for use cases."""

    config = providers.Configuration(strict=True)
    users_unit_of_work = providers.Dependency()
    app_entities_unit_of_work = providers.Dependency()
    auth_unit_of_work = providers.Dependency()
    event_producer = providers.Dependency()
    get_user_use_case = providers.Factory(
        use_cases.GetUserUseCase,
        users_unit_of_work=users_unit_of_work,
    )
    create_or_update_user_use_case = providers.Factory(
        use_cases.CreateOrUpdateUserUseCase,
        users_unit_of_work=users_unit_of_work,
    )
    authorize_app_entity_records_use_case = providers.Factory(
        use_cases.AuthorizeEntityRecordsUseCase,
        users_unit_of_work=users_unit_of_work,
        app_entities_unit_of_work=app_entities_unit_of_work,
        roles=config.ROLES,
    )
    get_allowed_app_entity_records_use_case = providers.Factory(
        use_cases.GetAllowedAppEntityRecordsUseCase,
        users_unit_of_work=users_unit_of_work,
        app_entities_unit_of_work=app_entities_unit_of_work,
        roles=config.ROLES,
    )
    authorize_and_get_records_or_get_all_allowed_use_case = providers.Factory(
        use_cases.AuthorizeAndGetRecordsOrGetAllAllowedUseCase,
        users_unit_of_work=users_unit_of_work,
        app_entities_unit_of_work=app_entities_unit_of_work,
        roles=config.ROLES,
        authorize_app_entity_records_use_case=authorize_app_entity_records_use_case,
        get_allowed_app_entity_records_use_case=get_allowed_app_entity_records_use_case,
    )
    get_users_with_access_to_app_entity_record_use_case = providers.Factory(
        use_cases.GetUsersWithAccessToAppEntityRecordUseCase,
        app_entities_unit_of_work=app_entities_unit_of_work,
        users_unit_of_work=users_unit_of_work,
        roles=config.ROLES,
    )
    process_user_message_use_case = providers.Factory(
        use_cases.ProcessUserMessageUseCase,
        users_unit_of_work=users_unit_of_work,
        app_entities_unit_of_work=app_entities_unit_of_work,
        roles=config.ROLES,
        create_or_update_user_use_case=create_or_update_user_use_case,
        tenants=config.TENANTS,
        app_identifier=config.APP_IDENTIFIER,
    )
    send_app_entity_record_event_use_case = providers.Factory(
        use_cases.SendAppEntityRecordEventUseCase,
        event_producer=event_producer,
        app_identifier=config.APP_IDENTIFIER,
    )


class UsersModuleDIContainer(containers.DeclarativeContainer):
    """Dependency injection container for users module."""

    config = providers.Configuration(strict=True)
    database = providers.Dependency()
    app_entities_unit_of_work = providers.Dependency()
    event_producer = providers.Dependency()
    auth_unit_of_work = providers.Factory(
        unit_of_work.AuthUnitOfWork,
        session=database.provided.session,
    )
    users_unit_of_work = providers.Factory(
        unit_of_work.UsersUnitOfWork,
        session=database.provided.session,
    )
    use_cases = providers.Container(
        UsersModuleUseCasesDIContainer,
        users_unit_of_work=users_unit_of_work,
        app_entities_unit_of_work=app_entities_unit_of_work,
        auth_unit_of_work=auth_unit_of_work,
        config=config,
        event_producer=event_producer,
    )
    start_mappers = providers.Callable(
        start_mappers,
        send_event_use_case=use_cases.send_app_entity_record_event_use_case,
    )
