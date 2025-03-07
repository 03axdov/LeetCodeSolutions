class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function splitList(head: ListNode): ListNode[] {
    return []
}

function mergeLists(head1: ListNode, head2: ListNode): ListNode {
    return new ListNode(-1);
}

function sortList(head: ListNode | null): ListNode | null {
    if (!head?.next) return head;
    let splitted: ListNode[] = splitList(head);

    return mergeLists(splitted[0], splitted[1]);
};