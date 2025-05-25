# my_awesome_lib/data_utils.py
def flatten_list(nested_list):
    """Spłaszcza listę zagnieżdżoną do jednej listy."""
    return [item for sublist in nested_list for item in sublist]

def remove_duplicates(data):
    """Usuwa duplikaty z listy."""
    return list(set(data))
