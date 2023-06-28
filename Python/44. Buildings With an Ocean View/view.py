def get_buildings_with_ocean_view(heights):
    ocean_view = []
    max_height = 0

    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > max_height:
            ocean_view.append(i)
            max_height = heights[i]

    ocean_view.reverse()

    return ocean_view

building_heights = [4,3,2,1]
result = get_buildings_with_ocean_view(building_heights)
print(result) 