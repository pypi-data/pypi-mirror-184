# There are 3 common rectangle formats, and converting them all the time really is a pain in the a**
### Using this function, you get all 3 formats, center coordinates, height, width and the area


```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install get-rectangle-infos

from get_rectangle_infos import get_rectangle_information

format_1x4 = (0, 0, 100, 200)
format_4x2 = [(0, 0), (100, 0), (100, 200), (0, 200)]
format_2x2 = [(0, 0), (100, 200)]

print(get_rectangle_information(rect=(0, 0, 100, 200)))
# Rect(format_1x4=(0, 0, 100, 200), format_4x2=[(0, 0), (100, 0), (100, 200), (0, 200)], format_2x2=[(0, 0), (100, 200)], height=200, width=100, area=20000, center=(50, 100))

print(get_rectangle_information(rect=[(0, 0), (100, 0), (100, 200), (0, 200)]))
# Rect(format_1x4=(0, 0, 100, 200), format_4x2=[(0, 0), (100, 0), (100, 200), (0, 200)], format_2x2=[(0, 0), (100, 200)], height=200, width=100, area=20000, center=(50, 100))

print(get_rectangle_information(rect=[(0, 0), (100, 200)]))
# Rect(format_1x4=(0, 0, 100, 200), format_4x2=[(0, 0), (100, 0), (100, 200), (0, 200)], format_2x2=[(0, 0), (100, 200)], height=200, width=100, area=20000, center=(50, 100))



	
```




