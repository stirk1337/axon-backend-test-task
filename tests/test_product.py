from tests.conftest import client


def test_create_products():
    response = client.post(
        "/product/",
        json=[
            {
                "УникальныйКодПродукта": "string",
                "НомерПартии": 0,
                "ДатаПартии": "2024-03-06",
            }
        ],
    )
    assert response.status_code == 201


def test_aggregate_product():
    response = client.patch(
        "/product/aggregate", json={"batch_id": 1}, params={"code": "string"}
    )
    assert response.status_code == 200


def test_already_aggregated_product():
    response = client.patch(
        "/product/aggregate", json={"batch_id": 1}, params={"code": "string"}
    )
    assert response.status_code == 400
