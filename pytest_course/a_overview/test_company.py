import pytest
from Company import Company

@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")

def test_with_fixture(company: Company) ->None:
    print(f"Printing {company} from fixture")
    
def test_str(company: Company) ->None: 
    assert str(company) == f"{company.name}:{company.stock_symbol}"

@pytest.mark.parametrize(
    "company_name",
    ["Tik Tok", "Instagram", "Twitch"],
    ids = ["TIKTOKTEST", "INSTAGRAMTEST", "TWITCHTEST"],
    )
def test_parameters(company_name:str)->None:
    print(f"\nTEST with {company_name}")

@pytest.mark.parametrize(
    "company_object",
    [
        {"name": "Twitter", "stock_symbol":"TWT"},
        {"name": "Facebook", "stock_symbol":"FB"},
        {"name": "Coca cola", "stock_symbol":"CCL"},
        {"name": "Moderna" , "stock_symbol": "MDN"},
        {"name": "Pepsi", "stock_symbol": "PPS"},
    ],
    ids=["TW", "FB", "CC", "MD", "PS"],
)
def test_objects(company_object:list)->None:
    company = Company(company_object['name'], company_object['stock_symbol'])
    assert str(company) == f"{company.name}:{company.stock_symbol}"