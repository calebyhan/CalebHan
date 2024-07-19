import requests
import os

URL = "https://api.teleport.org/api/"


def search(query):
    response = requests.get(URL + f"cities/?search={query}").json()

    i = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Is this your city: " + response["_embedded"]["city:search-results"][i]["matching_full_name"])
        if input("Y/N: ").upper() == "Y":
            break
        i += 1
    return response["_embedded"]["city:search-results"][i]


def city(link, raw=False):
    link = link["_links"]["city:item"]["href"]
    response = requests.get(link).json()

    os.system('cls' if os.name == 'nt' else 'clear')

    if raw:
        return response

    print(f"Location: {response['full_name']}")
    print(f"ID: {response['geoname_id']}")
    print(f"Population: {response['population']}")
    print(f"Coordinates: ({response['location']['latlon']['latitude']}, {response['location']['latlon']['longitude']})")


def urban_area(ua, raw=False):
    response = requests.get(URL + "urban_areas/slug:" + ua + "/").json()

    os.system('cls' if os.name == 'nt' else 'clear')

    if raw:
        return response

    cities = [i["name"] for i in response["_links"]["ua:primary-cities"]]

    print(f"Name: {response['name']}")
    print(f"ID: {response['ua_id']}")
    print(f"Mayor: {response['mayor']}")
    print(f"Primary cities: {', '.join(cities)}")

    print()

    scores = requests.get(response['_links']["ua:scores"]['href']).json()

    print("Scores:")
    print(f"\tHousing: {scores['categories'][0]['score_out_of_10']}")
    print(f"\tCost of living: {scores['categories'][1]['score_out_of_10']}")
    print(f"\tSafety: {scores['categories'][7]['score_out_of_10']}")
    print(f"\tHealthcare: {scores['categories'][8]['score_out_of_10']}")
    print(f"\tEducation: {scores['categories'][9]['score_out_of_10']}")
    print(f"\tOverall score: {scores['teleport_city_score']}")


def list_urban_areas():
    response = requests.get(URL + "urban_areas/").json()

    for query in response["_links"]["ua:item"]:
        print(f"{query['name']}: {query['href'].split('slug:')[1][:-1]}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        main_1 = input("Do you want to search a [c]ity or an [u]rban area?: ").lower()
        if main_1 == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            city(search(input("Input a valid city: ")))
            break
        elif main_1 == "u":
            os.system('cls' if os.name == 'nt' else 'clear')
            ua_q = input("List urban areas? y/n: ").lower()
            if ua_q == "y":
                list_urban_areas()
                input()
            elif ua_q == "n":
                pass
            else:
                print("Invalid input. Try again.")
            os.system('cls' if os.name == 'nt' else 'clear')
            urban_area(input("Input a valid urban area: ").lower())
            break
        else:
            print("Invalid input. Try again.")


main()
