from db import schemas

# Список городов TODO: определить решение, к примеру добавить бд городов или json
cities_list = ["Москва", "Багдад"]

# Преобразование списка городов в список экземпляров класса CitiesHintModel
cities_hint = [schemas.CitiesHintModel(id=i, name=city) for i, city in enumerate(cities_list, start=1)]


def convert_to_pagination(data, page, size):  # TODO: make a paginator method
    start = (page - 1) * size
    end = start + size
    users = data[start: end]
    meta = schemas.PrivateUsersListMetaDataModel(
        pagination=schemas.PaginatedMetaDataModel(
            total=len(data),
            page=page,
            size=size
        ),
        hint=schemas.PrivateUsersListHintMetaModel(
            city=cities_hint
        )
    )
    return {"data": users, "meta": meta}
