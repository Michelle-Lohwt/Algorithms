class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> idxArr;
        int key;
        
        for(int i = 0; i < nums.size(); i++){
          key = target - nums[i];
            if(map.find(key) != map.end()){
              idxArr.push_back(map[key]);
              idxArr.push_back(i);
              return idxArr;
            }
          map.insert(make_pair(nums[i], i));
        }
    return {};
    }
};
