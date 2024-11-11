from prefect_dbt.cli.commands import DbtCoreOperation
from prefect import flow

@flow
def trigger_dbt_flow() -> str:
    result = DbtCoreOperation(
        commands=["dbt build -t dev_ryan"],
        project_dir="C:/Users/ryanh/GITHUB_FOLDERS/jaffle_shop/dbt-tutorial",
        profiles_dir="~/.dbt"
    ).run()
    print(result)  # Add this line to inspect the result
    return result

if __name__ == "__main__":
    ##trigger_dbt_flow.test()
    trigger_dbt_flow.serve(name="testing-deployment",
                     tags=["testing"])