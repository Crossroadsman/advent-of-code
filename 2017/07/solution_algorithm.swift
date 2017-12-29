// This algorithm will solve the problem recursively
// WARNING: this can infinite loop if it is passed invalid data
func solver(list: [(String, [String])]) -> String {
    
    if list.count == 0 {
        return "No items in list"
    }
    
    if list.count == 1 {
        return list[0].0
    }
    
    var new_list = list.filter { !$0.1.isEmpty }
    let children = Set( list.flatMap { $0.1 } )
    
    new_list = list.filter { !children.contains($0.0) }
    
    return solver(list: new_list)
    
}

let test_data = [
    ("pbga", []),
    ("xhth", []),
    ("ebii", []),
    ("ktlj", []),
    ("fwft", ["ktlj","cntj","xhth"]),
    ("qoyg", []),
    ("padx", ["pbga", "havc", "qoyg"]),
    ("tknk", ["ujml", "padx", "fwft"]),
    ("jptl", []),
    ("ujml", ["gyxo", "ebii", "jptl"]),
    ("gyxo", []),
    ("cntj", []),
]


solver(list: test_data)
