from tests.conftest import client


def test_create_batches():
    response = client.post('/batch/',
                           json=[
                               {
                                   "СтатусЗакрытия": True,
                                   "ПредставлениеЗаданияНаСмену": "string",
                                   "Линия": "string",
                                   "Смена": "string",
                                   "Бригада": "string",
                                   "НомерПартии": 0,
                                   "ДатаПартии": "2024-03-06",
                                   "Номенклатура": "string",
                                   "КодЕКН": "string",
                                   "ИдентификаторРЦ": "string",
                                   "ДатаВремяНачалаСмены": "2024-03-06T19:44:08.731Z",
                                   "ДатаВремяОкончанияСмены": "2024-03-06T19:44:08.731Z"
                               }
                           ])
    assert response.status_code == 201


def test_create_batches_with_missing_fields():
    response = client.post('/batch/',
                           json=[
                               {
                                   "СтатусЗакрытия": True,
                                   "НомерПартии": 1,
                               }
                           ])
    assert response.status_code == 422


def test_get_batches_with_filters():
    response = client.get('/batch/filter',
                          params={
                              "closing_status": True,
                              "submission": "string",
                              "line": "string",
                              "shift": "string",
                              "crew": "string",
                              "number": 0,
                              "batch_date": "2024-03-06",
                          })
    assert len(response.json()) == 1


def test_get_batch_by_id():
    response = client.get('/batch/1')
    assert response.status_code == 200


def test_update_patch():
    response = client.patch('/batch/1',
                            json={
                                    "СтатусЗакрытия": False,
                                    "ПредставлениеЗаданияНаСмену": "string",
                                    "Линия": "string",
                                    "Смена": "string",
                                    "Бригада": "string",
                                    "НомерПартии": 23,
                                    "ДатаПартии": "2024-03-07",
                                    "Номенклатура": "string22",
                                }
                            )
    assert response.status_code == 200
