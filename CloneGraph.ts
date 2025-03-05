class _Node {
    val: number
    neighbors: _Node[]

    constructor(val?: number, neighbors?: _Node[]) {
        this.val = (val===undefined ? 0 : val)
        this.neighbors = (neighbors===undefined ? [] : neighbors)
    }
}


let seen: Map<number, _Node> = new Map();

function getNode(val: number): _Node {
    let nodeCopy: _Node;
    if (!seen.has(val)) {
        nodeCopy = new _Node(val);
        seen.set(val, nodeCopy);
    } else {
        nodeCopy = seen.get(val)!;
    }
    return nodeCopy;
}

function cloneGraphInner(node: _Node | null): _Node | null {
    if (node == null) return null;
    
    let nodeCopy: _Node = getNode(node.val);
	
    let oldNeighbors = node.neighbors;
    let copyNeighbors: _Node[] = [];
    for (let i=0; i < oldNeighbors.length; i++) {
        if (!seen.has(oldNeighbors[i].val)) {
            let neighborNode: _Node | null = cloneGraphInner(oldNeighbors[i]);
            if (neighborNode) copyNeighbors.push(neighborNode);
        } else {
            copyNeighbors.push(seen.get(oldNeighbors[i].val)!);
        }
        
    }
    nodeCopy.neighbors = copyNeighbors;

    return nodeCopy;
};

function cloneGraph(node: _Node | null): _Node | null {
    seen = new Map();
    return cloneGraphInner(node);
}