from utils import get_input

total_paper = 0
total_rippon = 0
for box in get_input(2):
    if not box: continue
    l, w, h = [int(x) for x in box.split('x')]
    sorted_dimensions = [l, w, h]
    sorted_dimensions.sort()
    total_rippon += 2*sorted_dimensions[0] + 2*sorted_dimensions[1] + l*w*h
    dimensions = [l*w, w*h, h*l]
    needed_paper = [2*x for x in dimensions]
    total_paper += (sum(needed_paper) + min(dimensions))
print(total_paper)
print(total_rippon)