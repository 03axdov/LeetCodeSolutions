function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    let prereq: Map<number, number[]> = new Map();
    
    // Build adjacency list
    for (let [course, pre] of prerequisites) {
        if (!prereq.has(course)) prereq.set(course, []);
        prereq.get(course)!.push(pre);
    }

    let visited: Set<number> = new Set();  // Nodes that have been fully processed
    let path: Set<number> = new Set();     // Nodes in the current DFS path

    function dfs(course: number): boolean {
        if (path.has(course)) return false;  // Cycle detected
        if (visited.has(course)) return true; // Already checked and safe

        path.add(course);
        if (prereq.has(course)) {
            for (let pre of prereq.get(course)!) {
                if (!dfs(pre)) return false;
            }
        }
        path.delete(course);  // Remove from path when done
        visited.add(course);  // Mark as fully processed

        return true;
    }

    // Check all courses
    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return false;
    }

    return true;
}
