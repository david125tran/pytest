# PyTest Playground

## 01 - PyTest 
 - **Part 1** - PyTest conventions.
 - **Part 2** - Testing w/code isolation to avoid API calls. 
 - **Part 3** - Behavior-driven development (BDD). Gherkin language automated testing. 

## 02 - Diving Deeper into PyTest
 - Class testing. 

## 03 - PyTest Fixtures
 - **Part 1** - PyTest fixtures. Test setup and teardown with `yield` instead of `return`. 
 - **Part 2** - FastAPI's `TestClient` client session. API testing. 
 - **Part 3** - Fixture scope. Conftest. API testing. 
   - `tmp_path_factory` fixture - Creating temporary directories for unit testing. 
   - `capsys` fixture - Capture anything printed to the terminal.
   - `monkeypatch` fixture - Temporarily replace things. 
   - [More fixtures](https://docs.pytest.org/en/6.2.x/fixture.html)

## 04 - Parameterization Techniques
 - Parameterization, running tests multiple times with different inputs. 
   - Manual parameterization w/for loop
   - Parmeterization fixture (most common). `@pytest.mark.parametrize(...)`
   - Fixture parameterization. `@pytest.fixture(params=[...])`
   - Fixture parameterization with custom IDs. `ids=lambda p: ...`
   -  Dynamic test generation
   - Fixture parameterization for infrastructure.
   Factory fixture. 
