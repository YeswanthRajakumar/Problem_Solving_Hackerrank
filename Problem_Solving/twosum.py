nums = [3,2,5,1]
target = 5
final_dict={}
for i in range(len(nums)):
        x=nums[i]
        y=target - nums[i]
        final_dict[x]=y
print(final_dict)
