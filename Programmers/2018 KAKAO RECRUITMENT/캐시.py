def solution(cacheSize, cities):
    answer = 0
    len_cities = len(cities)

    cityarr = []

    for n in range(len_cities):
        cities_low = cities[n].lower()


        if cities_low in cityarr:
            cityarr.remove(cities_low)
            cityarr.append(cities_low)
            answer += 1

        else:
            if cacheSize > 0:
                if len(cityarr) == cacheSize:
                    cityarr.pop(0)
                cityarr.append(cities_low)
            answer += 5

    return answer
