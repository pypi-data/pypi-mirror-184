import schemathesis

schema = schemathesis.from_path('./pet3.json')
schema.base_url = "https://petstore3.swagger.io/api/v3/"


@schema.parametrize()
def test_api(case):
    response = case.call()

    print(case)
    print(response)
    print(response.text)
    print("***** ***** *****")

    case.validate_response(response)
