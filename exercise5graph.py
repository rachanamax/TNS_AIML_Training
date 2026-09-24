FRIENDS = {
    "Aisha": ["Ben", "Carla"],
    "Ben":   ["Aisha", "Dev"],
    "Carla": ["Aisha", "Dev"],
    "Dev":   ["Ben", "Carla", "Eli"],
    "Eli":   ["Dev"],
}


def add_person(graph, name):
    """Put name in the graph with no friends yet - unless already there."""
    if name not in graph:
        graph[name] = []


def add_friendship(graph, a, b):
    """Link a and b BOTH ways. Friendship is mutual."""
    add_person(graph, a)
    add_person(graph, b)

    if b not in graph[a]:
        graph[a].append(b)

    if a not in graph[b]:
        graph[b].append(a)


def friend_count(graph, name):
    """How many friends does name have?"""
    if name not in graph:
        return 0

    return len(graph[name])


def are_friends(graph, a, b):
    """Is there a direct link between a and b?"""
    if a not in graph:
        return False

    return b in graph[a]


def most_friends(graph):
    """Return the name with the most friends, and how many."""
    best = ""
    best_count = 0

    for name in graph:
        count = len(graph[name])

        if count > best_count:
            best = name
            best_count = count

    return best, best_count


# Testing the functions

print("Aisha's friends:", friend_count(FRIENDS, "Aisha"))

print("Are Aisha and Ben friends?",
      are_friends(FRIENDS, "Aisha", "Ben"))

print("Are Aisha and Eli friends?",
      are_friends(FRIENDS, "Aisha", "Eli"))

print("Person with most friends:", most_friends(FRIENDS))
