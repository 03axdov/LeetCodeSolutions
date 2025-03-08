class TreeNode {
        val: number
        left: TreeNode | null
        right: TreeNode | null
        constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
            this.val = (val===undefined ? 0 : val)
            this.left = (left===undefined ? null : left)
            this.right = (right===undefined ? null : right)

    }
}


function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (!root) return false;
    return traverse(root, targetSum, 0);
};

function traverse(root: TreeNode | null, targetSum: number, currentSum: number): boolean {
    if (!root) return false;
    currentSum += root.val;

    if (!root.left && !root.right) return targetSum == currentSum;
    else return traverse(root.left, targetSum, currentSum) || traverse(root.right, targetSum, currentSum);
}