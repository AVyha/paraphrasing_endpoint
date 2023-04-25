import math
import random

import uvicorn
from fastapi import FastAPI
import nltk

app = FastAPI()


def paraphrase_by_np(tree: nltk.tree.Tree) -> None:
    """
    This is a recursive function, that moves along the branches and shuffles the NPs.
    Helps to find all possible permutations.
    :param tree:
    :return:
    """
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
                paraphrase_by_np(element)
        else:
            index = list(index_values_to_shuffle.keys())
            vals = list(index_values_to_shuffle.values())
            random.shuffle(vals)

            for key, val in zip(index, vals):
                tree[key] = val

    for element in tree:
        paraphrase_by_np(element)


def permutations_count(tree: nltk.tree.Tree, count: int = 1) -> int:
    """
    This recursion function moving along the branches finds the count of all existing permutations.
    :param tree:
    :param count:
    :return:
    """
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


def paraphrase(tree: str) -> list[str]:
    """
    This function finds all existing permutations of the current tree
    :param tree:
    :return:
    """
    tree = nltk.tree.Tree.fromstring(tree)
    perm_count = permutations_count(tree)
    all_permutations = set()

    while len(all_permutations) < perm_count:
        paraphrase_by_np(tree)
        all_permutations.add(" ".join(str(tree).split()))

    return list(all_permutations)


@app.get("/paraphrase")
def paraphrase_endpoint(tree: str, limit: int = 20):
    result = paraphrase(tree)[:limit]

    return {"status": 201, "paraphrases": [{
        "tree": phrase,
        "sentence": " ".join(nltk.tree.Tree.fromstring(phrase).leaves())
    } for phrase in result]}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
