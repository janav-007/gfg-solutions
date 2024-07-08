#User function Template for python3

class Solution:
    def search(self,arr,key):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == key:
                return mid
                
            if arr[mid] >= arr[left]:
                if key >= arr[left] and key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if key <= arr[right] and key > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends