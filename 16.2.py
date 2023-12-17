import numpy as np


def main():
    # filename = '16.1test.txt'
    filename = '16.1input.txt'
    
    with open(filename) as f:
        mirrors = [list(line.strip()) for line in f]
    mirrors = np.array(mirrors)

    max_i, max_j = mirrors.shape

    enter_beams = [(0, j, 1, 0) for j in range(max_j)] + \
                  [(max_i - 1, j, -1, 0) for j in range(max_j)] + \
                  [(i, 0, 0, 1) for i in range(max_i)] + \
                  [(i, max_j - 1, 0, -1) for i in range(max_i)]
    energized_all = []
    for enter_beam in enter_beams:
        energized = set()
        rays = {enter_beam}
        all_rays = set()
        rays_next = set()
        while len(rays) > 0:
            for ray_i, ray_j, dir_i, dir_j in rays:
                energized.add((ray_i, ray_j))
                if (ray_i, ray_j, dir_i, dir_j) in all_rays:
                    continue
                all_rays.add((ray_i, ray_j, dir_i, dir_j))
                if (mirrors[ray_i, ray_j] == '.' or
                    mirrors[ray_i, ray_j] == '-' and dir_i == 0 or
                    mirrors[ray_i, ray_j] == '|' and dir_j == 0):
                    next_i, next_j = ray_i + dir_i, ray_j + dir_j
                    if 0 <= next_i < max_i and 0 <= next_j < max_j:
                        rays_next.add((next_i, next_j, dir_i, dir_j))
                elif mirrors[ray_i, ray_j] == '-':
                    rays_next.add((ray_i, ray_j, 0, -1))
                    rays_next.add((ray_i, ray_j, 0, 1))
                elif mirrors[ray_i, ray_j] == '|':
                    rays_next.add((ray_i, ray_j, -1, 0))
                    rays_next.add((ray_i, ray_j, 1, 0))
                elif mirrors[ray_i, ray_j] == '/':
                    next_i, next_j = ray_i - dir_j, ray_j - dir_i
                    if 0 <= next_i < max_i and 0 <= next_j < max_j:
                        rays_next.add((next_i, next_j, -dir_j, -dir_i))
                else:
                    next_i, next_j = ray_i + dir_j, ray_j + dir_i
                    if 0 <= next_i < max_i and 0 <= next_j < max_j:
                        rays_next.add((next_i, next_j, dir_j, dir_i))
            rays = rays_next
            rays_next = set()
        energized_all.append(len(energized))

    print(max(energized_all))

    
if __name__ == '__main__':
    main()
