import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--tenant_name", default="au-n-um1259", help="Specify the tenant's name"
    )
    parser.addoption(
        "--tags_list",
        default="sanity or basic",
        help="Pytest tags to filter tests. For more information, refer to the pytest documentation on tag expressions.",
    )
    parser.addoption("--locust_tags_list", default="basic", help="Locust tags to filter tests. For more information, refer to the locust documentation on tag expressions.")
    parser.addoption("--locust_exclude_tags_list", default="", help="Locust tags to filter out tests. For more information, refer to the locust documentation on tag expressions.")
    parser.addoption("--num_users", default="1", help="Number of users")
    parser.addoption("--spawn_rate", default="1", help="Spawn rate")
    parser.addoption("--num_iterations", default="1", help="Number of iterations")
    parser.addoption("--dry_run", default="false", help="Dry run")


@pytest.fixture(scope="session", autouse=True)
def user_input(request):
    tenant_name = request.config.getoption("--tenant_name")
    tags_list = request.config.getoption("--tags_list")
    num_users = request.config.getoption("--num_users")
    spawn_rate = request.config.getoption("--spawn_rate")
    num_iterations = request.config.getoption("--num_iterations")
    dry_run = request.config.getoption("--dry_run")

    return {
        "tenant_name": tenant_name,
        "tags_list": tags_list,
        "num_users": num_users,
        "spawn_rate": spawn_rate,
        "num_iterations": num_iterations,
        "dry_run": dry_run,
    }