var hasCycle = function(head) {
   let set = new Set()
   let cur = head;
   while(cur){
       if(set.has(cur)){
           return true;
       }
       else{
           set.add(cur);
       }
       cur = cur.next;
   }
   return false
};