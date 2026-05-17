import pytest
from google.adk.evaluation import AgentEvaluator


@pytest.fixture(autouse=True)
def reset_data():
    from customer_service_agent.agent import reset_mock_data
    reset_mock_data()
    yield
    reset_mock_data()


def test_customer_service_agent():
    AgentEvaluator.evaluate(
        agent_module="customer_service_agent",
        eval_dataset_file_path_or_dir="customer_service_agent/eval.test.json",
        num_runs=1,
    )
