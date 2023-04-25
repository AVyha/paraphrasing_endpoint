import math
import random

import uvicorn
from fastapi import FastAPI
import nltk

app = FastAPI()


def paraphrase(tree: nltk.tree.Tree) -> None:
    if tree.height() <= 3:
        return

    if tree.label() == "NP":
        counter = 0

        index_values_to_shuffle = {}

        for n, val in enumerate(tree):
            if val.label() == "NP":
                counter += 1
                index_values_to_shuffle[n] = val

        if counter < 2:
            for element in tree:
                paraphrase(element)
        else:
            index = list(index_values_to_shuffle.keys())
            vals = list(index_values_to_shuffle.values())
            random.shuffle(vals)

            for key, val in zip(index, vals):
                tree[key] = val

    for element in tree:
        paraphrase(element)


def permutations_count(tree: nltk.tree.Tree, count: int = 1) -> int:
    if tree.height() <= 3:
        return count

    if tree.label() == "NP":
        counter = 0

        for val in tree:
            if val.label() == "NP":
                counter += 1

        if counter >= 2:
            count *= math.factorial(counter)

    for element in tree:
        count = permutations_count(element, count)

    return count


@app.get("/paraphrase")
def paraphrase_endpoint(tree: str, limit: int = 20):
    result = set()
    tree = nltk.tree.Tree.fromstring(tree)
    max_count_permutation = min((permutations_count(tree), limit))

    while len(result) < max_count_permutation:
        paraphrase(tree)
        result.add(" ".join(tree.leaves()))

    return {"status": 201, "response": result}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
