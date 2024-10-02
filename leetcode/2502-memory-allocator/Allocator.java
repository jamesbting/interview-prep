class Allocator {

    private final int[] memory;
    
    public Allocator(int n) {
        this.memory = new int[n];
    }
    
    public int allocate(final int size, final int mID) {
        //sliding window
        int cur = 0;
        for (int i = 0; i < this.memory.length; i++) {
            if (this.memory[i] == 0) {
                cur++;
                if (cur == size) {
                    for (int j = i; j >= i - size + 1; j--) {
                        this.memory[j] = mID;
                    }
                    return i-size+1;
                }
            } else {
                cur = 0;
            }
        }
        return -1;
    }
    
    public int free(int mID) {
        int count = 0;
        for(int i = 0; i < this.memory.length; i++) {
            if(this.memory[i] == mID) {
                this.memory[i] = 0;
                count++;
            }
        }
        return count;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.free(mID);
 */