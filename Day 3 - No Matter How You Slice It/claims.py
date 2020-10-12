from typing import List, Tuple, Dict, Set
from dataclasses import dataclass


@dataclass
class Claim:
    claim_id: int
    distance_left: int
    distance_top: int
    width: int
    height: int


def parse_input(input_filename: str) -> List:
    claims: List[Claim] = []
    with open(input_filename) as f:
        for line in f:
            # remove # symbol and newline
            line = line[1:].strip()
            # get id
            [claim_id, rest] = line.strip().split("@")
            claim_id = claim_id.strip()
            [distances, area] = rest.strip().split(":")
            distance_left, distance_top = distances.strip().split(",")
            width, height = area.strip().split("x")
            claims.append(
                Claim(
                    int(claim_id),
                    int(distance_left),
                    int(distance_top),
                    int(width),
                    int(height),
                )
            )

    return claims


def create_fabric(claims: List) -> Dict:
    fabric: Dict[Tuple[int, int], Set[int]] = {}
    # fabric[(12, 23)] = {6, 7} the patch 12, 23 is claimed both by ids 6 & 7
    for claim in claims:
        for x in range(claim.distance_left, claim.distance_left + claim.width):
            for y in range(claim.distance_top, claim.distance_top + claim.height):
                fabric.setdefault((x, y), {claim.claim_id})
                fabric[x, y].add(claim.claim_id)
    return fabric


def count_overlapping_fabric(fabric: Dict) -> int:
    overlap_counter = 0
    for patch in fabric:
        if len(fabric[patch]) > 1:
            overlap_counter += 1
    return overlap_counter


def find_non_overlapping_claim(fabric: Dict) -> int:
    all_claims = set()
    overalpping_claims = set()
    for patch in fabric:
        all_claims.update(fabric[patch])
        if len(fabric[patch]) > 1:
            overalpping_claims.update(fabric[patch])
    return (all_claims - overalpping_claims).pop()


if __name__ == "__main__":
    input_filename = "input"
    fabric = create_fabric(parse_input(input_filename))
    print("Part 1:", count_overlapping_fabric(fabric))
    print("Part 2:", find_non_overlapping_claim(fabric))
