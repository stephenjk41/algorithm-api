from operator import le
from fastapi import APIRouter

router = APIRouter()


@router.post("/search/binary")
async def run_binary_search_sorted(arr: list[int], target: int):
    # Python3 Program for recursive binary search.
    # Returns index of x in arr if present, else -1
    step = []
    def binary_search(arr, left, right, x, count):
        # Check base case
        count += 1
        if right >= left:
            mid = left + (right - left) // 2
            # If element is present at the middle itself
            if arr[mid] == x:
                step.append({arr[mid]})
                return mid, count
            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                step.append({arr[left], (arr[mid-1])})
                return binary_search(arr, left, mid - 1, x, count)
            # Else the element can only be present
            # in right subarray
            else:
                step.append({arr[left], (arr[mid+1])})
                return binary_search(arr, mid + 1, right, x, count)
        else:
            # Element is not present in the array
            return -1, count

    result, count = binary_search(arr, 0, len(arr) - 1, target, 0)

    if result != -1:
        return {"text": f"Element is present at index {result} in {count} steps", "steps": step}
    else:
        return "Element is not present in array"
