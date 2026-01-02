import numpy as np

coords = []
with open("lvl9-0.txt", "r") as f:
    for line in f.readlines():
        coords.append(tuple(int(e) for e in line.strip().split(",")))


def area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y2 - y1) + 1)


N = len(coords)


# Lvl 1
def max_area_all():
    maxval = -1
    for i in range(N):
        for j in range(i + 1, N):
            new_area = area(*coords[i], *coords[j])
            # print(f"{coords[i]}, {coords[j]} => {new_area}")
            maxval = max(maxval, new_area)

    print(maxval)
    return maxval


def orientation(p1, p2, p3):
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) > (p2[1] - p1[1]) * (p3[0] - p1[0])


def segments_intersect(p1, p2, a1, a2):
    if p1==a1 or p1 ==a2 or p2 ==a1 or p2 ==a2:
        return False
    return (orientation(p1, a1, a2) != orientation(p2, a1, a2)) and (
        orientation(p1, p2, a1) != orientation(p1, p2, a2)
    )


def is_on_segment(
    point: tuple[int, int], segment_start: tuple[int, int], segment_end: tuple[int, int]
):
    return any([point[i] == segment_start[i] == segment_end[i] for i in range(2)])


# This is correct but completely useless as by definition it will be inside
def raycast_collisions(x, y, vertices):
    N = len(vertices)
    collisions = 0
    for i in range(N):
        u, v = vertices[i], vertices[(i + 1) % N]
        if ((u[0] < x and v[1] > x) or (u[0] > x and u[1] < x)) and (u[1] < x):
            collisions += 1
    return collisions


maxval = 0
for i in range(N):
    for ii in range(i + 1, N):
        print()
        # v1, v3 = [coords[(i + j) % N] for j in range(2)]
        v1 = coords[i]
        v3 = coords[ii]
        v2 = (v1[0], v3[1])
        v4 = (v3[0], v1[1] )

        for corner in (v2, v4):  # v1 and v3 are guaranteed to be inside
            colls = raycast_collisions(*corner, coords)
            # print(f"{corner} <-> {coords} == {colls}")
            if colls % 2:
                print(f"rect {v1} {v3} failed on vertex {corner}")
                break
        else:
            v1p = ((v1[0] + v2[0]) // 2, (v1[1] + v2[1]) // 2)
            v2p = ((v2[0] + v3[0]) // 2, (v2[1] + v3[1]) // 2)
            v3p = ((v3[0] + v4[0]) // 2, (v3[1] + v4[1]) // 2)
            v4p = ((v4[0] + v1[0]) // 2, (v4[1] + v1[1]) // 2)
            print((v1,v2,v3,v4), (v1p, v2p, v3p, v4p))
            for corner in (v1p, v2p, v3p, v4p):
                # The next step, intersections will not trigger if there are three walls inside the are, but one is not
                colls = raycast_collisions(*corner, coords)

                if colls % 2:
                    print(f"rect {v1} {v3} failed on extension {corner}")
                    break
            else:
                corners = (v1, v2, v3, v4)
                for j in range(4):
                    bad = False
                    for k in range(N):
                        if segments_intersect(
                            corners[j],
                            corners[(j + 1) % 4],
                            coords[k],
                            coords[(k + 1) % N],
                        ):
                            bad = True
                            break
                    if bad:
                        print(
                            f"rect {v1} {v3} failed on side {
                                corners[j], corners[(j + 1) % 4]
                            } <--> {coords[k], coords[(k + 1) % N]}"
                        )
                        break

                else:
                    new_area = area(*v1, *v3)
                    maxval = max(maxval, new_area)
                    print(f"-Good: {v1},{v3}, {maxval}")
