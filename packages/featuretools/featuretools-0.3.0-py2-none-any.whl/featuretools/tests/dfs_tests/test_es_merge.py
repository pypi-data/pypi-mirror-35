import featuretools as ft
import pytest


def test_dfs():
    data = ft.demo.load_mock_customer()
    transactions_df = data["transactions"].merge(data["sessions"]).merge(data["customers"])
    products_df = data["products"]
    es = ft.EntitySet(id="transactions")
    es = es.entity_from_dataframe(entity_id="transactions",
                                  dataframe=transactions_df,
                                  index="transaction_id",
                                  time_index="transaction_time",
                                  variable_types={"product_id": ft.variable_types.Categorical})
    es = es.entity_from_dataframe(entity_id="products",
                                  dataframe=products_df,
                                  index="product_id")
    new_relationship = ft.Relationship(es["products"]["product_id"],
                                       es["transactions"]["product_id"])
    es = es.add_relationship(new_relationship)
    es = es.normalize_entity(base_entity_id="transactions",
                             new_entity_id="sessions",
                             index="session_id",
                             make_time_index="session_start",
                             additional_variables=["device", "customer_id", "zip_code", "session_start", "join_date"])
    es = es.normalize_entity(base_entity_id="sessions",
                             new_entity_id="customers",
                             index="customer_id",
                             make_time_index="join_date",
                             additional_variables=["zip_code", "join_date"])
    feature_matrix, feature_defs = ft.dfs(entityset=es,
                                          target_entity="products")