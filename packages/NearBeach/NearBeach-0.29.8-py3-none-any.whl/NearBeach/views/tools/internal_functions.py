from NearBeach.models import (
    customer,
    kanban_board,
    kanban_card,
    organisation,
    project,
    request_for_change,
    requirement,
    requirement_item,
    task,
    user_group,
)

OBJECT_DICT = {
    "customer": customer.objects,
    "project": project.objects,
    "task": task.objects,
    "requirement": requirement.objects,
    "requirement_item": requirement_item.objects,
    "kanban_board": kanban_board.objects,
    "kanban_card": kanban_card.objects,
    "organisation": organisation.objects,
    "request_for_change": request_for_change.objects,
}


# Internal function
def get_object_from_destination(input_object, destination, location_id):
    """
    To stop the repeat code of finding specific objects using destination and location_id - we will import
    the object filter for it here - before returning it.
    :param object: The object we want to filter
    :param destination: The destination we are interested in
    :param location_id: The location_id
    :return:
    """
    input_object = input_object.filter(
        **{destination: location_id}
    )

    # Just send back the array
    return input_object


# Internal Function
def get_user_permissions(field, value):
    return (
        user_group.objects.filter(
            is_deleted=False,
            **{field: value},
        )
        .values(
            "username",
            "username__first_name",
            "username__last_name",
            "username__email",
            "group",
            "group__group_name",
            "group_leader",
            "permission_set",
            "permission_set__permission_set_name",
        )
        .order_by(
            "username__first_name",
            "username__last_name",
            "group__group_name",
            "permission_set__permission_set_name",
        )
    )


# Internal function
def set_object_from_destination(input_object, destination, location_id):
    """
    This function is used to set data against an object using the destination and location data.
    :param input_object: The input object that we are setting data for
    :param destination: The destination we are interested in
    :param location_id: The location we are interested in
    :return:
    """
    setattr(input_object, destination, OBJECT_DICT[destination].get(pk=location_id))

    return input_object
