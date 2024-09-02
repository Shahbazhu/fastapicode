import json
from typing import List
from models import Item

# JSON file to simulate a database
DATABASE_FILE = 'items.json'

def read_items() -> List[Item]:
    try:
        with open(DATABASE_FILE, 'r') as f:
            items = json.load(f)
        return [Item(**item) for item in items]
    except FileNotFoundError:
        return []

def write_items(items: List[Item]) -> None:
    with open(DATABASE_FILE, 'w') as f:
        json.dump([item.dict() for item in items], f, indent=4)

def find_item(item_id: int) -> Item:
    items = read_items()
    for item in items:
        if item.id == item_id:
            return item
    return None

def add_item(item: Item) -> None:
    items = read_items()
    items.append(item)
    write_items(items)

def update_item(item_id: int, item_data: Item) -> bool:
    items = read_items()
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = item_data
            write_items(items)
            return True
    return False

def delete_item(item_id: int) -> bool:
    items = read_items()
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            write_items(items)
            return True
    return False
