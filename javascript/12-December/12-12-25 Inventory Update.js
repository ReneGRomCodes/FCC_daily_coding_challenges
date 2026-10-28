/*
Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have
received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]],
return [[3, "apples"], [8, "bananas"]].

1. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]])
    should return [[3, "apples"], [8, "bananas"]].
2. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]])
    should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
3. update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]])
    should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
4. update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"],
[1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])
    should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"],
    [1, "Toothpaste"]].
 */

function updateInventory(inventory, shipment) {
    // Immediately return 'shipment' if 'inventory' is empty.
    if (inventory.length === 0) {
        return shipment;
    }

    // Indices for objects in inner lists.
    const [amountIndex, nameIndex] = [0, 1];

    // Dict for item lookups.
    const inventoryDict = {};
    inventory.forEach((item, index) => {
        inventoryDict[item[nameIndex]] = index;
    });

    for (const item of shipment) {
        const [amount, name] = [item[amountIndex], item[nameIndex]];

        if (inventoryDict[name] !== undefined) {
            inventory[inventoryDict[name]][amountIndex] += amount;
        } else {
            inventory.push([amount, name]);
            inventoryDict[name] = inventory.length - 1;
        }
    }

    return inventory;
}


console.log(updateInventory(
    [[2, "apples"], [5, "bananas"]],
    [[1, "apples"], [3, "bananas"]]));
console.log(updateInventory(
    [[2, "apples"], [5, "bananas"]],
    [[1, "apples"], [3, "bananas"], [4, "oranges"]]));
console.log(updateInventory(
    [],
    [[10, "apples"], [30, "bananas"], [20, "oranges"]]));
console.log(updateInventory(
    [[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]],
    [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]));
