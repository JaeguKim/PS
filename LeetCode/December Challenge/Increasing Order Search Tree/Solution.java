/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public void inorder(List<TreeNode> list, TreeNode root) {
        if (root == null) {
            return;
        }
        inorder(list,root.left);
        list.add(root);
        inorder(list,root.right);
    }
    
    public TreeNode increasingBST(TreeNode root) {
        if (root == null) {
            return null;
        }
        List<TreeNode> list = new ArrayList<>();
        inorder(list,root);
        for (int i=0; i<list.size()-1; i++){
            list.get(i).left = null;
            list.get(i).right = list.get(i+1);
        }
        list.get(list.size()-1).left = null;

        return list.get(0);
    }
}