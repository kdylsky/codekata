def make_route(temp, dungeons, route_lst): 
    if len(temp) > 0:
        route_lst.append(temp)
    for i in range(len(dungeons)):
        make_route(temp+[dungeons[i]], dungeons[0:i]+dungeons[i+1:], route_lst)
    return route_lst

def is_possible(k, route):
    for i in route: 
        if i[0] > k:
            return False
        else:
            k = k - i[1]
    if k >=0:
        return True
    else:
        return False


def solution(k, dungeons):
    route_lst = []
    routes = make_route([], dungeons, route_lst)
    result = []
    for route in routes:
        if is_possible(k, route):
            result.append(len(route))    
    return max(result)