// class ListNode {
//     val: number
//     next: ListNode | null
//     constructor(val?: number, next?: ListNode | null) {
//         this.val = (val===undefined ? 0 : val)
//         this.next = (next===undefined ? null : next)
//     }
// }


const getLength = (list: ListNode): number =>  {
    let curr = list;
    let getLength = 0;

    while(curr !== null) {
        curr = curr.next!;
        ++getLength;
    }

    return getLength;
}

const split = (list: ListNode): {f : ListNode, s : ListNode } => {
    const first = new ListNode(-1);
    first.next = list;
    let curr = first;
    let second = new ListNode(-1);
    let iterations = Math.floor(getLength(list) / 2);

    while(iterations > 0) {
        --iterations;
        curr = curr.next!;

        if(iterations === 0){
            let temp = curr.next;
            curr.next = null;
            second.next = temp;
        }
    }

    return {f : first.next!, s : second.next!};
}

const mergeH = (list1: ListNode, list2: ListNode): ListNode | null =>  {
    const res = new ListNode(-1);
    let curr = res;

    while(list1 !== null && list2 !== null) {
        if(list1.val < list2.val) {
            curr.next = list1;
            list1 = list1.next!;
        } else {
            curr.next = list2;
            list2 = list2.next!;
        }
        curr = curr.next;
    }

    if(list1 !== null) {
        curr.next = list1;
    } else if(list2 !== null){
        curr.next = list2;
    }

    return res.next;
};

const sortList = (head: ListNode | null): ListNode | null => {
    if(!head?.next) return head;
    let spl = split(head);
    
    return mergeH(sortList(spl.f)!, sortList(spl.s)!);
}