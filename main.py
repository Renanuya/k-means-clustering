from rich.console import Console
from rich.table import Table

age_array = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22


def get_closest_center(age, cluster_1, cluster_2):
    c1_distance = abs(age - cluster_1)
    c2_distance = abs(age - cluster_2)
    if c2_distance > c1_distance:
        return cluster_1
    elif c1_distance >= c2_distance:
        return cluster_2


def find_cluster(cluster1, cluster2):
    c1_sum = 0
    c2_sum = 0
    c1_elements = 0
    c2_elements = 0

    for age in age_array:
        nearest_cluster = get_closest_center(age, cluster1, cluster2)
        if nearest_cluster == cluster2:
            c2_elements += 1
            c2_sum += age
        elif nearest_cluster == cluster1:
            c1_elements += 1
            c1_sum += age
    return c1_sum / c1_elements, c2_sum / c2_elements


last_c1 = c1
last_c2 = c2

for i in range(1, 5):
    c1, c2 = find_cluster(last_c1, last_c2)

    table = Table(title=f"C1 = {c1:.2f} / C2 = {c2:.2f}")
    table.add_column("Xi", justify="center", style="cyan", no_wrap=False)
    table.add_column("C1", justify="center", style="cyan", no_wrap=False)
    table.add_column("C2", justify="center", style="cyan", no_wrap=False)
    table.add_column("Distance 1", justify="center", style="cyan", no_wrap=False)
    table.add_column("Distance 2", justify="center", style="cyan", no_wrap=False)
    table.add_column("Nearest Cluster", justify="center", style="cyan", no_wrap=False)
    table.add_column("New Centroid", justify="center", style="cyan", no_wrap=False)

    for age in age_array:
        c1_distance = abs(age - last_c1)
        c2_distance = abs(age - last_c2)
        cluster = "1" if get_closest_center(age, last_c1, last_c2) == last_c1 else "2"
        new_cluster = c1 if cluster == "1" else c2
        table.add_row(str(age),
                      str(f"{last_c1:.2f}"),
                      str(f"{last_c2:.2f}"),
                      str(f"{c1_distance:.2f}"),
                      str(f"{c2_distance:.2f}"),
                      str(cluster),
                      str(f"{new_cluster:.2f}")
                      )

    last_c1 = c1
    last_c2 = c2
    console = Console()
    console.print(table)
