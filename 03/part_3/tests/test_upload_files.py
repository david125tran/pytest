from pathlib import Path
import pytest
from tempfile import TemporaryDirectory

@pytest.fixture(scope="session")
def tmp_file(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp('user_data')
    tmp_file = tmp_path / 'test_user_data.txt'
    tmp_file.write_text("Hello World!")
    yield tmp_file

# @pytest.fixture
# def tmp_file():
#     with TemporaryDirectory() as tmp_path:
#         tmp_path = Path(tmp_path)
#         tmp_file = tmp_path / 'test_user_data.txt'
#         tmp_file.write_text("Hello World!")
#         yield tmp_file

def test_upload_successful(client, tmp_file):
    with tmp_file.open("rb") as f:
        response = client.post(
            "/user/123/file",
            files={"file": ("test.txt", f, "text/plain")}
        )
    
    assert response.status_code == 200

def test_upload_file_has_expected_response(client, tmp_file):
    with tmp_file.open("rb") as f:
        response = client.post(
            "/user/123/file",
            files={"file": ("test.txt", f, "text/plain")}
        )

    json_resp = response.json()
    assert json_resp["user_id"] == 123
    assert json_resp["filename"] == "test.txt"
    assert json_resp["content"] == "Hello World!"

def test_upload_logs(tmp_file, client, capsys):
    with tmp_file.open("rb") as f:
        response = client.post(
            "/user/123/file",
            files={"file": ("test.txt", f, "text/plain")}
        )

    captured = capsys.readouterr()
    assert "Received file: test.txt from user 123" in captured.out