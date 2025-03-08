class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function moveToFront(node: ListNode, head: ListNode, x: number): void {
    let current: ListNode | null = head;
    let newNode: ListNode = node;

    let inserted: boolean = false;

    while (current) {
        let nextNode: ListNode | null = current.next;

        if (nextNode && nextNode.val >= x) {
            current.next = newNode;
            newNode.next = nextNode;
            current = nextNode;
            inserted = true;
            continue;
        } else if (nextNode == node) {
            if (inserted) {
                current.next = node.next;
            }

            break;
        }

        current = current.next;
    }
}

function partition(head: ListNode | null, x: number): ListNode | null {

    let current: ListNode | null = head;
    let prevNode: ListNode | null = current;

    while (current) {
        let temp: ListNode = current;
        current = current.next;
        
        if (temp.val < x) {
            moveToFront(temp, head!, x);
            prevNode!.next = current;
        }

        prevNode = current;
        
    }

    return head;
};