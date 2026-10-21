import requests
import pandas as pd

def test_posts_dataframe():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/")

    assert response.status_code == 200

    df = pd.DataFrame(response.json())

    assert len(df) == 100
    assert list(df.columns) == ["userId", "id", "title", "body"]
    assert df.iloc[0]["id"] == 1