from dataclasses import dataclass
import pytest


@pytest.mark.parametrize("browser", ["Chrome", "Firefox", "Safari"])
def test_with_param(browser):
    pass


@pytest.mark.parametrize("browser", ["Chrome", "Firefox", "Safari"])
@pytest.mark.parametrize("test_user", ["Admin", "User", "Support"])
def test_with_matrix_param(browser, test_user):
    pass


@pytest.mark.parametrize("browser", [
    pytest.param("Chrome"),
    pytest.param("Firefox", marks=pytest.mark.xfail(reason="TASK-123")),
    pytest.param("Safari", marks=pytest.mark.slow)
])
def test_with_param_marks(browser):
    pass


@pytest.mark.parametrize("os", ["ubuntu-22.04", "windows-11", "macos-13.2"],
                         ids=["Ubuntu", "Windows", "Mac OS"])
@pytest.mark.parametrize("group_id", ["12321", "35423523", "dfsefsef"],
                         ids=["Admin", "User", "Support"])
def test_with_os(os, group_id):
    pass


@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def browser(request):
    if request.param == "Chrome":
        return "chrome.open_browser()"
    if request.param == "Firefox":
        return "firefox.open_browser()"
    if request.param == "Safari":
        return "safari.open_browser()"


def test_with_parametrized_fixture(browser):
    pass


@pytest.mark.parametrize("browser", ["Chrome", "Firefox"], indirect=True)
def test_with_indirect_parametrization(browser):
    pass


chrome_only = pytest.mark.parametrize("browser", ["Chrome"], indirect=True)

@chrome_only
def test_with_account(browser):
    pass




@dataclass
class User:
    id: int
    name: str
    age: int
    description: str

    def __repr__(self):
        return f"{self.name} ({self.id})"

user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)

def show_user(user):
    return f"User: {user.id}, {user.name}"

@pytest.mark.parametrize("user", [user1, user2], ids=repr)
def test_users(user):
    print()
