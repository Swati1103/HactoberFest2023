#include <bits/stdc++.h>
using namespace std

class Solution{
public:
    bool check(string &s, int i, int j){
        while(i<j){
            if(s[i]!=s[j])
            return false;
            
            i++;
            j--;
        }
        return true;
    }
    int result(int x,int n,string &str,vector<int>&v){
        if(x==n)
        return 0;
        
        int mini = INT_MAX;
        if(v[x]!=-1)
        return v[x];
        
        for(int i=x;i<n;i++){
            if(check(str,x,i)){
                int c = 1+result(i+1,n,str,v);
                mini = min(mini,c);
            }
        }
        return v[x]=mini;
    }
    int palindromicPartition(string str)
    {
        // code here
        int n=str.size();
        vector<int>v(n,-1);
        
        return result(0,n,str,v)-1;
    }
};
int main()
{
  int t;
  cin>>t;
while(t--){
  string s;
  cin>>s;
  Solution p;
  cout<<p.palindromicPartition(s)<<"\n";
}
return 0;
}
